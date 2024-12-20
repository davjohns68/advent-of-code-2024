#!/usr/bin/python

inputFile = open("../input-day-1","r")

locIDs = []
for item in inputFile:
    locIDs.append(item)

# Part 1
locs1 = []
locs2 = []
for line in locIDs:
    line = line.strip()
    temp = line.split(" ")
    locs1.append(int(temp[0]))
    locs2.append(int(temp[-1]))
locs1.sort()
locs2.sort()
distance = 0
for i in range(len(locs1)):
    distance += abs((locs1[i] - locs2[i]))
print(distance)

# Part 2
similarity = 0
for loc in locs1:
    similarity += (loc * locs2.count(loc))

print(similarity)
