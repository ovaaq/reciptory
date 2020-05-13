import pymongo


class Connection:

    def __init__(self, url='mongodb://localhost:27017', database_name='reciptory'):
        """Constructor

        Keyword arguments:
        url -- optional. needed string to find the host
        database_name -- optional. database name you prefer to use
        """
        try:
            client = pymongo.MongoClient(url)
            # creates database or just connects if already there
            self.db = client.get_database(database_name)
            print('Connected to database "' + database_name + '"')

        except (pymongo.errors.OperationFailure, ValueError):
            print("Connection failed")
