class Job:
    def __init__(self, release_time, processing_time):
        self.remainingLifetime = processing_time
        self.releaseDate = release_time
        self.processingTime = processing_time

    def isCompleted(self):
        if self.remainingLifetime > 0:
            return False
        else:
            return True

    def reduce(self, time):
        self.remainingLifetime -= time

    def resetLifetime(self):
        self.remainingLifetime = self.processingTime


class SchedulingInstance:
    def __init__(self, release_times, processing_times):
        self.r = release_times
        self.p = processing_times
