from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

kv = Builder.load_file("assets/screen_manager.kv")

class MyScreen1(Screen):
    pass

class MyScreen2(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(MDApp):

    def build(self):       
        
        return MyScreenManager()

if __name__ == "__main__":
    MyApp().run()