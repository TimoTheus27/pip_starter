import sqlite3

class Database:
    def __init__(self):
        print("2. Initialize the new instance of GUI.")
        # Initiate Graphic User Interface
        # Create a database or connect to existing one
        self.connection = sqlite3.connect('Materialien.db')

    def create_table(self, dataframe):
        # Create a cursor
        c = self.connection.cursor()

        # Commit changes
        self.connection.commit()


# Create delete-Function for Database
def delete():
    # Create a database or connect to existing one
    connection = sqlite3.connect('Materialien.db')
    # Create a cursor
    c = connection.cursor()

    c.execute("DELETE from Materialien WHERE oid= " + delete_box.get())

    # Commit changes
    connection.commit()
    # Close connection
    connection.close()