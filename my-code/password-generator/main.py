import random
passlen = int(input("enter the length of password: "))
# uses these chars as sample base
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# creates random sample using s and user input "passlen" as arguments for join function
p = "".join(random.sample(s,passlen ))
print(p)