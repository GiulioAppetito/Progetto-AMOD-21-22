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


APX_CYPHERS = 4  # round cyphers

name = 0


def main():
    global time_limit
    print(bcolors.OKGREEN)
    time_limit = float(input("Set time limit for execution [sec] : "))
    print(bcolors.ENDC)
    output_filename = "results" + "_" + str(time_limit) + "_sec.csv"
    output = open(output_filename, 'w')
    csv_writer = csv.writer(output)
    csv_writer.writerow(
        ["releaseTimes","processingTimes", "jobs", "gurobi interrupted", "bnb interrupted", "gurobiSolution", "bnbSolution",
         "gurobiTime", "bnbTime"])
    lenght = 0
    for filename in os.listdir("instances"):
        lenght += 1
    print("LEN : " + str(lenght))

    for filename in os.listdir("instances"):
        r = []
        p = []
        gurobiInterrupted = False
        bnbInterrupted = False
        with open(os.path.join("instances", filename), 'r') as f:
            instance_csv_reader = csv.reader(f, delimiter=',')
            for row in instance_csv_reader:
                r.append(int(row[0]))
                p.append(int(row[1]))
        print(bcolors.WARNING + filename + bcolors.ENDC)
        # gurobi execution.
        gurobiProblem = SchedulingProblem(r, p, time_limit)
        if time_limit == 0:
            # gurobi execution without stop.
            timer = Timer()
            timer.start()
            gurobiProblem.solve()
            gurobiTime = timer.stop()
            gurobiSolution = gurobiProblem.getObjFunVal()
        else:
            # gurobi execution with stop.
            timer = Timer()
            timer.start()
            gurobiProblem.solve()
            gurobiTime = timer.stop()
            if gurobiTime >= time_limit:
                gurobiTime = time_limit
                gurobiInterrupted = True
            gurobiSolution = gurobiProblem.getObjFunVal()
        # BnB execution.
        bnbProblem = BranchAndBound(r, p)
        timer = Timer()
        timer.start()
        if time_limit != 0:
            # bnb execution with stop.
            try:
                timer = Timer()
                timer.start()
                bnbSolution = func_timeout(time_limit, bnbProblem.solve)
                # bnbSolution = bnbProblem.solve()
                bnbTime = timer.stop()
            except FunctionTimedOut:
                bnbSolution = bnbProblem.getIncumbent()
                bnbTime = time_limit
                bnbInterrupted = True
        else:
            # BnB execution without stop.
            timer = Timer()
            timer.start()
            bnbSolution = bnbProblem.solve()
            bnbTime = timer.stop()

        s = filename.split("_")

        r_type = s[0]
        s_type = s[1]

        csv_writer.writerow(
            [r_type, s_type, len(r), gurobiInterrupted, bnbInterrupted, gurobiSolution, bnbSolution,
             round(gurobiTime, APX_CYPHERS), round(bnbTime, APX_CYPHERS)])


main()
