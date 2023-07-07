pathOrign = "./checkpoint_average_best-3.pt.test_constrained.out.text"  # path of the text of tables
pathCharts = "./charts"  # path of charts

fOrign = open(pathOrign, 'r')
line = fOrign.readline()
num = 1

while len(line) > 0:
    fChart = open(pathCharts + '/chart' + str(num) + '.csv', 'w+')

    lines = ','.join(('\n'.join(line.split("<NEWLINE>"))).split('|'))
    fChart.truncate()
    fChart.writelines(lines)
    fChart.close()

    # test for the first chart
    # if num == 1:
    #    break

    num += 1
    line = fOrign.readline()

fOrign.close()
