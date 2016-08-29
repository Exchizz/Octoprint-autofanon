# coding=utf-8

from __future__ import absolute_import

import octoprint.plugin
from octoprint.util import RepeatedTimer

class AutoFanOnPlugin(octoprint.plugin.StartupPlugin,
		octoprint.plugin.OctoPrintPlugin,
		octoprint.plugin.TemplatePlugin,
		octoprint.plugin.SettingsPlugin):

        def __init__(self):
                self._checkTempTimer = None
                self._interval = 5 # [secs]

        def on_after_startup(self):
                self._checkTempTimer = RepeatedTimer(self._interval, self.checkTemp, None, None, True)
                self._checkTempTimer.start()

                self._threshold = self._settings.get(["temp_threshold"]

        def checkTemp(self):
                temp_hotend = 0
                try:
                        temp_hotend = self._printer.get_current_temperatures()["tool0"]["actual"]
                except Exception,e:
                        self._logger.info("Not ready.. Exception: %s", str(e));

                if temp_hotend >= self._threshold:
                        self._printer.commands(["M106"])


        def get_settings_defaults(self):
                return dict(temp_threshold=50)

	def get_template_vars(self):
	        return dict(temp_threshold=self._settings.get(["temp_threshold"]))

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

__plugin_name__ = "AutoFanOn"


def __plugin_load__():
        global __plugin_implementation__
        __plugin_implementation__ = AutoFanOnPlugin()
