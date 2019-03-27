import os
from objection.utils.plugin import Plugin
from objection.state.connection import state_connection


class ClipboardPlugin(Plugin):
    def __init__(self, namespace):
        super().__init__(__file__, namespace, {
            'meta': 'Work with the Android Clipboard',
            'commands': {
                'monitor': {
                    'meta': 'Monitor the Android Clipboard',
                    'exec': self.monitor
                }
            }
        })
        self._inject()

    def monitor(self, args: list = None) -> None:
        """
            Starts a new objection job that monitors the Android clipboard
            and reports on new strings found.

            :param args:
            :return:
        """
        self.api.android_monitor_clipboard()


namespace = 'clipboard'
plugin = ClipboardPlugin
