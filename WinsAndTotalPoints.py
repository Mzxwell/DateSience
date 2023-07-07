with open('chart.csv', 'r') as f:
    str0 = f.readline()
    chart = open('WinsAndTotalPoints.csv', 'a')
    while len(str0):
        if 'Team:' in str0:
            str1 = f.readline().split(',')
            if ' Total points ' in str1 and ' Wins ' in str1:
                n0, n1 = str1.index(' Total points '), str1.index(' Wins ')
                str3 = f.readline()
                while 'Player:' not in str3 and len(str3):
                    str3 = str3.split(',')
                    chart.writelines(str3[1] + ',' + str3[n0] + ',' + str3[n1] + '\n')
                    str3 = f.readline()
        str0 = f.readline()
