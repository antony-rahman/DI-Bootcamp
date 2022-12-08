import faker
import psycopg2
fake = faker.Faker('pt-PT')

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'first'
DATABASE = 'fake'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()

query = f"""insert into fake_people values
(default, {fake.first_name()}, {fake.last_name()},'{fake.job()}'"""
cursor.execute(query)


connection.commit()
connection.close()






# print(fake.first_name(), fake.last_name())
