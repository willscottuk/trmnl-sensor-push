from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_URL, DEFAULT_URL

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_URL, default=DEFAULT_URL): cv.string,
    }
)

class TRMNLSensorPushConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for TRMNL Sensor Push."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title="TRMNL Sensor Push",
                data={
                    CONF_URL: user_input[CONF_URL],
                }
            )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return TRMNLSensorPushOptionsFlow(config_entry)

class TRMNLSensorPushOptionsFlow(config_entries.OptionsFlow):
    """Handle TRMNL Sensor Push options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage TRMNL Sensor Push options."""
        errors: dict[str, str] = {}

        if user_input is not None:
            return self.async_create_entry(
                title="",
                data={
                    CONF_URL: user_input[CONF_URL],
                }
            )

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_URL,
                    default=self.config_entry.data.get(CONF_URL, DEFAULT_URL),
                ): cv.string,
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=schema,
            errors=errors,
        )