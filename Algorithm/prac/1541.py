susik = input()
arr = susik.split('-')

res = sum(map(int, arr[0].split('+')))
for i in range(1, len(arr)):
    res -= sum(map(int, arr[i].split('+')))
print(res)