import time

t1 = time.time()
nums = range(10000000)
sum = 0
for k in nums:
    sum = sum + k
print(f"Sum of {len(nums)} numbers is : {sum}")
t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
