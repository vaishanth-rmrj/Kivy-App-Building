from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

kv = Builder.load_file("assets/grid_layout.kv")

class MyScreen(Screen):
    pass

class MyApp(MDApp):

    def build(self):       
        
        return MyScreen()

if __name__ == "__main__":
    MyApp().run()