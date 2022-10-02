from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField

class MyApp(MDApp):

    def build(self):
        # adding themes
        text_field = MDTextField(text="Username",
                                pos_hint= {"center_x": 0.5, "center_y": 0.5},
                                size_hint_x = None,
                                width=300,
                                helper_text="Enetr your username",
                                helper_text_mode="persistent",
                                icon_right="android")


        screen = Screen()        
        btn_rectangle = MDRectangleFlatButton( text="Submit",
                                                pos_hint= {"center_x": 0.5, "center_y": 0.4})

        screen.add_widget(btn_rectangle)
        screen.add_widget(text_field)
        return screen

if __name__ == "__main__":
    MyApp().run()