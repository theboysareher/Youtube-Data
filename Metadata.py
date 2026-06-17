from yt_dlp import YoutubeDL
import json
from uuid import uuid4
from threading import Thread,Event
import traceback

class Youtube():
    def __init__(self):
        self.data = {}
        self.event = Event()
        
    def get_metadata(self,url:str,callback):
        self.thread = Thread(target=self._get,args=(url,callback))
        self.thread.start()
        
    def save_metadata(self):
        self.event.wait()
        Thread(target=self._save).start()
           
    def _get(self,url:str,callback) -> str:
       options = {"skip_download": True,"quiet":True,"no_warnings": True}    
       with YoutubeDL(options) as ydl:
           try:
             info = ydl.extract_info(url, download=False)
             data = {
                "channel_name":info.get('channel',""),
                "uploader": info.get('uploader_id',""),
                "uploader_url":info.get('uploader_url',""),
                "view_count":info.get('view_count',""),
                "likes":info.get('like_count',""), 
                "duration":f"{info.get('duration',"")}s",
                "display_id":info.get('display_id',""),
                "upload_date":(
                        info['upload_date'][:4] + "/" +
                        info['upload_date'][4:6] + "/" +
                        info['upload_date'][6:]),
               "channel_follower_count":info.get('channel_follower_count',""),
               "channel_is_verified": info.get('channel_is_verified', False)}
                
              
             self.data = data
             callback(data)
             self.event.set()                   
           except Exception as e: traceback.print_exc();self.event.set()
           
           
    def _save(self) -> None:
        try:
           with open(f"{self.data['uploader']}-{uuid4().hex[:5]}.json","w") as f:
               json.dump(self.data,f,indent=4)
        except Exception as e :
           traceback.print_exc()
           quit()
           
              
      
