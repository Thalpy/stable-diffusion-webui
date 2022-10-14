import os
names = os.listdir('./scripts/wildcards')

doc = open("wildcardNames.txt", "w")

for x in names:
    x = x[0:-4]
    doc.write(x)
    doc.write("\n")