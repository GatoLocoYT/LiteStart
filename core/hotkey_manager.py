from pynput import keyboard


class HotkeyManager:

    def __init__(self, callback):

        self.callback = callback

        self.listener = None

    def start(self):

        print(
            "HotkeyManager iniciado"
        )

        self.listener = keyboard.GlobalHotKeys(
            {
                "<ctrl>+<alt>+<h>": self.on_hotkey
            }
        )

        self.listener.start()

    def on_hotkey(self):

        print(
            "HOTKEY DETECTADA"
        )

        self.callback()