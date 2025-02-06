import googleapiclient.discovery
import os
import json
import pprint

class YtApi:
    
    def __init__(self):
        self.__api_key = None
        self.video_id = None

    
    def set_api_key(self, key):
        self.__api_key = key

    def get_api_key(self):
        return self.__api_key

    def set_video_id(self, id):

        self.video_id = id

    def fetch_data(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"

        if not self.get_api_key():
            raise ValueError("API key is not set.")

        if not self.video_id:
            print(self.video_id)
            raise ValueError("video_id is not set.")
        
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=self.get_api_key()
            )

        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=self.video_id
        )
        response = request.execute()
        return response
    
