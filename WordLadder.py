import sys
import time
starttime = time.time()
file = open("words.txt", "r")
input = file.read()
words = input.split("\n")
#print(words)
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
#print(isEdge('potato', 'potojo')) #doesnt work for 2 of same words but that doesnt matter
print("2")
print('A: ', len(words))
edgeCount = 0
edges = {}
for i in range(0, len(words)):
    for j in range(i, len(words)):
        if isEdge(words[i], words[j]):
            edgeCount+=1
            if len(edges[words[i]]>0):
                edges[words[i]].append(words[j])
            else:
                edges[words[i]] = [words[j]]
            if len(edges[words[j]]>0):
                edges[words[j]].append(words[i])
            else:
                edges[words[j]] = words[i]
timetaken = time.time()-starttime
print('B: ', edgeCount)
neighboursof = sys.argv[1]
neighbourcount = 0
for i in range(0, len(words)):
    if(isEdge(neighboursof, words[i])):
        neighbourcount+=1
print('C: ', neighbourcount)
print('D: ', timetaken)
print('E: ', time.time()-starttime)

print('3')
maxwords = []
max = 0
print(len(edges['grapes']))
print(edges['grapes'])
for i in edges:
    #print(edges[i])
    if len(edges[i]) > max:
        max = len(edges[i])
        maxwords = i
    if len(edges[i]) == max:
        maxwords += i
print(maxwords, max)