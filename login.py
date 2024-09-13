from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.filechooser import FileChooserProgressBase
from kivy.uix.screenmanager import Screen
from constants import *
from mydatabase import Database
from kivy.lang import Builder

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignUpText custom_widgets                    

<Login>:
    name: "login"
    BoxLayout:
        padding: dp(20)
        orientation: 'vertical'
        BoxLayout:
            size_min: 1, 0.15
            Image:
                source: "computer.png"
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: "top"
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: '10dp'
                Label:
                    color: 0 , 0 , 0 , 1
                    font_size: '12sp'
                    halign: "left"
                    font_name: "roboto-black.ttf"
                    size_hint_y: None
                    size: self.texture_size
                    text_size: self.size
                    spacing: dp(10)
                    padding: [dp(30), 0, dp(30), 0]
                    text: "Login to your account"
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: 'Email'
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: 'Password'
                CButton:
                    id: loginbutton
                    text: "Login"
                    size_hint_x: None
                    pos_hint:{"center_x": 0.5, "y":0}
                    on_press: root.login()
                    size_hint_y: None
                    height: dp(50)
                    width: dp(100)
                    
        AnchorLayout:
            size_hint: 1, 0.1
            anchor_x: 'center'
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                Label:
                    text:"Don't have an account? "
                    color: 0, 0, 0, 1  
                    size_hint_x: None
                    size: self.texture_size
                SignUpText:    
                    text: 'Sign up'                      
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switchToSignup()
""")

class Login(Screen):
    def switchToSignup(self):
        self.manager.current = "signup"
        
    def login(self):
        email = self.ids.email.text
        password = self.ids.password.text
        if(Database.exist(email, password)):
            print("Login successfull")
        else:
            print("Login failed")
        