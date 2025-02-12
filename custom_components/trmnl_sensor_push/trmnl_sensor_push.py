"""The TRMNL Sensor Push integration."""
import requests
import logging
from datetime import datetime, timedelta

from homeassistant.core import HomeAssistant, callback
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_STATE_CHANGED
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, CONF_URL, MIN_TIME_BETWEEN_UPDATES

_LOGGER = logging.getLogger(__name__)

def create_entity_payload(state):
    """Create the payload for a single entity."""
    attributes = state.attributes
    return {
        "id": state.entity_id,
        "name": state.name if state.name else "unknown",
        "state": state.state,
        "area": attributes.get("area", "unknown"),
        "icon": attributes.get("icon", "mdi:help-circle"),
        "state_class": attributes.get("state_class", "unknown"),
        "unit_of_measurement": attributes.get("unit_of_measurement", "unknown"),
        "device_class": attributes.get("device_class", "unknown"),
        "friendly_name": attributes.get("friendly_name", "unknown")
    }

def setup_platform(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Set up the TRMNL Sensor Push platform."""
    url = entry.data[CONF_URL]
    
    # Store last update times for each entity
    last_updates = {}
    
    @callback
    def state_change_listener(event):
        """Handle state changes."""
        entity_id = event.data.get("entity_id")
        new_state = event.data.get("new_state")
        
        # Check if enough time has passed since last update
        now = datetime.now()
        if entity_id in last_updates:
            time_since_last_update = (now - last_updates[entity_id]).total_seconds()
            if time_since_last_update < MIN_TIME_BETWEEN_UPDATES:
                _LOGGER.debug(
                    f"Skipping update for {entity_id}: Too soon since last update"
                )
                return

        # if url is not set, raise an error
        if not url:
            _LOGGER.error("URL is not set")
            return

        if new_state and "TRMNL" in new_state.attributes.get("tags", []):
            # Create the payload in the required format
            payload = {
                "merge_variables": {
                    "entities": [create_entity_payload(new_state)]
                }
            }
            
            try:
                headers = {"Content-Type": "application/json"}
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
                _LOGGER.info(f"Data pushed for {entity_id}: {response.status_code}")
                # Update last update time
                last_updates[entity_id] = now
            except requests.RequestException as e:
                _LOGGER.error(f"Failed to push data for {entity_id}: {e}")

    # Store the listener function
    hass.data[DOMAIN][entry.entry_id]['listener'] = hass.bus.async_listen(
        EVENT_STATE_CHANGED, 
        state_change_listener
    )

    _LOGGER.info("TRMNL Sensor Push integration loaded with URL: %s", url)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up TRMNL Sensor Push from a config entry."""
    url = entry.data[CONF_URL]
    
    # Store last update times for each entity
    last_updates = {}
    
    @callback
    def state_change_listener(event):
        """Handle state changes."""
        entity_id = event.data.get("entity_id")
        new_state = event.data.get("new_state")
        
        # Check if enough time has passed since last update
        now = datetime.now()
        if entity_id in last_updates:
            time_since_last_update = (now - last_updates[entity_id]).total_seconds()
            if time_since_last_update < MIN_TIME_BETWEEN_UPDATES:
                _LOGGER.debug(
                    f"Skipping update for {entity_id}: Too soon since last update"
                )
                return

        if new_state and "TRMNL" in new_state.attributes.get("tags", []):
            # Create the payload in the required format
            payload = {
                "merge_variables": {
                    "entities": [create_entity_payload(new_state)]
                }
            }
            
            try:
                headers = {"Content-Type": "application/json"}
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
                _LOGGER.info(f"Data pushed for {entity_id}: {response.status_code}")
                # Update last update time
                last_updates[entity_id] = now
            except requests.RequestException as e:
                _LOGGER.error(f"Failed to push data for {entity_id}: {e}")

    # Remove existing listener if exists
    if DOMAIN in hass.data:
        hass.bus.async_remove_listener(EVENT_STATE_CHANGED, hass.data[DOMAIN])
    
    # Store the listener function so we can remove it later
    hass.data[DOMAIN] = state_change_listener
    hass.bus.async_listen(EVENT_STATE_CHANGED, state_change_listener)

    _LOGGER.info("TRMNL Sensor Push integration loaded with URL: %s", url)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if DOMAIN in hass.data:
        hass.bus.async_remove_listener(EVENT_STATE_CHANGED, hass.data[DOMAIN])
        del hass.data[DOMAIN]
    return True 