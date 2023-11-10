import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special = "!@#$%^&*(){}[]?<>,.;':"
all = lower + upper + numbers + special
length = 7
password = "".join(random.sample(all,length))
print(password)