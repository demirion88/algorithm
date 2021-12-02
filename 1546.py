lstcnt = int(input())
lst = list(map(int, input().split()))
max_list = max(lst)

for i in range(0, lstcnt):
    lst[i] = lst[i]/max_list * 100
    ret = sum(lst) / len(lst)

print(ret)



