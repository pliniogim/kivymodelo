from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from login import Login
from kivy.core.window import Window
from signup import Signup
from mydatabase import Database
from home import Home


Window.size = (480, 640)
#classe Interface
class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #database test
        try: 
          Database.connecDataBase()
        except Exception as e:
          print(e)
        
        login = Login()
        self.add_widget(login)
        signup = Signup()
        self.add_widget(signup)
        home = Home()
        self.add_widget(home)
        
class NumberApp(App):
    pass

NumberApp().run()
