import json
import os
import configparser

class Database:

    def save_cfg_data(self, data, fname):
        config = configparser.RawConfigParser()
        config.add_section('main')
        for item in data:
            config.set('main', item, data[item])

        with open(f'{fname}.cfg', "w") as f:
            config.write(f)

    def save_json_data(self, data, fname):
        with open(f"{fname}.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_filter_data(self): #
        '''
        To get comments only
        '''
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

    def get_cfg_data(self, fname):
        config = configparser.RawConfigParser()
        config.read(f'{fname}.cfg')
        return dict(config.items("main"))