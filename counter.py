import sys
from Baller import Baller
import operator

canz = open('canzzersCon.txt', encoding="utf8")

canzzersNames = ['Bryan Samuelson\n',
            'zach fackrell\n',
            'Merit Egan\n',
            'Colby Condie\n',
            'John Sherwood\n',
            'Alex Crawford\n',
            'Alex Platis\n',
            'Brayden Haws\n',
            'Tyson Amundsen\n',
            'Jared Carter\n',
            'Seth Vance\n',
            'Edward Ekstrom\n',
            'Samuel McConkie\n',
            'Jeff Knudsen\n']

canzzersCounts = {}
canzzers = {}
for baller in canzzersNames:
    canzzersCounts[baller] = 0
    canzzers[baller] = Baller(baller)

currentBaller = canzzers['Edward Ekstrom\n']
previousBaller = canzzers['Edward Ekstrom\n']
for line in canz:
    for name in canzzersNames:
        if line == name:
            canzzersCounts[name] += 1
            previousBaller = currentBaller
            currentBaller = canzzers[name]
            continue

    if "*" in line:
        currentBaller._corrections += 1
    if ("haha" in line) or ("lol" in line) or ("hags" in line) or ("haga" in line):
        previousBaller._funnyVoxes += 1
    currentBaller._characters += len(line)

total = 0
for baller in canzzersNames:
    total += canzzersCounts[baller]
    canzzers[baller]._messageCount = canzzersCounts[baller]

sortedBallers = sorted(canzzersCounts, key=canzzersCounts.get)
sys.stdout = open('stats.txt', 'w')
for baller in reversed(sortedBallers):
    canzzers[baller].print(total)
