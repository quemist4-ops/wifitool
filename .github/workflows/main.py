from kivy.app import App
from kivy.uix.label import Label

class WifiApp(App):
    def build(self):
        return Label(text="WiFi Scanner")

if __name__ == "__main__":
    WifiApp().run()
