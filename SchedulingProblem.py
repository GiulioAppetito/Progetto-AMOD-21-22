import gurobipy as gp
from gurobipy import GRB


class SchedulingProblem:
    def __init__(self, release_times, processing_times):
        self.r = []
        self.p = []
        for i in range(len(release_times)):
            self.r.append(release_times[i])
            self.p.append(processing_times[i])
        M = gp.quicksum(self.p[j] for j in range(len(release_times))) + max(self.r)
        J = range(len(self.r))

        # model
        self.m = gp.Model("Scheduling")
        self.m.setParam('TimeLimit', 1)

        # variables
        x = self.m.addVars(J, J, vtype=GRB.BINARY, name="x")
        s = self.m.addVars(J, vtype=GRB.INTEGER, name="s")

        # constraints
        for i in J:
            for j in J:
                if i < j:
                    self.m.addConstr(s[j] >= (s[i] + self.p[i] - M * (1 - x[i, j])))
                    self.m.addConstr(s[i] >= (s[j] + self.p[j] - M * x[i, j]))
        for j in J:
            self.m.addConstr(s[j] >= self.r[j])

        self.m.setObjective(gp.quicksum(s[j] + self.p[j] for j in J), GRB.MINIMIZE)

    def solve(self):
        self.m.optimize()
        return self.m.getAttr("ObjVal")