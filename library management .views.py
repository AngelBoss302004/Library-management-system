import mysql.connector


class library:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Angel@1234",
                database="library_db"
            )

            if self.connection.is_connected():
                print("Database connected successfully!")

        except Exception as e:
            print(e)
            self.connection = None



    def post(self, name, author, price, quantity):
        try:
            self.cursor = self.connection.cursor()

            query = """
            INSERT INTO books (name, author, price, quantity)
            VALUES (%s, %s, %s, %s)
            """

            values = (name, author, price, quantity)

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Book inserted successfully!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()



    def get(self):
        try:
            self.cursor = self.connection.cursor()

            self.cursor.execute("SELECT * FROM books")

            result = self.cursor.fetchall()

            for row in result:
                print(row)

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()



    def get_object(self, id):
        try:
            self.cursor = self.connection.cursor()

            query = "SELECT * FROM books WHERE id=%s"

            self.cursor.execute(query, (id,))

            result = self.cursor.fetchone()

            if result:
                print(result)
            else:
                print("Book not found!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()



    def put(self, id, name, author, price, quantity):
        try:
            self.cursor = self.connection.cursor()

            query = """
            UPDATE books
            SET name=%s, author=%s, price=%s, quantity=%s
            WHERE id=%s
            """

            values = (name, author, price, quantity, id)

            self.cursor.execute(query, values)
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print("Book updated successfully!")
            else:
                print("Book not found or no changes made!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()



    def delete(self, id):
        try:
            self.cursor = self.connection.cursor()

            query = "DELETE FROM books WHERE id=%s"

            self.cursor.execute(query, (id,))
            self.connection.commit()

            if self.cursor.rowcount > 0:
                print("Book deleted successfully!")
            else:
                print("Book not found!")

        except Exception as e:
            print(e)

        finally:
            if hasattr(self, "cursor"):
                self.cursor.close()



    def close(self):
        try:
            if (self.connection is not None
                    and self.connection.is_connected()):

                self.connection.close()
                print("Database connection closed!")

        except Exception as e:
            print(e)


obj1 = library()

if obj1.connection is not None:
    obj1.post(
        name="Python Programming",
        author="John",
        price=450,
        quantity=10
    )
    obj1.get()
    obj1.get_object(1)
    obj1.put(
        id=1,
        name="Advanced Python",
        author="John",
        price=550,
        quantity=15
    )
     #obj1.delete(1)
    obj1.close()