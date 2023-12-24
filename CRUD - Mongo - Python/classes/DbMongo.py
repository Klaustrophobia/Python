"""
This class takes the role of connect with the DataBase of MongoDB 
"""
import pymongo
import os

class MongoDB():
    
    @staticmethod
    def getDB():
        ## GRAB THE INFORMATION
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'

        ##  MongoDB connection string 
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )

        ## Create a MongoClient object using the constructed connection string.
        client = pymongo.MongoClient(uri)
        ## Access the MongoDB database specified by the value of the 'DB' environment variable.
        db = client[os.environ['DB']]

        return client, db

