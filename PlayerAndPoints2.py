with open('PlayerAndPoints.csv', 'r') as f:
    chart = open('PlayerAndPoints2.csv', 'a')
    str0 = f.readline().split(',')
    while len(str0):
        str1,p,n = f.readline().split(','),int(str0[1]),1
        while str1[0]==str0[0]:
            p+=int(str1[1])
            n+=1
            str1 = f.readline().split(',')
        chart.writelines(str0[0] + ',' + str(p/n) + ',\n')
        str0=str1