from slistener import SListener
import time, tweepy, sys
from pymongo import MongoClient
client =MongoClient('localhost',27017)
db=client.bitphi
## authentication
auth = tweepy.OAuthHandler('', '') 
auth.set_access_token('', '')
api = tweepy.API(auth)

def main():
    #   words.extend(db.words)
    track = [] array of words you want to keep track of
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        print "yoyoyoyyoyoyo"
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
