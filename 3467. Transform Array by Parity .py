nums = [4,3,2,1]
nl = []
for i in nums:
    if i % 2 == 0:
        nl.append(0)
    else:
        nl.append(1)

print(sorted(nl))