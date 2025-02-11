"""Config flow for TRMNL Sensor Push integration."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, CONF_URL, DEFAULT_URL

class TRMNLSensorPushConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for TRMNL Sensor Push."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, any] | None = None
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
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_URL, default=DEFAULT_URL): cv.string,
                }
            ),
            errors=errors,
        ) 