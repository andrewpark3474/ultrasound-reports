import os, sys


collection = f'collection.txt'
finding = f'finding.txt'
impression = f'impression.txt'
treatment = f'treatment.txt'
with open(collection, 'r', encoding = 'utf-8') as f:
    with open(finding, 'w', encoding = 'utf-8') as ff:
        with open(impression, 'w', encoding = 'utf-8') as fi: 
            with open(treatment, 'w', encoding = 'utf-8') as ft: 
                flag = 0
                tmpf = []
                tmpi = []
                tmpt = []
                for idx, line in enumerate(f.readlines()):
                    # input(line)
                    if len(line.strip()) < 2: continue
                    if '超声所见：' in line: 
                        print('flag = 1')
                        flag = 1
                        if not tmpf == []: ff.write('#'.join(tmp.strip() for tmp in tmpf) + '\n')
                        if tmpf == []: input(f'超声所见： is None at {idx}')
                        tmpf = []
                        continue
                    elif '超声提示：' in line: 
                        print('flag = 2') 
                        flag = 2
                        if not tmpi == []: fi.write('#'.join(tmp.strip() for tmp in tmpi) + '\n')
                        if tmpi == []: input(f'超声提示： is None at {idx}')
                        tmpi = []
                        continue
                    elif '诊断意见：' in line: 
                        print('flag = 3')
                        if not tmpt == []: ft.write('#'.join(tmp.strip() for tmp in tmpt) + '\n')
                        if tmpt == []: input(f'诊断意见： is None at {idx}')
                        flag = 3
                        tmpt = []
                        continue

                    if flag == 1:
                        tmpf.append(line)
                    elif flag == 2:
                        tmpi.append(line)
                    elif flag == 3:
                        tmpt.append(line)

                
                














