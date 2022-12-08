import psycopg2
import re 

HOSTNAME = 'localhost'
USERNAME = 'yussiroz'
PASSWORD = 'cluster'
DATABASE = 'users'


def run_query(query):
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


def insert_q(*new_values):
    """partial query for specifying values as with parentheses (varchar etc.)
       or without parentheses (int etc.)
        params:
            new_values: tuple (value1, value2...)
        returns: str -> '(value1 [int], value2 [varchar]...)'
    """
    q = '('
    for new_value in new_values:
        if not new_value.isdigit() or new_value.isalpha():
            q += f"""'{new_value}',"""
            continue

        q += f'{new_value},'

    return q[:-1] + ')'


def create_table_query(table_name, **fields_names_types):
    """query for creating table
        params:
            table_name: str (new table)
            fields_names_types: dict (new fields and value types)
        returns: str -> ('ALTER TABLE table_name ')
    """
    q = f'Create table {table_name} ('
    for field_name, field_type in fields_names_types.items():
        q += f'{field_name} {field_type},'

    return q[:-1] + ')'


def delete_query(table_name, *indexes):
    """query for deleting values in table with index
        params:
            table_name: str
            indexes: tuple (indexes to remove)
        returns: str -> 'DELETE FROM table_name id in (idx1, idx2..)'
    """   
    q = f"DELETE FROM {table_name} WHERE id in ("
    for idx in indexes:
        q += f'{idx},'

    return q[:-1] + ');'


def insert_query(table_name, **fields_vals):
    """partial query of altering table
        params:
            table_name: str
            fields_vals: dict (fields and new value pairs)
        returns: str -> ('INSERT INTO TABLE table_name (field1, field2..) 
                                 VALUES (value1, value2...)')
    """   
    q = f"INSERT INTO {table_name} "
    field_names = list(list(fields_vals.keys()))
    values = list(fields_vals.values())

    # partial query: '(field1, field2, field3...)'
    q += f'({",".join(field_names)}) '
    # partial query: '(value1, value2, value3...)'
    q += f'VALUES {insert_q(*values)} '
    # partial query: 'RETURNING field1, field2, field3...;'
    q += f'RETURNING {",".join(field_names)};'

    return q


def alter_table(table_name):
    """partial query of altering table
        params:
            table_name: str
        returns: str -> ('ALTER TABLE table_name ')
    """
    return f'ALTER TABLE {table_name} '
    
def add_contraint_query(table_name, constaint_name):
    """query for adding a new constraint to database
        params:
            table_name: str
            constraint_name: str (new constraint)
        returns: str
        
        addons:
            alter_table(): str
    """
    return alter_table(table_name) + f'ADD CONSTRAINT {constaint_name} '


def remove_constraint_query(table_name, constaint_name):
    """query for removing a constraint from database
        params:
            table_name: str
            constraint_name: str (old constraint)
        returns: str
        
        addons:
            alter_table(): str
    """
    return alter_table(table_name) + f'DROP CONSTRAINT {constaint_name} '


def add_foreign_key(table_name, other_table_name, foreign_key, other_table_field):
    """query for adding a new field to database
        params:
            table_name: str
            other_table_name: str 
            foreign_key: str (foreign key in table)
            other_table_field: str (the field in other to connect foreign_key to)
        returns: str

        addons:
            alter_table(): str
    """
    constraint_q = add_contraint_query(table_name, f'{foreign_key}_fk')
    q = f'FOREIGN KEY ({foreign_key}) REFERENCES {other_table_name}({other_table_field});'
    return constraint_q + q


def add_field(table_name, field_name, field_type):
    """query for adding a new field to database
        params:
            table_name: str
            field_name: str 
            field_type: str (int/varchar/text)
        returns: str

        addons:
            alter_table(): str
    """
    return alter_table(table_name) + f'ADD COLUMN {field_name} {field_type} '


def drop_column(table_name, field_name):
    """query for dropping a specified column from database
        params:
            table_name: str
            field_name: str
        returns: str

        addons:
            alter_table(): str
    """
    return alter_table(table_name) + f'DROP COLUMN {field_name} '


def select_records(table_name, *fields, limit = None):
    q = f'SELECT '
    if fields:
        fields = ','.join(list(fields))
        q += f'{fields} FROM {table_name} '
    else:
        q += f'* FROM {table_name} '
    if limit: 
        q += f'LIMIT {limit}'
    return q


def menu():
    menu = """Hello mortal! you are no connected to the <users> database!
    [1] To select all records
    [2] To insert records
    [3] To delete records
    [0] To EXIT"""
    return menu

def handle_kwargs(kwargs_str):
    is_int = lambda x: int(x) if x.isnumeric() else x
    d = dict(map(is_int,x.split("=")) for x in kwargs_str.split(","))
    return d

if __name__ == '__main__':

    while True:

        choice = input(menu())

        if choice == '0':
            break

        if choice == '1':
            q = select_records('user_passwords')
            res = run_query(q)
            print(res, '\n')

        elif choice == '2':
            table_name = input('Table name to insert records: ')
            fields_vals = input('Comma separated field = new value: ')
            kwargs = handle_kwargs(fields_vals)
            q = insert_query(table_name, **kwargs)
            run_query(q)           

            
        elif choice == '3':
            pass
        else:
            print("####Invalid input####")