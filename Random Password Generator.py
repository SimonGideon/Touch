import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all = lower + digits + symbols
length = 16
password = "".join(random.sample(all, length))
print(password)