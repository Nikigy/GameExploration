from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGameApp(App):
    floating_ground_texture = ObjectProperty(None)

class  Background(Widget):
    pass

App().run()