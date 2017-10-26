# -*- coding: utf-8 -*-

import os
import sys
import shutil

def getPoetList(): 
    f = open('poetList.txt', 'w')
    path = './collection/'
    dirs = os.listdir(path)
    for poet in dirs:
        if not poet.startswith('.'):
            f.write('"' + poet + '", ')
    f.close()
    with open('poetList.txt', 'rb+') as f:
        f.seek(-2, os.SEEK_END)
        f.truncate()

def getPoemList():
    f = open('poemList.txt', 'w')
    path = './collection/'
    for poet in os.listdir(path):
        if not poet.startswith('.'):
            dirs = os.listdir(path + poet)
            for poem in dirs:
                if not poem.startswith('.'):
                    f.write('"' + poem + '", ')
    f.close()
    with open('poemList.txt', 'rb+') as f:
        f.seek(-2, os.SEEK_END)
        f.truncate()

def extractPoems():
    originPath = './collection/'
    destinationPath = './collection/'
    count = 0
    for poet in os.listdir(originPath):
        if not poet.startswith('.'):
            dirs = os.listdir(originPath + poet)
            for poem in dirs:
                if not poem.startswith('.'):
                    os.rename(originPath + poet + '/' + poem, destinationPath + str(count) + '.json')
                    count += 1
