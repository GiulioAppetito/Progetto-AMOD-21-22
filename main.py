import csv
import os
from BranchAndBound import BranchAndBound
from SchedulingProblem import SchedulingProblem
from Timer import Timer
from func_timeout import func_timeout, FunctionTimedOut


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


APX_CYPHERS = 5  # round cyphers
FILENAME = "results.csv"  # file to print results
LIMIT = 20  # time limit for each instance of BnB

# create the csv writer.
f = open(FILENAME, "w", newline="")
writer = csv.writer(f)
writer.writerow(["filename", "# jobs", "bnb interrupted", "gurobi solution", "bnb solution", "gurobi time", "bnb time", "release dates",
                 "processing times"])

# traverse root directory, and list directories as dirs and files as files
filesNames = []
for root, d_names, f_names in os.walk("instances"):
    for f in f_names:
        filesNames.append(os.path.join(root, f))
for filename in filesNames:
    print(bcolors.WARNING + filename + bcolors.ENDC)
    # instance creation.
    r = []
    p = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            r.append(int(row[0]))
            p.append(int(row[1]))
        gurobiProblem = SchedulingProblem(r, p)
        bnbProblem = BranchAndBound(r, p)

        # gurobi execution.
        timer = Timer()
        timer.start()
        gurobiSolution = gurobiProblem.solve()
        gurobiTime = timer.stop()

        # BnB execution.
        interrupted = False
        try:
            timer = Timer()
            timer.start()
            bnbSolution = func_timeout(LIMIT, bnbProblem.solve)
            bnbTime = timer.stop()
        except FunctionTimedOut:
            bnbSolution = bnbProblem.getIncumbent()
            bnbTime = LIMIT
            interrupted = True

        # write on file.
        writer.writerow([filename, len(r),interrupted, gurobiSolution, bnbSolution, gurobiTime, bnbTime, r, p])
