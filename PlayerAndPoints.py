with open('chart.csv', 'r') as f:
    str0 = f.readline()
    chart = open('PlayerAndPoints.csv', 'a')
    chart.writelines(',points,\n')
    while len(str0):
        if 'Player:' in str0:
            str1 = f.readline().split(',')
            if ' Points ' in str1:
                n = str1.index(' Points ')
                str3 = f.readline()
                while 'Team:' not in str3:
                    str3 = str3.split(',')
                    chart.writelines(str3[1] + ',' + str3[n] + ',\n')
                    str3 = f.readline()
        str0 = f.readline()
