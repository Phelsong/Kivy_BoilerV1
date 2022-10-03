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
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = GridLayout
        self.cols = 2
        self.add_widget(Label(text="User Name", width=50, height=20))
        self.username = TextInput(multiline=False, width=50, height=20)
        self.add_widget(self.username)
        self.add_widget(Label(text="password", width=50, height=20))
        self.password = TextInput(password=True, multiline=False, width=50, height=20)
        self.add_widget(self.password)
