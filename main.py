from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import Login
from kivy.core.window import Window
from signup import Signup


Window.size = (480, 640)
#classe Interface
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        login = Login()
        self.add_widget(login)
        signup = Signup()
        self.add_widget(signup)
class NumberApp(App):
    pass

NumberApp().run()
