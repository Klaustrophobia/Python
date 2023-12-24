class Career:

    def __init__(self, description, id):
        self.description = description
        
        ## Private instance variables
        self.__id = id
        self.__collection = "career"

    def save(self, db):
        ## Access the MongoDB collection specified by the __collection attribute.
        collection = db[self.__collection]
        ## Insert a document into the collection using the object's attributes
        result = collection.insert_one(self.__dict__)
        ## Update the private __id attribute with the inserted document's ID, obtained from the inserted_id attribute of the result.
        self.__id = result.inserted_id

    @staticmethod

    def return_list(db):
        collection = db["Careers"]

        list_career = []
        for d in collection.find():
            career = Career(d['descripcion'], d["_id"])
            list_career.append(career)       

        return list_career
