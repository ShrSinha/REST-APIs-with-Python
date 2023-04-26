# On Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
from typing import Iterable
from typing import Callable
from operator import itemgetter


def search(sequence: Iterable[dict[str, str | int]], expected: str, finder: Callable[[dict[str, str]], str]):
   for e in sequence:
       if finder(e) == expected:
           return e
   raise RuntimeError(f"Couldn't find an element with {expected}")       


Friend = dict[str, str | int]
friends: list[Friend] = [
   {'name': 'R', 'age': 10},
   {'name': 'S', 'age': 20},
   {'name': 'N', 'age': 30}
]

def get_friend_name(friend: dict[str, str]) -> str:
   return friend['name']


print(search(friends, 'V', get_friend_name))
#print(search(friends, 'R', lambda friend: friend['name']))
#print(search(friends, 'R', itemgetter('name'))) # itemgetter is a function that creates other functions


# import functools

# def make_secure(func): # make_secure = decorator
#     @functools.wrap(func)
#     def secure_function(): #secure_function replaces get_admin_password
#         if user["access_level"] == "admin":
#             return func()
#         else:
#             return f"No admin permissions for user {user['username']}."    

#     return secure_function #return function itself        

# @make_secure
# def get_admin_password() -> str: # want to secure this function when called
#     return "1234"



# user = {"username": "jose", "access_level": "guest"}
# print(get_admin_password())
