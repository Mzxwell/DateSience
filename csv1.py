with open('checkpoint_average_best-3.pt.test_constrained.out.txt', 'r') as f:
    str0 = ','.join(('\n'.join(f.readline().split('<NEWLINE>'))).split('|'))
    chart = open('chart.csv', 'a')
    while len(str0):
        chart.write(str0)
        str0 = ','.join(('\n'.join(f.readline().split('<NEWLINE>'))).split('|'))
