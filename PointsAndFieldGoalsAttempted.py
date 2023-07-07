with open('chart.csv', 'r') as f:
    str0 = f.readline()
    chart = open('PointsAndFieldGoalsAttempted.csv', 'a')
    while len(str0):
        if 'Player:' in str0:
            str1 = f.readline().split(',')
            if ' Points ' in str1 and ' Field goals attempted ' in str1:
                n0, n1 = str1.index(' Points '), str1.index(' Field goals attempted ')
                str3 = f.readline()
                while 'Team:' not in str3 and len(str3):
                    str3 = str3.split(',')
                    chart.writelines(str3[1] + ',' + str3[n0] + ',' + str3[n1] + '\n')
                    str3 = f.readline()
        str0 = f.readline()
