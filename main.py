import csv
import math
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


APX_CYPHERS = 4  # round cyphers

name = 0


def main():
    global limit
    limit = float(input("Set time limit for execution [sec] : "))

    # traverse root directory, and list directories as dirs and files as files
    filenames = []
    directories = []
    for root, d_names, f_names in os.walk("instances"):
        for d in d_names:
            directories.append(d)
    print(bcolors.OKGREEN)
    for directory in directories:
        print(directory)
    print(bcolors.ENDC)

    for directory in directories:
        filenames = []
        with open("results/" + directory + ".csv", 'w') as results_directory:
            directory_csv_writer = csv.writer(results_directory)
            directory_csv_writer.writerow(
                ["instance", "jobs", "gurobi interrupted", "bnb interrupted", "gurobiSolution", "bnbSolution", "gurobiTime", "bnbTime"])

            for root, d_names, f_names in os.walk("instances/" + directory):
                for f in f_names:
                    filenames.append(os.path.join(root, f))
            for instance in filenames:
                print(bcolors.WARNING + instance + bcolors.ENDC)
                # instance creation.
                r = []
                p = []

                with open(instance) as instance_csv_file:
                    bnbInterrupted = False
                    gurobiInterrupted = False
                    instance_csv_reader = csv.reader(instance_csv_file, delimiter=',')
                    for row in instance_csv_reader:
                        r.append(int(row[0]))
                        p.append(int(row[1]))
                    gurobiProblem = SchedulingProblem(r, p, limit)
                    bnbProblem = BranchAndBound(r, p)

                    # gurobi execution.
                    timer = Timer()
                    timer.start()
                    gurobiProblem.solve()
                    gurobiTime = timer.stop()
                    if gurobiTime >= limit:
                        gurobiInterrupted = True
                    gurobiSolution = gurobiProblem.getObjFunVal()
                    # BnB execution.

                    try:
                        timer = Timer()
                        timer.start()
                        bnbSolution = func_timeout(limit, bnbProblem.solve)
                        #bnbSolution = bnbProblem.solve()
                        bnbTime = timer.stop()
                    except FunctionTimedOut:
                        bnbSolution = bnbProblem.getIncumbent()
                        bnbTime = limit
                        bnbInterrupted = True

                    # write on file.
                    directory_csv_writer.writerow(
                        [instance, len(r), gurobiInterrupted, bnbInterrupted, gurobiSolution, bnbSolution,
                         round(gurobiTime, APX_CYPHERS), round(bnbTime, APX_CYPHERS)])
                    instance_csv_file.close()


main()
