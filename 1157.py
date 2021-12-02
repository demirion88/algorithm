strl = (str(input())).upper()
dic = {}
dicl = []
for i in strl:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
maxval = max(dic.values())
for k, v in dic.items():
    if v == maxval:
        dicl.append(k)
if len(dicl) >= 2:
    print("?")
else:
    print(dicl[0])

