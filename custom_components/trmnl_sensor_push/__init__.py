"""The TRMNL Sensor Push integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the TRMNL Sensor Push component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up TRMNL Sensor Push from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    await hass.async_add_executor_job(
        setup_integration, hass, entry
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if DOMAIN in hass.data:
        if 'listener' in hass.data[DOMAIN]:
            hass.data[DOMAIN]['listener']()  # Remove the listener
        hass.data.pop(DOMAIN)
    return True

def setup_integration(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Set up the integration."""
    from .trmnl_sensor_push import setup_platform
    setup_platform(hass, entry) 