from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from mydatabase import Database

from styles import Styles


Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<history>:
    name: "history"
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
                text: "History"
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
                            source: "arrow_back.png"
                    size_hint:  None, None
                    size: dp(35), dp(35)
                    background_color: 0, 0, 0, 0
                    on_press: root.goToHome()
        BoxLayout:
            ScrollView:
                do_scroll_y: True
                Label:
                    id: texto
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: [dp(20), dp(20)]
                    color: root.secondary_color
""")


class History(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def on_pre_enter(self, *args):
        result = Database.getAllFact()
        self.ids.texto.text = result

    def goToHome(self):
        self.manager.current = "Home"
