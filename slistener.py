from tweepy import StreamListener
import json, time, sys
from pymongo import MongoClient
client =MongoClient('localhost',27017)
db=client.bitphi
class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix

    def on_data(self, data):

        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return false

    def on_status(self, status):
        posts=db.tweet
        # post_id=posts.insert(status)
        status_json= json.loads(status)
        language=status_json.get("user",{}).get("lang",{})
        if  language == "en":
            post= {"created at" : status_json.get("created_at",{}),
                "text": status_json.get("text",{}),
                "name": status_json.get("user",{}).get("name",{}),
                "screen_name": status_json.get("user",{}).get("screen_name",{}),
                "follower_count":status_json.get("user",{}).get("followers_count",{})
                }
            post_id=posts.insert(post)    
        # print status_json
        return

    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "\n")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 
