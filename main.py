from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class App(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.material_style = "M3"

        screen_manager = ScreenManager()
        screen_manager.add_widget(
            Builder.load_file("Kv_ui/user_application.kv")
        )

        return screen_manager


if __name__ == "__main__":
    App().run()
