from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.graphics import Canvas
# custom classes
from view.kheader import HeaderLayout

class setBackground(BoxLayout):
    def __init__(self, **kwargs):
        super(setBackground, self).__init__(**kwargs)


# create wrapper layout of the application
class TheFlash(BoxLayout):
    def __init__(self, **kwargs):
        super(TheFlash, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(setBackground())
        self.add_widget(HeaderLayout())



class TheFlashApp(App):
    def build(self):
        return TheFlash()
    


if __name__ == '__main__':
    TheFlashApp().run()