with open('chart.csv', 'r') as f:
    str0 = f.readline()
    chart = open('chart0.csv', 'a')
    chart.writelines(', ,total,\n')
    while len(str0):
        if 'Team:' in str0:
            str1 = f.readline().split(',')
            if ' Total points ' in str1:
                n = str1.index(' Total points ')
                str4, str3 = f.readline().split(','), f.readline().split(',')
                a = int(str3[n]) + int(str4[n])
                chart.writelines(',' + str3[1] + 'and' + str4[1] + ',' + str(a) + ',\n')
        str0 = f.readline()
