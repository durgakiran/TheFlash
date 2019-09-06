from kivy.uix.actionbar import (ActionBar, ActionView, ActionPrevious, ActionGroup, ActionButton, ActionItem)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class CreateDeck(ActionButton):
    def __init__(self, **kwargs):
        super(CreateDeck, self).__init__(**kwargs)
        self.text = "Deck +"


class ButtonGroup(ActionGroup):
    def __init__(self, **kwargs):
        super(ButtonGroup, self).__init__(**kwargs)
        self.text = "options"
        self.add_widget(CreateDeck()) 



class HeaderTitle(ActionPrevious):
    def __init__(self, **kwargs):
        super(HeaderTitle, self).__init__(**kwargs)
        self.with_previous = False
        self.app_icon = ''
        self.title = 'The Flash'




class Header(ActionView):
    def __init__(self, **kwargs):
        super(Header, self).__init__(**kwargs)
        self.add_widget(HeaderTitle())
        self.add_widget(ButtonGroup())

class HeaderWrapper(ActionBar):
    def __init__(self, **kwargs):
        super(HeaderWrapper, self).__init__(**kwargs)
        self.background_color = [0, 1, 0.5, 1]
        self.add_widget(Header())

class HeaderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(HeaderLayout, self).__init__(**kwargs)
        self.height = 50
        self.add_widget(HeaderWrapper())
        