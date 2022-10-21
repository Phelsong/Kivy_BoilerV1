""" Application File """
# libs
import os
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, ShaderTransition
from kivy.lang import Builder

# local imports
from pages.splash.splash_screen import SplashScreen
from pages.login.login_screen import LoginScreen

# =============================================================================

Builder.load_file(f"{os.getcwd()}\\RedMoon.kv")


class RedMoon(App):
    """RedMoon"""
    def build(self):
        s_m = ScreenManager()
        s_m.add_widget(SplashScreen(name='SplashScreen'))
        s_m.add_widget(LoginScreen(name='LoginScreen'))
        return s_m


if __name__ == "__main__":
    RedMoon().run()
