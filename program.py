import re
f = open('friends.txt')
a = []
b = []
for line in f:
    b = line.split(' ')
    for x in b:
        d = x.find('<b>')
#        if d !=-1:
#            print x, d
#            print x[d:]
        e = x.find('</b>')
        if (d != -1) and (e != -1):
#            print x[(d+3):(e-1)]
            p = x[(d+3):(e-1)]
            p = re.sub('<.*?>', '', p)
            if p != '':
                p = p[0] + p[1:].lower()
                a.append(p)
        else:
            c = x.find(':')
            if c != -1:
                p = x[:c]
                p = re.sub('<.*?>', '', p)
                if len(p) >1:
                    p = p[0] + p[1:].lower()
#                    print p
                    a.append(p)
    b = []
#for string in a:
#    string = re.sub('<.*?>', '', string)
f.close()
#print a
for x in a:
    if (x.find('html') != -1) or (x.find('href') != -1) or (x.find('content') != -1) or (x.find('=') != -1):
        a.remove(x)
#print len(a)
u = []
for x in range(len(a)):
    if (a[x] in u) == False:
        u.append(a[x])
#print u
rmpjcr = [0,0,0,0,0,0]
for x in a:
    if x == 'Rachel':
        rmpjcr[0]+=1
    elif x == 'Monica':
        rmpjcr[1]+=1
    elif x == 'Phoebe':
        rmpjcr[2]+=1
    elif x == 'Joey':
        rmpjcr[3]+=1
    elif x == 'Chandler':
        rmpjcr[4]+=1
    elif x == 'Ross':
        rmpjcr[5]+=1
    
print 'Rachel ' + str(rmpjcr[0]) + ' Monica ' + str(rmpjcr[1]) + ' Phoebe ' + str(rmpjcr[2]) + '\nJoey ' + str(rmpjcr[3]) + \
' Chandler ' + str(rmpjcr[4]) + ' Ross ' + str(rmpjcr[5])
        
f = open('nodes.csv', 'w')
f.write("Label\n")
for x in range (len(u)):
    f.write(u[x] + '\n')
f.close()   
f = open('1.csv', 'w')
g = open('2.csv', 'w')
f.write('Source\n')
g.write('Target\n')
for x in range (len(a)):
    if x != 0:
        if (a[x].find('scene') == -1) and (a[x-1].find('scene') == -1) and (a[x].find('=') == -1) and (a[x-1].find('=') == -1):
            f.write(a[x-1]+'\n')
            g.write(a[x]+'\n')
f.close() 
g.close()