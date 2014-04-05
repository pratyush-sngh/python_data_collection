from pymongo import MongoClient
client =MongoClient('localhost',27017)
db=client.bitphi
# collection= db.tweets
words= {"word":post}
words=db.tweets
post_id=words.insert(word)
