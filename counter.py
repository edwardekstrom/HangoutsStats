from math import ceil
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
for baller in canzzersNames:
    canzzersCounts[baller] = 0

for line in canz:
    for name in canzzersNames:
        if line == name:
            canzzersCounts[line] += 1

total = 0
for baller in canzzersNames:
    total += canzzersCounts[baller]

sortedBallers = sorted(canzzersCounts, key=canzzersCounts.get)

for baller in reversed(sortedBallers):
    print(baller[:-1] + ' = ' + str(canzzersCounts[baller]) + ' (' + str(ceil((canzzersCounts[baller] / total) * 100) / 100) + ')')
