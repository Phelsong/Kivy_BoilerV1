"""SplashScreen"""
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# local imports


# =============================================================================
Builder.load_string(
    """
<SplashScreen>:
    FloatLayout:
        rows: 2          
        Label: 
            text: "Welcome to ~Red Moon~"
            text_size: self.width-40, self.height-40
            valign: 'center'
            halign: 'center'
            background: "blue"
        Button:
            text: "Login"
            text_size: self.width-40, self.height-40
            valign: 'center'
            halign: 'center'
            background: "grey"
            on_release: root.manager.current = 'LoginScreen'
                                  """
)


class SplashScreen(Screen):
    pass
