from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Test(MDApp):
    def build(self):
        return MDLabel(text="Hello Android 15")


Test().run()
