import sys
import time
starttime = time.time()
file = open("words.txt", "r")
input = file.read()
words = input.split("\n")

def isEdge(s1, s2):
    if len(s1) != len(s2): return False
    if s1 == s2: return False
    count = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count >= 2:
                return False
    return True


dict = {}
for i in words:
    dict[i] = []
for a in words:
    for b in words:
        if isEdge(a, b):
            l = dict[a]
            l.append(b)
            dict[a] = l
readtime = time.time()-starttime
#2
#A
print('A: ', len(words))

#B
count = 0
for i in words:
    count += len(dict[i])
print('B: ', count/2)

#C
neighboursof = sys.argv[1]
neighbourcount = 0
for i in range(0, len(words)):
    if(isEdge(neighboursof, words[i])):
        neighbourcount+=1
print('C: ', neighbourcount)

#D
print('D: ', readtime)

#E
print('E: ', time.time()-starttime)

#F
maxwords = []
maxcount = 0
for i in dict:
    if len(dict[i]) > maxcount:
        maxwords = [i]
        maxcount = len(dict[i])
    elif len(dict[i]) == maxcount:
        maxwords.append(i)
print('F: ', 'Count: ', maxcount, '\nWords: ', maxwords)

#G
dictalreadyseen = {} #2018
conncount = 0

maxconn = []
tempmaxconn = []
maxsize = 0
maxconncount = 0
for i in dict:
    if i not in dictalreadyseen:
        tree = [i]
        tempmaxconn.append(i)
        while len(tree)>0:
            current = tree.pop(0)
            dictalreadyseen[current] = ''
            for j in dict[current]:
                if j not in dictalreadyseen:
                    tree.append(j)
                    tempmaxconn.append(j)
                    maxconncount += 1
                    dictalreadyseen[j] = ''
        if maxconncount > maxsize:
            maxconn = tempmaxconn
            maxsize = maxconncount
            tempmaxconn = []
            maxconncount = 0
        conncount += 1
print('G: ', conncount)

#H
print('H: ', maxconn)
print(len(maxconn)) #1625