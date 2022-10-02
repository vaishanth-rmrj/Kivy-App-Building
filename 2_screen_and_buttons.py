from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class MyApp(MDApp):

    def build(self):
        screen = Screen()
        btn_flat = MDFlatButton( text="Click here",
                            pos_hint= {"center_x": 0.5, "center_y": 0.7})
        
        btn_rectangle = MDRectangleFlatButton( text="Click here",
                            pos_hint= {"center_x": 0.5, "center_y": 0.6})

        btn_icon = MDIconButton(icon="language-python",
                                pos_hint= {"center_x": 0.5, "center_y": 0.5})

        btn_floating_action = MDFloatingActionButton(icon="language-python",
                                pos_hint= {"center_x": 0.5, "center_y": 0.4})

        screen.add_widget(btn_flat)
        screen.add_widget(btn_rectangle)
        screen.add_widget(btn_icon)
        screen.add_widget(btn_floating_action)
        return screen

if __name__ == "__main__":
    MyApp().run()