"""Login Page"""
# libs
import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
# local imports

# =================================================================
Builder.load_file(f"{os.getcwd()}\\pages\\login\\login_screen.kv")


class LoginScreen(Screen):
    """Login"""
