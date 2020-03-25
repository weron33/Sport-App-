import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.image import Image
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from numpy.random import randint


class Widgets(Widget):
    pass


class StartScreen(Screen):
    #def sprint_buttonO(self):
    pass


class Popups(Popup):
    pass


class MainScreen(Screen):

    iter = ObjectProperty(None)
    dist = ObjectProperty(None)
    

    def start_button(self):
        iter = int(self.iter.text)
        dist = int(self.dist.text)

        while True:
            dist_new = (randint(6) + 1) * 5

            if (dist_new == 5 or dist_new != dist):
                dist = dist_new
                dist_str = str(dist)
                self.dist.text = dist_str
                break

        if iter == 10:
            iter = -1
            self.dist.text = "0"

        iter_str = str(iter + 1)
        self.iter.text = iter_str

    def help_button(self):
        pop = Popups()
        
        pop.open()


class RootScreen(ScreenManager):
    pass


#kv = Builder.load_file("sport.kv")


class SportApp(App):

    def build(self):
        return RootScreen()


if __name__ == "__main__":
    SportApp().run()
