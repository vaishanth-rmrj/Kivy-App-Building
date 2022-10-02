from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.dialog import MDDialog

kv = Builder.load_file("assets/pop_up.kv")

class MyScreen1(Screen):
    pass

class MyScreen2(Screen):
    # def __init__(self, **kw):
    #     self.username = "None"
    
    def show_username(self):
        # pass
        username = self.ids.username_input.text
        popup_window = MDDialog(text=username,
                            size_hint=(None, None),
                            size=(200, 200))
        popup_window.open()

class MyScreenManager(ScreenManager):
    pass

class MyApp(MDApp):

    def build(self):       
        
        return MyScreenManager()

if __name__ == "__main__":
    MyApp().run()