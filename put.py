from pymongo import MongoClient
import gridfs

conn = MongoClient()
db = conn.pdf
fs = gridfs.GridFS(db)

with open('python.pdf','rb') as f:
    fs.put(f.read(),filename = 'python.pdf')

conn.close()






















