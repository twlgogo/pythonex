import time

fil = open(r"C:\Users\ttwl\Desktop\123.txt")

nums = []

for line in fil:
    vec = [int(x) for x in line.split()]
    nums += vec

print(time.asctime())


print(nums)

