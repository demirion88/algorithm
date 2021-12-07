#영화감독 숌

# n666, 666n
# nn666 n666n 666nn

N = int(input())
lst = [666]
#4자릿수

for j in range(1, 5):
    for i in range(0,10**j):
        A = "666" + str(i)
        B = str(i) + "666"
        lst.append(int(A))
        lst.append(int(B))



for i in range(1,5): # i ~ 1, 2, 3, 4
    for p in range(0,i+1): # p = range(1,1), range(1,2), range(1,3)
        for j in range(0, 10 ** (i-p)): #( 10** 1, 10**2, 10**1, 10**3, 10**4)
            for k in range(0,10 ** (p)): #*10**1, 10**1 , 10**2, 10**1
                #print(i, p,j, k)
                A = str(j) + "666" + str(k).zfill(p)
                lst.append(int(A))

lst1 = list(set(lst))
lst1.sort()
print(lst1[N-1])