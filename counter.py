import sys
from Baller import Baller
chats = ['worsleyCon', "canzzersCon"]
for chat in chats:
    canz = open(chat + '.txt', encoding="utf8")

    canzzersNames = canz.readline()
    canzzersNames = canzzersNames[:-1].split(",")
    firstLine = []
    for name in canzzersNames:
        firstLine.append(name + "\n")
    canzzersNames = firstLine
    canzzersCounts = {}
    canzzers = {}
    for baller in canzzersNames:
        canzzersCounts[baller] = 0
        canzzers[baller] = Baller(baller)

    currentBaller = canzzers['Edward Ekstrom\n']
    previousBaller = canzzers['Edward Ekstrom\n']
    funnyCanzzer = None
    hasFunnyCanzzer = False
    continueFlag = False
    for line in canz:
        for name in canzzersNames:
            if line == name:
                canzzersCounts[name] += 1
                currentBaller._messageCount += 1
                previousBaller = currentBaller
                currentBaller = canzzers[name]
                continueFlag = True
                break
        if continueFlag:
            continueFlag = False
            continue
        lowerLine = line.lower()
        if "*" in line:
            currentBaller._corrections += 1
        if ("haha" in lowerLine) or ("lol" in lowerLine) or ("hags" in lowerLine) or ("haga" in lowerLine):
            currentBaller._laughsAt += 1
            if not hasFunnyCanzzer:
                hasFunnyCanzzer = True
                funnyCanzzer = previousBaller
                funnyCanzzer._funnyVoxes += 1
            else:
                funnyCanzzer._funnyVoxes += 1
        else:
            hasFunnyCanzzer = False
            funnyCanzzer = None
        currentBaller._characters += len(line)

    total = 0
    for baller in canzzersNames:
        total += canzzersCounts[baller]

    sortedBallers = sorted(canzzersCounts, key=canzzersCounts.get)
    sys.stdout = open(chat + 'Stats.txt', 'w')
    for baller in reversed(sortedBallers):
        canzzers[baller].print(total)
