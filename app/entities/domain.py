from entities import Collection


class Domain():

    @classmethod
    def createCollection(cls, data):
        collection = Collection(cls, data)
        return collection
