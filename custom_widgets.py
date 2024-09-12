from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.codeinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from styles import Styles


Builder.load_string("""

<CButton>:
    background_color: self.bg_color
    background_normal: ""
    on_press: root.pressed()
    on_release: root.released()
    
<CTextInput>:
    background_normal: ""
    background_color: self.bg_color
    font_name: "roboto-light.ttf"
    font_size: "16sp"   
    
<SignUpText>:
    color: self.bg_color

""")


class CButton(Button):
    bg_color=Styles.primary_color
    def pressed(self):
        self.background_color = (self.background_color[0], self.background_color[1], self.background_color[2], 0.8)

    def released(self):
        self.background_color = self.bg_color

class CTextInput(TextInput):
    bg_color = Styles.textinput_bg


class SignUpText(ButtonBehavior, Label):
    bg_color=Styles.primary_color