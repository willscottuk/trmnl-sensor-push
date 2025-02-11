"""The TRMNL Sensor Push integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .trmnl_sensor_push import async_setup_entry, async_unload_entry

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the TRMNL Sensor Push component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up TRMNL Sensor Push from a config entry."""
    return await async_setup_entry(hass, entry)

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await async_unload_entry(hass, entry) 