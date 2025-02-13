# TRMNL Sensor Push for Home Assistant

This integration pushes state changes for entities tagged with "TRMNL" to your TRMNL webhook endpoint.

## Installation

### HACS Installation
1. Add this repository to HACS as a custom repository
2. Install the integration through HACS
3. Restart Home Assistant

### Manual Installation
1. Copy the `custom_components/trmnl_sensor_push` directory to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

Installation [video](https://screen.studio/share/LFguEhAJ)

## Configuration

1. In Home Assistant, go to Configuration → Integrations
2. Click "+ ADD INTEGRATION" and search for "TRMNL Sensor Push"
3. Enter your TRMNL webhook URL
   - This URL should look like: `https://usetrmnl.com/api/custom_plugins/AAAA-d000-4000-8000-000000000000`
   - You can get this URL from your TRMNL custom plugin settings

## Usage

1. Add the "TRMNL" tag to any entity you want to monitor
2. When the state of these entities changes, the new state will be pushed to your TRMNL webhook
3. Updates are rate-limited to once every 5 minutes per entity to prevent overwhelming the endpoint

## Troubleshooting

Check the Home Assistant logs for any error messages. Common issues:
- Invalid webhook URL
- Network connectivity problems
- Rate limiting (updates are limited to once every 5 minutes per entity)
- Ensure you have the integration enabled in Home Assistant
- Ensure you have the TRMNL label created and assigned to some entities in Home Assistant

## License

MIT License 