# -*- coding: utf-8 -*-

import pymongo

from source.API import console


class Connection:

    def __init__(self, url='mongodb://localhost:27017', database_name='reciptory') -> None:
        """
        Constructor

        :param url: optional. needed string to find the host
        :param database_name: optional. database name you prefer to use
        """
        try:
            client = pymongo.MongoClient(url)
            # creates database or just connects if already there
            self.db = client.get_database(database_name)
            console.log('Connected to database "' + database_name + '"')

        except (pymongo.errors.OperationFailure, ValueError) as e:
            console.log("Connection failed")
            console.log(e.__str__())
