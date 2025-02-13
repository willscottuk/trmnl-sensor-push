"""Sensor platform for Terminal Sensor Push."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Terminal Sensor Push sensor."""
    url = config_entry.data["url"]
    
    async_add_entities([TRMNLSensor(url)], True)


class TRMNLSensor(SensorEntity):
    """Representation of a Terminal Sensor Push sensor."""

    def __init__(self, url: str) -> None:
        """Initialize the sensor."""
        self._url = url
        self._attr_unique_id = f"trmnl_sensor_{url.split('/')[-1]}"
        self._attr_name = "TRMNL Sensor"
        self._state = None

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        # TODO: Implement actual data fetching from the TRMNL API
        self._state = "Unknown" 