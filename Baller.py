from math import ceil
import sys
__author__ = 'i53425'

class Baller:
    def __init__(self, ballerName):
        self._name = ballerName
        self._messageCount = 1
        self._corrections = 0
        self._characters = 0
        self._words = 0
        if self._name == 'David Monson\n':
            self._funnyVoxes = -100
        else:
            self._funnyVoxes = 0

    def print(self, total):
        print(self._name[:-1] + ':')
        print('\t total voxes: ' + str(self._messageCount)  + ' / ' + str(total))
        print('\t percent of total: ' + str(self._messageCount / total))
        print('\t used *: ' + str(self._corrections))
        print('\t characters: ' + str(self._characters))
        print('\t average vox length: ' + str(self._characters/self._messageCount))
        print('\t funny voxes: ' + str(self._funnyVoxes))
        print('\t % funny voxes: ' + str(self._funnyVoxes/self._messageCount))