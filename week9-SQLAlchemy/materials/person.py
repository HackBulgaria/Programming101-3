import inspect

def map_python_type_to_sql_type(value):
    types = {
        int: "INTEGER",
        str: "TEXT"
    }
    
    value_type = type(value)
    
    if value_type in types:
        return types[value_type]


def map_class_to_table(cls):
    members = inspect.getmembers(cls, lambda a:not(inspect.isroutine(a)))

    members = [m for m in members if not "__" in m[0]]

    create_sql = """
        CREATE TABLE {}(
    {})
    """.strip()
    
    columns = []
    
    columns.append("""
    {} INTEGER PRIMARY KEY
    """.format("{}_id".format(cls.__name__.lower())).strip())

    for member in members:
        column_name = member[0]
        column_type = map_python_type_to_sql_type(member[1])

        columns.append("""
    {} {}
        """.format(column_name, column_type).strip())
    
    columns = ",\n".join(columns)

    create_sql = create_sql.format(cls.__name__, columns)
    print(create_sql)


class Person:
    name = ""
    age = 0

map_class_to_table(Person)
