import RPi.GPIO as gpio

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton


RED_LED_PIN = 29
ORANGE_LED_PIN = 31
GREEN_LED_PIN = 33


class LedWidget(ToggleButton):
    def __init__(self, led_pin, **kwargs):
        super().__init__(**kwargs)

        self.led_pin = led_pin
        gpio.setup(led_pin, gpio.OUT)
        gpio.output(self.led_pin, gpio.LOW)

    def on_state(self, widget, value):
        if value == "down":
            gpio.output(self.led_pin, gpio.HIGH)
        else:
            gpio.output(self.led_pin, gpio.LOW)


class LedScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 3

        red_led = LedWidget(RED_LED_PIN)
        orange_led = LedWidget(ORANGE_LED_PIN)
        green_led = LedWidget(GREEN_LED_PIN)

        self.add_widget(red_led)
        self.add_widget(orange_led)
        self.add_widget(green_led)


class LedApp(App):
    def build(self):
        return LedScreen()


if __name__ == '__main__':
    gpio.setmode(gpio.BOARD)

    LedApp().run()