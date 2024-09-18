from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.actionbar import BoxLayout
from kivy.uix.accordion import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from history import History
from mydatabase import Database
from styles import Styles
import random


Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Home>:
    name: "Home"
    FloatLayout:
        Image:
            id: bg_img
            source: "computer.png"
            fit_mode: "contain"
            pos_hint: {'center_x': 0.5, 'top': 1.1 }
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
                    text: "Interesting Fact"
                    #font_name: 'robotoblack.ttf'
                    font_size: '20sp'
                AnchorLayout:
                    anchor_x: 'right'
                    padding: [0, 0, dp(30), 0]
                    Button:
                        canvas.before:
                            Rectangle:
                                pos: self.pos 
                                size: self.size
                                source: "history.png"
                        size_hint:  None, None
                        size: dp(35), dp(35)
                        background_color: 0, 0, 0, 0
                        on_press: root.switchToHistory()

            BoxLayout: 
                Label:
                    text_size: self.width, None
                    id: result_placeholder
                    padding: [dp(20), dp(20)]
                    color: root.secondary_color
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
                                color: root.secondary_color
                                size_hint_y: None
                                size: self.texture_size
                                #font_name: 'robotomedium.ttf'
                                font_size: '18sp'
                                halign: 'left'
                                text_size: self.size
                            CTextInput:
                                size_hint_y: None
                                height: dp(50)
                                id: day
                        BoxLayout:
                            orientation:'vertical'
                            spacing: '5dp'
                            Label:
                                text: "Month"
                                color: root.secondary_color
                                size_hint_y: None
                                size: self.texture_size
                                #font_name: 'robotomedium.ttf'
                                font_size: '18sp'
                                halign: 'left'
                                text_size: self.size
                            CTextInput:
                                size_hint_y: None
                                height: dp(50)
                                id: month
                    CButton: 
                        text: "Display Fact"
                        #font_name: "robotomedium.ttf"
                        font_size: "18sp"   
                        height: dp(60)
                        size_hint_y: None
                        on_press: root.insertFact()
                        
                    
                    


""")


class Home(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def insertFact(self):
        day = self.ids.day.text
        month = self.ids.month.text
        print(day, month)
        Database.insertFact(day + month, "x@teste.mail",
                            f"Fact - Fact{random.randint(0, 1000)}")
        try:
            result = Database.getFact(day + month, "x@teste.mail")
            self.ids.bg_img.color = (1, 1, 1, 0.3)
            self.ids.result_placeholder.text = result
        except Exception as e:
            print(e)

    def switchToHistory(self):
        self.manager.current = "history"
