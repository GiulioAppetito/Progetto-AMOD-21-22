import gurobipy as gp
from gurobipy import GRB


class GurobiPLI:
    def __init__(self, release_times, processing_times):
        global t
        self.r = []
        self.p = []
        for i in range(len(release_times)):
            self.r.append(release_times[i])
            self.p.append(processing_times[i])
        M = gp.quicksum(self.p[j] for j in range(len(release_times))) + max(self.r)
        J = range(len(self.r))
        releaseSum = 0
        for j in J:
            releaseSum += self.r[j]
        length = len(self.r) + 100
        T = range(length)

        # model
        self.m = gp.Model("Scheduling")

        # variables
        x = self.m.addVars(J, T, vtype=GRB.BINARY, name="x")
        C = self.m.addVars(J, vtype=GRB.INTEGER, name="C")
        y = self.m.addVars(J, vtype=GRB.INTEGER, name="y")

        # constraints
        for j in J:
            for t in range(0, self.r[j]):
                self.m.addConstr(x[j, t] == 0)
        for j in J:
            self.m.addConstr(gp.quicksum(x[j, t] for t in T) == self.p[j])
            self.m.addConstr(C[j] == (y[j] + 1))
            for t in T:
                self.m.addConstr(y[j] >= (t * x[j, t]))
        for t in T:
            self.m.addConstr(gp.quicksum(x[j, t] for j in J) <= 1)

        self.m.setObjective(gp.quicksum(C[j] for j in J), GRB.MINIMIZE)

    def solve(self):
        self.m.optimize()
        return self.m.getAttr("ObjVal")
