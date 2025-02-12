from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .trmnl_sensor_push import setup_platform

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the TRMNL Sensor Push component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up TRMNL Sensor Push from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {}

    # Add update listener
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    # Set up the platform
    await hass.async_add_executor_job(setup_platform, hass, entry)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if DOMAIN in hass.data:
        domain_data = hass.data[DOMAIN]
        if entry.entry_id in domain_data:
            if 'listener' in domain_data[entry.entry_id]:
                domain_data[entry.entry_id]['listener']()
            domain_data.pop(entry.entry_id)

    return True

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)