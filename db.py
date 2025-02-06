import json
import os

class Database:

    def save_data(self, data):
        with open("ytCommentsData.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_filter_data(self): #To get comments only
        try:
            with open("ytComments.json", "r") as fcmnts: 
                comments = json.load(fcmnts)
                return comments
        
        except:
            if os.path.exists("ytCommentsData.json"):
                with open("ytCommentsData.json", "r") as f:
                    ytContent = json.load(f)
                    print(len(ytContent["items"]))
                    comments = { 
                        "inputs": [
                            item["snippet"]["topLevelComment"]["snippet"]["textOriginal"] 
                            for item in ytContent["items"]
                        ]
                    }
                    return comments

            else:
                print("Error: Cannot filter ytCommentsData.")
                return -1
        