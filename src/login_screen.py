"""Login Page"""
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# local imports


# =================================================================
Builder.load_string(
    """
<LoginScreen>:
    GridLayout:
        columns:2
        rows:3          
        Label: 
            text: "User Name"
            text_size: self.width-20, self.height-20
            valign: 'center'
            halign: 'center'
            background: "blue"

        TextInput:
            multiline: False
            width: 50
            height: 20
            valign: 'center'
            halign: 'center'

        Label:
            text: 'Password'
            valign: 'center'
            halign: 'center'
            text_size: self.width-20, self.height-20
            background: 'blue'

        TextInput:
            multiline: False
            width: 50
            height: 20
            valign: 'center'
            halign: 'center'

        Button:
            text: "Login"
            text_size: self.width-40, self.height-40
            valign: 'center'
            halign: 'center'
            background: "grey"
            on_release: root.manager.current = 'SplashScreen'"""
)


class LoginScreen(Screen):
    pass
