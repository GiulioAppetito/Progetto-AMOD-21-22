import math
import copy
import datetime

from Entities import Job
from Timer import Timer


class Node:
    def __init__(self, fixed, unfixed):
        self.fixedJobs = fixed
        self.notFixedJobs = unfixed
        self.LB = 0.0


def SRPTN(node, current, initialSum):
    activeJobs = []
    completedJobs = []
    usesPreemption = False
    completionSum = initialSum
    releaseDates = []

    if node.notFixedJobs is not None:
        for j in node.notFixedJobs:
            j.resetLifetime()
            releaseDates.append(j.releaseDate)
    else:
        return

    t_current = current

    # timer initialization.
    timer = Timer()
    timer.start()

    # loop.
    stop = False

    while len(completedJobs) < len(node.notFixedJobs):
        # if there's no active jobs, advance the clock until next released job: used for the first cycle and in every idle period
        while len(activeJobs) == 0:
            for job in node.notFixedJobs:
                if job.releaseDate <= t_current:
                    activeJobs.append(job)
                    stop = True
            if stop:
                stop = False
                break
            else:
                t_current += 1

        # search for job with the shortest remaining lifetime.
        nextJob = activeJobs[0]
        for job in activeJobs:
            if job.remainingLifetime <= nextJob.remainingLifetime:
                nextJob = job
                # t_current = nextJob.releaseDate + t_current
        # find next release date.
        t_next = math.inf
        for t in releaseDates:
            if t_next >= t > t_current:
                t_next = t

        # process nextJob until next release date.
        if t_next >= (nextJob.remainingLifetime + t_current):
            t_next = nextJob.remainingLifetime + t_current
        else:
            usesPreemption = True

        nextJob.reduce(t_next - t_current)

        if nextJob.isCompleted():
            activeJobs.remove(nextJob)  # update clock.
            if nextJob in completedJobs:
                pass
            else:
                completedJobs.append(nextJob)
                completionSum += t_next

        # add released job(s) to list.
        for job in node.notFixedJobs:
            if job.releaseDate == t_next:
                activeJobs.append(job)
        t_current = t_next

    timer.stop()
    return completionSum, usesPreemption


class BranchAndBound:
    def __init__(self, *params):
        # initialize algorithm jobs.
        self.jobs = []
        self.releaseDates = params[0]
        self.processingTimes = params[1]
        self.completionTimesSum = 0.0
        for i in range(len(self.releaseDates)):
            self.jobs.append(Job(self.releaseDates[i], self.processingTimes[i]))
        # initialize algorithm variables.
        self.z_opt = math.inf
        self.Q = []
        self.incumbent = math.inf

    # actual b&b
    def solve(self):
        print("B&B execution, start : "+ str(datetime.datetime.now()))
        # solve the relaxed problem.
        root = Node([], self.jobs)
        result, preemptive = SRPTN(root, 0, 0)
        root.LB = result
        self.incumbent = root.LB
        if not preemptive and result < self.z_opt:
            self.z_opt = result
        if root.LB < self.z_opt:
            self.Q.append(root)

        # cycle until a non-preemptive solution with LB opt
        while len(self.Q) > 0:
            node = self.Q.pop()
            if len(node.notFixedJobs) > 0:  # is not a leaf.
                for job in node.notFixedJobs:

                    idx = node.notFixedJobs.index(job)

                    p_fixedJobs = copy.deepcopy(node.fixedJobs[:])
                    p_notFixedJobs = copy.deepcopy(node.notFixedJobs[:])

                    p_fixedJobs.append(job)
                    p_notFixedJobs.pop(idx)

                    child = Node(p_fixedJobs, p_notFixedJobs)

                    if len(child.notFixedJobs) > 0:
                        current = 0
                        initSum = 0
                        for j in child.fixedJobs:
                            if max(j.releaseDate, current) == current:
                                current += j.processingTime

                            else:
                                current += (j.releaseDate - current) + j.processingTime
                            initSum += current

                        result, preemptive = SRPTN(child, current, initSum)
                        child.LB = result
                        if (not preemptive) and (result < self.z_opt):
                            self.z_opt = result
                            for q in self.Q:
                                if q.LB >= self.z_opt:
                                    self.Q.remove(q)
                        if child.LB < self.z_opt:
                            self.incumbent = child.LB
                            self.Q.append(child)
        return self.z_opt

    def getIncumbent(self):
        return self.incumbent
