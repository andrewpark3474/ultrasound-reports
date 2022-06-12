import os, sys


fileName = f'score.txt'
saveName = f'index_{fileName}'

with open(fileName, 'r', encoding = 'utf-8') as fo:
    indexed = []
    for idx, line in enumerate(fo.readlines()):
        indexed.append(f'{idx} {line}')

    with open(saveName, 'w', encoding = 'utf-8') as fw:
        fw.write(''.join(indexed))




















