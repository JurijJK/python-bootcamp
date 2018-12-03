
import sys

with open("logs.txt") as f:

    for line in f:
        line = line.split(";")
        user = line[0]
        action = line[1]
        time = line[2]
        time = int(time)

        # print(line, time)

    for user in f:
        if action == 'LOGIN':
            time = -time

        else:
            time = time


