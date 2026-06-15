from pynput import keyboard


class HotkeyManager:

    def __init__(self, callback):

        self.callback = callback

        self.listener = None

    def start(self):

        self.listener = keyboard.GlobalHotKeys(
            {
                "<ctrl>+<space>": self.callback
            }
        )

        self.listener.start()