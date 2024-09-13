from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.actionbar import BoxLayout
from kivy.uix.accordion import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from styles import Styles


Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Home>:
    name: "Home"
    FloatLayout:
        Image:
            source: "computer.png"
        BoxLayout:
            orientation: 'vertical'
            BoxLayout:
                canvas.before:
                    Color:
                        rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint_y: None 
                height: dp(60)
                Label:
                    text: "interesting Fact"
                    font_name: 'roboto-black.ttf'
                    font_size: '20sp'
                    color: 1, 1, 1, 1
                AnchorLayout:
                    anchor_x: 'right'
                    padding: [0, 0, dp(30), 0]
                    Button:
                        size_hint:  None, None
                        size: dp(35), dp(35)
                        text: "h"
            BoxLayout: 
                Label:
                    text: "Result"
                    color: 0, 0, 0, 1
            AnchorLayout:
                anchor_y: 'center'
                anchor_x: 'center'
                size_hint: 1, 0.3
                BoxLayout: 
                    orientation: 'vertical'
                    height: self.minimum_height
                    size_hint_y: None
                    padding: dp(30)
                    spacing: dp(10)
                    BoxLayout:
                        size_hint: 1, 0.65
                        spacing: dp(10)
                        BoxLayout:
                            orientation:'vertical'
                            spacing: dp(10)
                            Label:
                                text: "Day"
                                color: 0, 0, 0, 1
                                size_hint_y: None
                                size: self.texture_size
                                font_name: 'roboto-medium.ttf'
                                font_size: '18sp'
                                halign: 'left'
                                text_size: self.size
                            CTextInput:
                                size_hint_y: None
                                height: dp(50)
                                id: 'day'
                        BoxLayout:
                            orientation:'vertical'
                            spacing: '5dp'
                            Label:
                                text: "Month"
                                color: 0, 0, 0, 1
                                size_hint_y: None
                                size: self.texture_size
                                font_name: 'roboto-medium.ttf'
                                font_size: '18sp'
                                halign: 'left'
                                text_size: self.size
                            CTextInput:
                                size_hint_y: None
                                height: dp(50)
                                id: 'month'
                    CButton: 
                        text: "Display Fact"
                        height: dp(60)
                        size_hint_y: None
                    
                    


""")

class Home(Screen):
    bg_color = Styles.primary_color
    