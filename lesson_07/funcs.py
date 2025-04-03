from datetime import datetime


# def print_my_name() -> None:
#     """
#     the function that prints my name
#     """
#     name: str = "Bohdan"
#     print(name)
#
# print_my_name()

# -----------------

def return_my_name() -> str:
    """
    the function that prints my name
    """
    name: str = "Bohdan"
    return name


result = return_my_name()
print(result)


# -----------------------------

def print_name(name: str) -> None:
    print(name)

print_name("Vasyl")


def return_name(name: str) -> str:
    return name.title()

result = return_name("mykola")
print(result)


def greeting_person(name: str, age: int, profession: str, is_married: bool) -> str:
    return f"Hello, my {name}! My age is {age} years old and profession is {profession}. I am {"married" if is_married else "not married"}."

result = greeting_person("Vasyl", 25, "Test Automation Engineer", False)
# result = greeting_person(25, "Vasyl", "Test Automation Engineer", False)

print(result)

# --------------------------------------------------------------

def greeting_person(name: str, age: int, profession: str, is_married: bool = False, sex: str = "male") -> str:
    """
    Returning greeting string of a person
    :param name: name of a person
    :param age: age of a person
    :param profession: pr`
    :param is_married: if person is married
    :param sex: sex of person
    :return: a greeting string
    """
    return f"Hello, my {name}! My age is {age} years old and profession is {profession}. I am {"married" if is_married else "not married"}. I am {sex}"

result = greeting_person("Vasyl", 25, "Test Automation Engineer", is_married=True)
result_2 = greeting_person(name="Vasyl", age=25, profession="Test Automation Engineer", is_married=False)

print(result)


# ----------------------------------------------

def return_list_of_names(*args , is_married: bool =True, have_job_now: bool = None) -> None:
    # args - tuple
    print(args, type(args))
    for name in args:
        print(name, is_married, have_job_now)

# result = return_list_of_names("Bohdan", "Denys", "Kyrylo", is_married=False)

list_of_users: list[str] = ["Bohdan", "Denys", "Kyrylo"]

result_lists = return_list_of_names(*list_of_users)
print(result_lists)

# ----------------------------------------------

def return_sql_query(table_name: str, id: int, column = None):
    sql = f"SELECT {column} FROM {table_name} WHERE id={id}"
    return sql


result = return_sql_query("users", 777, "status")
print(result)

# ----------------------------------------------

def return_sql_query(table_name: str, id: int, **kwargs):
    # conditions - dict
    print(kwargs, type(kwargs))
    sql = f"SELECT * FROM {table_name} WHERE id={id}"
    if kwargs:
        for key, value in kwargs.items():
            sql += f" AND {key}={value}"
    return sql


result = return_sql_query("users", 777, status="active", isactive=False, isdeleted=False, created_date=str(datetime.now()))
print(result)

# -------------------------------------

def elements_list(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


elements_list(55, 0, 22.4, -11, color="red", size="small")

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dict_of_conditions = {"color": "red",
                      "size": "small",
                      "is_active": True}


elements_list(*list_of_numbers, **dict_of_conditions)

# first, *second = dict_of_conditions
# print(first, second)






