# 3190. Find Minimum Operations to Make All Elements Divisible by Three

nums = [1,2,3,4]
output = 0
for i in nums:
    if i % 3 != 0:
        output+=1
    
print(output)