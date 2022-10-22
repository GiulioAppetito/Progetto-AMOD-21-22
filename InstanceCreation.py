import numpy as np

max_num_jobs = 30
ub = 100
lb = 0

release_types = ["releasesCloseToZero", "releasesFarFromZero", "releasesLowVariance", "releasesUniform", "releasesHighVariance"]
distributions = ["processingLowVariance", "processingUniform", "processingHighVariance"]


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


def generateInstance(num_jobs, lb, ub, r_distribution, p_distribution):
    releaseDates = []
    processingTimes = []

    if r_distribution == "releasesCloseToZero":
        releaseDates = np.random.default_rng().uniform(lb, ub, num_jobs) / 10
    elif r_distribution == "releasesFarFromZero":
        releaseDates = np.random.default_rng().uniform(lb, ub, num_jobs) + 50
    elif r_distribution == "releasesLowVariance":
        releaseDates = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    elif r_distribution == "releasesUniform":
        releaseDates = np.random.default_rng().uniform(lb, ub, num_jobs)
    elif r_distribution == "releasesHighVariance":
        releaseDates = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 30.0, num_jobs)

    if p_distribution == "processingLowVariance":
        processingTimes = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    elif p_distribution == "processingUniform":
        processingTimes = np.random.default_rng().uniform(lb, ub, num_jobs)
    elif p_distribution == "processingHighVariance":
        processingTimes = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 30.0, num_jobs)

    return releaseDates, processingTimes


folder = 'instances'
for release_type in release_types:
    for distribution in distributions:
        for num_jobs in range(2, max_num_jobs+1):
            print(bcolors.HEADER)
            print(release_type, distribution, num_jobs)
            print(bcolors.ENDC)
            r, p = generateInstance(num_jobs, lb, ub, release_type, distribution)
            file_path = folder + "/" + release_type + "_" + distribution+"_" + str(num_jobs)
            print(bcolors.WARNING)
            print(file_path)
            print(bcolors.ENDC)
            fp = open(file_path, 'w')
            for j in range(0, num_jobs):
                if int(r[j]) >= 0 and int(p[j]) > 0:
                    line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
                    fp.write(line)
            fp.close()
