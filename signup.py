from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.actionbar import partial
from kivy.uix.actionbar import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder



Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
               
<Signup>:
    name: "signup"
    BoxLayout:
        padding: dp(20)
        orientation: 'vertical'
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.4
            Image:
                source: "computer.png"
        AnchorLayout:
            size_hint: 1, 0.6
            anchor_y: "top"   
            BoxLayout:
                size_hint_y: None
                height: self.minimum_height
                spacing: '15dp'
                padding: ('20dp', '20dp', '20dp', '20dp')
                orientation: 'vertical'
                Label: 
                    text: "Create your account"
                    sfont_size: '12sp'
                    halign: "left"
                    font_name: "roboto-black.ttf"
                    size_hint_y: None
                    size: self.texture_size
                    text_size: self.size
                    spacing: dp(10)
                    padding: [dp(30), 0, dp(30), 0]
                    color: 0, 0, 0, 1
                CTextInput:
                    multiline: False
                    hint_text: 'Email'
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    hint_text: "Password"
                    multiline: False
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    hint_text: "Password confirmation"
                    multiline: False
                    size_hint_y: None
                    height: dp(50)
                CButton:
                    text: "Signup"
                    size_hint_x: None
                    pos_hint:{"center_x": 0.5, "y":0}    
                    size_hint_y: None
                    height: dp(50)
                    width: dp(100)
""")


class Signup(Screen):
    pass