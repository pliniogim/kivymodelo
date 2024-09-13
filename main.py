from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import Login
from kivy.core.window import Window


Window.size = (480, 640)
#classe Interface
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        login = Login()
        self.add_widget(login)

class NumberApp(App):
    pass

NumberApp().run()
