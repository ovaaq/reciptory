import pymongo
from bson import ObjectId


class Connection:

    def __init__(self, host='localhost', port='27017', user='', password='', database_name='reciptory'):
        """Constructor

        Keyword arguments:
        host -- used host for the database connection
        port -- used port for the database connection
        user -- optional. user for the database connection
        password -- optional user password for the database connection
        """
        if len(password) > 0 and len(user) > 0:
            url = "mongodb://%s:%s@%s:%s" % (user, password, host, port)
        else:
            url = "mongodb://%s:%s" % (host, port)

        try:
            client = pymongo.MongoClient(url)
            print("Connected to " + url)

            # creates database or just connects if already there
            self.db = client.get_database(database_name)

        except:
            print("Connection failed")
