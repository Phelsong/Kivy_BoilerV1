"""SplashScreen"""
# libs
import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# local imports

# =============================================================================
Builder.load_file(f"{os.getcwd()}\\pages\\splash\\splash_screen.kv")


class SplashScreen(Screen):
    """Splash Page"""
