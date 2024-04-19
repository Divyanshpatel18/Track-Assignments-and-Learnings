from pymongo import MongoClient

def get_db():
        # Connection URI
        uri = "mongodb+srv://divyanshpatel0011:MongoDB123@cluster0.hwoam27.mongodb.net/"
        # Create a MongoClient
        client = MongoClient(uri)
        # Access the database
        db = client["FastAPI"]
        return db 


