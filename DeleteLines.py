with open("WinsAndTotalPoints.csv", "r") as f:
    lines = f.readlines()
with open("WinsAndTotalPoints.csv", "w") as f:
    for line in lines:
        if ',  'not in line and ',  ,'not in line:
            f.write(line)
