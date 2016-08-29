# coding=utf-8

import octoprint.plugin

class AutoFanOnPlugin(octoprint.plugin.OctoPrintPlugin):
	def on_gcode(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
		self._logger.info("Received code: %s", gcode);
		if gcode and gcode == "M109":
			cmd = "M106"
		return cmd,

#	def sent_m106(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
#		if gcode and gcode == "M106":
#			self._logger.info("Just sent M106: {cmd}".format(**locals()))

__plugin_name__ = "AutoFanOn"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AutoFanOnPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.on_gcode,
#		"octoprint.comm.protocol.gcode.sent": __plugin_implementation__.sent_m106
	}

