import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from .src.other import OtherWidget

Builder.load_string(
    """
<SplashPage>:
    FloatLayout:
        rows: 1          
        Label: 
            text: "Welcome to ~Red Moon~"
            text_size: self.width-20, self.height-20
            valign: 'center'
            halign: 'center'
            background: "blue"
                                  """
)


class SplashPage(FloatLayout):
    pass


class Red_Moon(App):
    def build(self):
        # return OtherWidget()
        return SplashPage()


if __name__ == "__main__":
    Red_Moon().run()


# EXAMPLE
# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)
