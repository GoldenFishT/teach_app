import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

screen_names = ['home', 'note', 'explore']

class MainScreen(BoxLayout):
    pass

class MainScreenManager(ScreenManager):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='home screen'))

class NoteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='note screen'))


class ExploreScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='explore screen'))


class TeachingApp(App):
    def build(self):
        return MainScreen()

    def go_to_screen(self, name='home', *args):
        self.root.ids.lessons_lst.current = name
    
if __name__ == '__main__':
    TeachingApp().run()
