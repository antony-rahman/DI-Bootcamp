import psycopg2
import pandas as pd
import pandas.io.sql as psql

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'first'
DATABASE = 'W6D5'


class MenuItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def run_query(query):
        """opens connection, runs a query, closes the connection"""
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()


    def save(self) -> str:
        """Create a query that inserts values into the table"""
        q = f"insert into menu values ('{self.name}', {self.price})"

        MenuItem.run_query(q)
        return q


    def delete(self) -> str:
        """Create a query that deletes a row from the table"""
        q = f"delete from menu where dish_name = '{self.name}' or price = {self.price}"
        
        MenuItem.run_query(q)
        return q


    def update(self, name: str, price: float) -> str:
        """Create a query that updates a row in the table"""
        q = f"update menu set dish_name = '{name}', price = {price} where dish_name = '{self.name}' or price = {self.price}"

        MenuItem.run_query(q)
        print(f"You updated the entry to {name} for {price}NIS")
        
        return q

    @classmethod
    def all() -> str:
        """Create a query that selects all rows in the table"""

        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        menu = pd.read_sql('select dish_name, price from menu', connection)
        print(menu)


    def get_by_name(name) -> str:
        """Creates a query that selects a row by 'name' column from the table"""
        q = f"select * from menu where dish_name = '{name}'"

        print(MenuItem.run_query(q))
        return q




item = MenuItem('Burger', 35)

# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
# items = MenuItem.all()


