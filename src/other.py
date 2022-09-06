import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty



Builder.load_string(
    """
<OtherWidget>:
    FloatLayout:
        rows: 1          
        Label: 
            text: "Other things"
            text_size: self.width-20, self.height-20
            valign: 'bottom'
            halign: 'center'
                                  """
)


class OtherWidget(FloatLayout):
    pass

