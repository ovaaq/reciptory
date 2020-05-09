from source.connection import Connection

#testing the instance of Connection class
c = Connection()
print(c.db)

print(c.add_ingredient(None, [1,2,3],[0,0,0,0,0,0,0,0]))