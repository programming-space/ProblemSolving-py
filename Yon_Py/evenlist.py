n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if arr[j] == arr[i]:
            new_arr = []
            for k in range(i,j+1):
                new_arr.append(arr[k])
try:
    if len(new_arr) % 2 == 0:
        print(new_arr)
except:
    print("-1")