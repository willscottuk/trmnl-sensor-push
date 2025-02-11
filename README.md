# TRMNL Sensor Push for Home Assistant

This integration pushes state changes for entities tagged with "TRMNL" to a specified endpoint.

## Installation

### HACS Installation
1. Add this repository to HACS as a custom repository
2. Install the integration through HACS
3. Restart Home Assistant

### Manual Installation
1. Copy the `custom_components/trmnl_sensor_push` directory to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

## Configuration

No configuration is needed. The integration will automatically start monitoring for state changes of entities with the "TRMNL" tag.

## Usage

Add the "TRMNL" tag to any entity you want to monitor. When the state of these entities changes, the new state will be pushed to the configured endpoint.

## License

MIT License 