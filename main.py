from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock
from kivymd.app import MDApp
from Metadata import Youtube

class App(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.material_style = "M3"
        screen_manager = ScreenManager()
        screen_manager.add_widget(
            Builder.load_file("Kv_ui/user_application.kv")
        )
        self.yt = Youtube()
        return screen_manager

  
    def on_start(self):
        self.app_folder = self.user_data_dir

    def downloader(self,url):
         self.yt.get_metadata(url, self.on_result)
         
    def on_result(self, data):
     Clock.schedule_once(lambda dt: self.Data(data))
     
     
    def Data(self,data):
        screen = self.root.get_screen("main")
        ids =  screen.ids
        ids.channel_name.text = f"[+] channel_name: {data.get('channel_name', '')}"
        ids.uploader.text = f"[+] uploader: {data.get('uploader', '')}"
        ids.channel_is_verified.text = f"[+] channel_is_verified: {data.get('channel_is_verified', '')}"
        ids.viecount.text = f"[+] viewcount: {data.get('view_count', '')}"
        ids.likes.text = f"[+] likes: {data.get('likes', '')}"
        ids.duration.text = f"[+] duration: {data.get('duration', '')}"
        ids.display_id.text = f"[+] display_id: {data.get('display_id', '')}"
        ids.upload_date.text = f"[+] upload_date: {data.get('upload_date', '')}"
        ids.channel_follower_count.text = (f"[+] channel_follower_count: {data.get('channel_follower_count', '')}")

    def Save_data(self):
       self.yt.save_metadata(self.app_folder)
       dialog = MDDialog(
             title="Debug",
             text=self.app_folder,
             radius=[60,60,60,60],
             buttons =
             [MDFlatButton(text='Cancel',on_release= lambda x : dialog.dismiss())])           
       dialog.open()
                                 
    def clear_field(self,field):
         field.text = ""
         

if __name__ == "__main__":
    App().run()
