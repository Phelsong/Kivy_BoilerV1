""" Application File """
from imp import reload
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, ShaderTransition
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# local imports
from src.splash_screen import SplashScreen
from src.login_screen import LoginScreen

# =============================================================================
Builder.load_file('X:\\0.code_projects\\Red_Moon_pw34\\RedMoon.kv')


class RedMoon(App):
    """RedMoon"""
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='SplashScreen'))
        sm.add_widget(LoginScreen(name='LoginScreen'))
        return sm


if __name__ == "__main__":
    RedMoon().run()
