# lst = [1,2,3,4,5]
# my_str = "Hello, World!"
# my_int = 42
# print(type(lst))
# print(type(my_str))
# print(type(my_int))
# print(type(type(my_int)))

from oops_proj import Chatbook  
#user1 = Chatbook()

# lst = [1, 2, 3, 4, 5]

# #function
# l = len(lst)
# print(l)

# #method
# user1.send_msg()

# #getter and setter methods
# print(user1.get_name())
# user1.set_name( "John Doe")
# print(user1.get_name())

user1 = Chatbook()
print(user1.id)
# user2 = Chatbook()
# print(user2.id)
# user3 = Chatbook()
# print(user3.id)

Chatbook.set_id(100)
user2 = Chatbook()
print(user2.id)




