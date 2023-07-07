with open('PointsAndFieldGoalsAttempted.csv', 'r') as f:
    chart = open('PointsAndFieldGoalsAttempted2.csv', 'a')
    str0 = f.readline().split(',')
    while len(str0):
        str1, p0, p1, n = f.readline().split(','), int(str0[1]), int(str0[2]), 1
        while str1[0] == str0[0]:
            p0 += int(str1[1])
            p1 += int(str1[2])
            n += 1
            str1 = f.readline().split(',')
        chart.writelines(str0[0] + ',' + str(p0 / n) + ',' + str(p1 / n) + ',\n')
        str0 = str1
