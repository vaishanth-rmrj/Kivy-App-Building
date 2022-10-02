from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class MyApp(MDApp):

    def build(self):
        # adding themes
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "A400"
        # enables dark or light modes
        self.theme_cls.theme_style = "Dark"


        screen = Screen()        
        btn_rectangle = MDRectangleFlatButton( text="Click here",
                            pos_hint= {"center_x": 0.5, "center_y": 0.6})

        screen.add_widget(btn_rectangle)
        return screen

if __name__ == "__main__":
    MyApp().run()