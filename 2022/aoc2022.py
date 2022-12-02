import sys
import numpy as np

def import_data(file, ftype=str):
    with open(file, 'r') as fname:
        return [ftype(x.rstrip('\n')) for x in fname.readlines()]
    
    
### Day 1
def day1(day, timeit=False):
    data = import_data('input/{}.txt'.format(day))
    
    ### Part 1
    nr_elves = data.count('') + 1
    elves = np.zeros(nr_elves)
    
    elf = 0
    for item in data:
        if item == '':
            elf += 1
        else:
            elves[elf] += int(item)
    
    if not timeit:
        print("Elf with the most carried calories: {}".format(max(elves)))
    
    ### Part 2
    if not timeit:
        print("Calories carried by the top 3 elves: {}".format(sum(sorted(elves)[-3:])))


### Day 2
def day2(day, timeit=False):
    data = import_data('input/{}.txt'.format(day))
    
    ### Part 1
    # A, X: Rock
    # B, Y: Paper
    # C, Z: Scissors
    rps = {'A': 'X', 'B': 'Y', 'C': 'Z', 'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    
    def rps_outcome(a, b):
        # Draw
        if a == b:
            return 3
        # Win
        elif (a, b) in [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')]:
            return 6
        # Loss
        else:
            return 0
    
    for instr in data:
        a, b = instr.split(' ')
        score += rps[b]
        score += rps_outcome(rps[a], b)
    
    if not timeit:
        print("Total score according to the (assumed) strategy guide: {}".format(score))
    
    ### Part 2
    rps = {'A': (1, 'B', 'C'), 'B': (2, 'C', 'A'), 'C': (3, 'A', 'B')}
    score = 0
    
    def rps_outcome2(a, b):
        # Need to lose
        if b == 'X':
            return rps[a][2], 0
        # Need to end in a draw
        elif b == 'Y':
            return a, 3
        # Need to win
        elif b == 'Z':
            return rps[a][1], 6
    
    for instr in data:
        a, b = instr.split(' ')
        action, val = rps_outcome2(a, b)
        score += rps[action][0] + val

    if not timeit:
        print("Total score according to the strategy guide: {}".format(score))


day = sys.argv[1].rstrip('ex')

if len(sys.argv) > 2:
    import time
    t = []
    for i in range(50):
        start = time.perf_counter()
        locals()["day" + day](sys.argv[1], True)
        t.append(time.perf_counter() - start)
    print("Day {}".format(day))
    print("Minimum of 50 runs: {} s".format(min(t)))
    print("Average of 50 runs: {} s".format(np.mean(t)))
    import matplotlib.pyplot as plt
    plt.plot(t)
    plt.title("Day {}".format(sys.argv[1]))
    plt.xlabel("Run nr.")
    plt.ylabel("Time")
    plt.show()
else:
    locals()["day" + day](sys.argv[1])
