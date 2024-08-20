# 1672. Richest Customer Wealth
arr = []
accounts = [[1,2,3],[3,2,1]]
for i in range(len(accounts)):
    total = 0
    for j in accounts[i]:
        total = total+j
    arr.append(total)
print(max(arr))


# accounts = [[1,2,3],[3,2,1]]
# wealth = [sum(account) for account in accounts]
# print(max(wealth))