name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
di = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    w = wds[1]
    add = lst.append(w)



for i in lst:    
    if i in di:
        di[i]=di[i] + 1
    else:
        di[i]=1
        
bc = None
bw = None
for k,v in di.items():
    if bc is None or v > bc:
        bw = k
        bc = v
print(bw, bc)

Hello
this is the feature branch
