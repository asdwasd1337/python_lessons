f=open('travels.txt','r')

dates = []
m = []


for s in file:
    s = s.strip()
    ch = s.split()

    data = ch[0]
    massa = int(ch[5])

    dates.append(data)
    m.append(massa)

    rdates = []

for i in range(len(dates)):




