import json

class Database:

    def save_data(self, data):
        with open("ytCommentData.json", "w") as f:
            json.dump(data, f, indent=4)

