from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from matplotlib.pyplot import text

class MyApp(MDApp):

    def build(self):
        label = MDLabel( text="Hey there !!!",
                         halign="center",
                         theme_text_color="Custom",
                         text_color=(236/ 255.0, 98/ 255.0, 1/255.0, 1),
                         font_style="Caption")
        icon = MDIcon(icon="language-python", halign="center")
        return icon

if __name__ == "__main__":
    MyApp().run()