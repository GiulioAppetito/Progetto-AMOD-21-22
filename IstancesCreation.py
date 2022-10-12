import numpy as np

num_instances = 3
ub = 30
lb = 0

folder = 'instances/few jobs'
num_jobs = 10

# FEW JOBS / RJ HIGH VARIANCE PJ UNIFORM

file_Path = folder + "/high variance/instance_F_HU_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >=0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ UNIFORM PJ HIGH VARIANCE
file_Path = folder + "/high variance/instance_F_UH_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ HIGH VARIANCE PJ HIGH VARIANCE
file_Path = folder + "/high variance/instance_F_HH_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >= 0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ LOW VARIANCE PJ UNIFORM

file_Path = folder + "/low variance/instance_F_LU_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ UNIFORM PJ LOW VARIANCE

file_Path = folder + "/low variance/instance_F_UL_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ LOW VARIANCE PJ LOW VARIANCE

file_Path = folder + "/low variance/instance_F_LL_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ LOW VARIANCE PJ HIGH VARIANCE

file_Path = folder + "/low variance/instance_F_LH_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ HIGH VARIANCE PJ LOW VARIANCE

file_Path = folder + "/low variance/instance_F_HL_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >= 0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 2

# FEW JOBS / RJ UNIFORM PJ UNIFORM

file_Path = folder + "/uniform/instance_F_UU_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / Rj far from zero

file_Path = folder + "/uniform/far from zero/instance_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    r = r + 50
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

# FEW JOBS / Rj close to zero

file_Path = folder + "/uniform/close to zero/instance_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    r = r / 10
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 2

####################################################################################

# MANY JOBS / RJ HIGH VARIANCE PJ uniform
folder = 'instances/many jobs'
num_jobs = 100

file_Path = folder + "/high variance/instance_F_HU_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >= 0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ UNIFORM PJ HIGH VARIANCE

file_Path = folder + "/high variance/instance_F_UH_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >= 0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ HIGH VARIANCE PJ HIGH VARIANCE

file_Path = folder + "/high variance/instance_F_HH_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >= 0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ LOW VARIANCE PJ UNIFORM

file_Path = folder + "/low variance/instance_F_LU_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ UNIFORM PJ LOW VARIANCE

file_Path = folder + "/low variance/instance_F_UL_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ LOW VARIANCE PJ LOW VARIANCE

file_Path = folder + "/low variance/instance_F_LL_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ LOW VARIANCE PJ HIGH VARIANCE

file_Path = folder + "/low variance/instance_F_LH_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ HIGH VARIANCE PJ LOW VARIANCE

file_Path = folder + "/low variance/instance_F_HL_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
    p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)

    for j in range(0, num_jobs):
        if r[j] >= 0 and p[j] >= 0:
            line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
            fp.write(line)

    num_jobs += 10

# MANY JOBS / RJ UNIFORM PJ UNIFORM

file_Path = folder + "/uniform/instance_F_UU_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

# MANY JOBS / Rj far from zero

file_Path = folder + "/uniform/far from zero/instance_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    r = r + 50
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

# MANY JOBS / Rj close to zero

file_Path = folder + "/uniform/close to zero/instance_"

for i in range(0, num_instances):
    path = file_Path + str(i)
    fp = open(path, 'w')

    r = np.random.default_rng().uniform(lb, ub, num_jobs)
    r = r / 10
    p = np.random.default_rng().uniform(lb, ub, num_jobs)

    for j in range(0, num_jobs):
        line = str(int(r[j])) + ',' + str(int(p[j])) + '\n'
        fp.write(line)

    num_jobs += 10

print("END")
