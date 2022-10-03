""" Application File """
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, ShaderTransition
from kivy.lang import Builder

# local imports
from src.splash_screen import SplashScreen
from src.login_screen import LoginScreen

# =============================================================================
class Red_Moon(App):
    def build(self):
        SM = ScreenManager()
        SM.add_widget(SplashScreen(name='SplashScreen'))
        SM.add_widget(widget=LoginScreen(name='LoginScreen'))
        return SM


if __name__ == "__main__":
    Red_Moon().run()
