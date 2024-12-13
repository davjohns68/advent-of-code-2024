#!/usr/bin/python

inputFile = open("/usr/local/google/home/davjohns/git/advent-of-code-2024/input-day-1","r")

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
