import requests
import logging

from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.typing import ConfigType
from homeassistant.const import EVENT_STATE_CHANGED

DOMAIN = "trmnl_sensor_push"
URL = "https://stuarteggerton.com/example"

_LOGGER = logging.getLogger(__name__)

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    @callback
    def state_change_listener(event):
        entity_id = event.data.get("entity_id")
        new_state = event.data.get("new_state")

        if new_state and "TRMNL" in new_state.attributes.get("tags", []):
            payload = {
                "entity_id": entity_id,
                "state": new_state.state,
                "attributes": new_state.attributes
            }
            
            try:
                response = requests.post(URL, json=payload)
                response.raise_for_status()
                _LOGGER.info(f"Data pushed for {entity_id}: {response.status_code}")
            except requests.RequestException as e:
                _LOGGER.error(f"Failed to push data for {entity_id}: {e}")

    hass.bus.listen(EVENT_STATE_CHANGED, state_change_listener)

    _LOGGER.info("TRMNL Sensor Push integration loaded.")
    return True 