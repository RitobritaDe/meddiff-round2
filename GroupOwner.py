num = input()
inputDict = {}
for _ in range(int(num)):
    A, B = input().split()
    inputDict[A] = B
print(inputDict)

res = {}
for i, v in inputDict.items():
    res[v] = [i] if v not in res.keys() else res[v] + [i]
print(res)