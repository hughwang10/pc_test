s = '10101100000100001111111000000001'

# print(int(s[:8],2))
result = []
for i in range(0, 32, 8):
    result.append(str(int(s[i:(i+8)], 2)))
print('.'.join(result))

