import time

t1 = time.time()
nums = range(1000000)
sum = 0
for k in nums:
    sum = sum + k
print("Sum of 100,000,000 numbers is : ", sum)
t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")