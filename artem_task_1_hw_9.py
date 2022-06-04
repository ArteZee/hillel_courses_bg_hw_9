import datetime

# Mlist of products which must be sorted
list_of_products = [("banana", 4), ("egg", 11), ("milk", 1), ("pencil", 33), ("notebook", 22)]

# sorted our list with key in value lambda
list_of_products.sort(key=lambda x: x[1])

print(list_of_products)

random_dict_1 = {"artem": 22,
                 "Maria": 13,
                 "Huan": 0
                 }
random_dict_2 = {"": 11, "Maria": 13, "Huan": 31}

# all get True if all key is True or False if key empty or False
print("random dict 1 result with all ", all(random_dict_1), "\nrandom dict 2 result with all", all(random_dict_2))

# in dict_2  with any we got True bc anny get True if any key is true (in dict)
print("\nrandom dict 1 result with any ", any(random_dict_1), "\nrandom dict 2 result with any", any(random_dict_2))

#  zip function get union of iterable objects
season = ["winter", "spring", "summer", "autumn"]
digits = [1, 2, 3, 4]

union_list = list(zip(season, digits))
print(union_list)
# example of filter()
print(datetime.datetime.now().year)
list_user = [("Artem", 2000), ("Anna", 1999), ("Kirill", 2005), ("Vadim", 2010)]


# filter ()
def people(adult: list):
    """
    Example of filter()
    :param adult:
    :return: list of user that rich 18 years old
    """
    return list(filter(lambda x: datetime.datetime.now().year - x[1] >= 18, adult))


print(people(list_user))
numbers = range(0, 100)

# example of map
even_numbers = list(map(lambda x: x ** 1 / 2, numbers))
print(even_numbers)
