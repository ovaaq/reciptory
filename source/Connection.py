import pymongo


class Connection:

    def __init__(self, host='localhost', port='27017', user='', password='', database_name='reciptory'):
        """Constructor

        Keyword arguments:
        host -- used host for the database connection
        port -- used port for the database connection
        user -- optional. user for the database connection
        password -- optional. user password for the database connection
        database_name -- optional. database name you prefer to use
        """
        if len(password) > 0 and len(user) > 0:
            url = "mongodb+srv://%s:%s@%s" % (user, password, host)
        else:
            url = "mongodb+srv://%s" % (host, port)

        if len(port) > 0:
            url = url + ':' + port

        try:
            client = pymongo.MongoClient(url)

            # creates database or just connects if already there
            self.db = client.get_database(database_name)
            print(client.list_database_names())

        except (pymongo.errors.OperationFailure, ValueError):
            print("Connection failed")
