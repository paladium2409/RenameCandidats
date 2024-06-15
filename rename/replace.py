import os

oldList = []
newList = []

linesFile = open('./candidats.txt','r').readlines()
for l in linesFile:
    parsed = l.split(';')
    oldList.append(parsed[0])
    newList.append(parsed[1])

for i in range(len(oldList)):
    old = oldList[i]
    new = newList[i]

    if not os.path.exists(f'./output/{new}'): os.makedirs(f'./output/{new}')

    for fileName in os.listdir('./input/'):
        if old in fileName:
            newFileName = f"{new} {fileName.replace(old, '')}"
            print(f"Rename {fileName} en {newFileName}")
            os.rename(f'./input/{fileName}', f'./output/{new}/{newFileName}')
