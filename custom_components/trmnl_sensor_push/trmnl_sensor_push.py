"""Platform for TRMNL Sensor Push integration."""
import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_registry import async_get as async_get_entity_registry

# Get the logger
_LOGGER = logging.getLogger(__name__)

def setup_platform(hass: HomeAssistant, entry) -> None:
    """Set up the TRMNL Sensor Push platform."""
    def process_trmnl_entities():
        """Find and process entities with TRMNL label."""
        entity_registry = async_get_entity_registry(hass)
        
        # Get all entities with the TRMNL label
        trmnl_entities = [
            entity for entity in entity_registry.entities.values()
            if "TRMNL" in entity.labels
        ]
        
        # Log the number of TRMNL entities found
        _LOGGER.info(f"Found {len(trmnl_entities)} entities with TRMNL label")
        
        # Log the names of these entities
        for entity in trmnl_entities:
            _LOGGER.debug(f"TRMNL Entity Found: {entity.name or entity.entity_id}")

    # Run the processing function
    hass.add_job(process_trmnl_entities)
