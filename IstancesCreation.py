import numpy as np

folder = 'instances'
num_instances = 10
ub = 30
lb = 0


def foo(file_path, num_jobs, distribution_1, distribution_2, increment):

    for k in range(0, num_instances):
        path = file_path + str(k)
        fp = open(path, 'w')
        r=[]
        p=[]

        if distribution_1 == "normal_high":
            r = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
        elif distribution_1 == "normal_low":
            r = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
        elif distribution_1 == "uniform":
            r = np.random.default_rng().uniform(lb, ub, num_jobs)
        elif distribution_1 == "uniform_far":
            r = np.random.default_rng().uniform(lb, ub, num_jobs) + 50
        elif distribution_1 == "uniform_close":
            r = np.random.default_rng().uniform(lb, ub, num_jobs) / 10

        if distribution_2 == "normal_high":
            p = np.random.default_rng().normal((ub - lb) / 2 + 10.0, 10.0, num_jobs)
        elif distribution_2 == "normal_low":
            p = np.random.default_rng().normal((ub - lb) / 2, 1.0, num_jobs)
        elif distribution_2 == "uniform":
            p = np.random.default_rng().uniform(lb, ub, num_jobs)

        for h in range(0, num_jobs):
            if int(r[h]) >= 0 and int(p[h]) > 0:
                line = str(int(r[h])) + ',' + str(int(p[h])) + '\n'
                fp.write(line)

        num_jobs += increment

################################################################################
# few


num_jobs = 10

# FEW JOBS / RJ HIGH VARIANCE PJ UNIFORM
file_path = folder + "/few high variance/instance_F_HU_"
foo(file_path, num_jobs, "normal_high", "uniform", 2)

# FEW JOBS / RJ UNIFORM PJ HIGH VARIANCE
file_path = folder + "/few high variance/instance_F_UH_"
foo(file_path, num_jobs, "uniform", "normal_high", 2)

# FEW JOBS / RJ HIGH VARIANCE PJ HIGH VARIANCE
file_path = folder + "/few high variance/instance_F_HH_"
foo(file_path, num_jobs, "normal_high", "normal_high", 2)

# FEW JOBS / RJ LOW VARIANCE PJ UNIFORM
file_path = folder + "/few low variance/instance_F_LU_"
foo(file_path, num_jobs, "normal_low", "uniform", 2)

# FEW JOBS / RJ UNIFORM PJ LOW VARIANCE
file_path = folder + "/few low variance/instance_F_UL_"
foo(file_path, num_jobs, "uniform", "normal_low", 2)

# FEW JOBS / RJ LOW VARIANCE PJ LOW VARIANCE
file_path = folder + "/few low variance/instance_F_LL_"
foo(file_path, num_jobs, "normal_low", "normal_low", 2)

# FEW JOBS / RJ LOW VARIANCE PJ HIGH VARIANCE
file_path = folder + "/few low variance/instance_F_LH_"
foo(file_path, num_jobs, "normal_low", "normal_high", 2)

# FEW JOBS / RJ HIGH VARIANCE PJ LOW VARIANCE
file_path = folder + "/few low variance/instance_F_HL_"
foo(file_path, num_jobs, "normal_high", "normal_low", 2)

# FEW JOBS / RJ UNIFORM PJ UNIFORM
file_path = folder + "/few uniform/instance_F_UU_"
foo(file_path, num_jobs, "uniform", "uniform", 2)

# FEW JOBS / Rj few far from zero
file_path = folder + "/few far from zero/instance_"
foo(file_path, num_jobs, "uniform_far", "uniform", 2)

# FEW JOBS / Rj few  close to zero
file_path = folder + "/few close to zero/instance_"
foo(file_path, num_jobs, "uniform_close", "uniform", 2)

####################################################################################
# many
num_jobs = 100

# MANY JOBS / RJ HIGH VARIANCE PJ few many uniform
file_path = folder + "/many high variance/instance_M_HU_"
foo(file_path, num_jobs, "normal_high", "uniform", 10)

# MANY JOBS / RJ UNIFORM PJ HIGH VARIANCE
file_path = folder + "/many high variance/instance_M_UH_"
foo(file_path, num_jobs, "uniform", "normal_high", 10)

# MANY JOBS / RJ HIGH VARIANCE PJ HIGH VARIANCE
file_path = folder + "/many high variance/instance_M_HH_"
foo(file_path, num_jobs, "normal_high", "normal_high", 10)

# MANY JOBS / RJ LOW VARIANCE PJ UNIFORM
file_path = folder + "/many low variance/instance_M_LU_"
foo(file_path, num_jobs, "normal_low", "uniform", 10)

# MANY JOBS / RJ UNIFORM PJ LOW VARIANCE
file_path = folder + "/many low variance/instance_M_UL_"
foo(file_path, num_jobs, "uniform", "normal_low", 10)

# MANY JOBS / RJ LOW VARIANCE PJ LOW VARIANCE
file_path = folder + "/many low variance/instance_M_LL_"
foo(file_path, num_jobs, "normal_low", "normal_low", 10)

# MANY JOBS / RJ LOW VARIANCE PJ HIGH VARIANCE
file_path = folder + "/many low variance/instance_M_LH_"
foo(file_path, num_jobs, "normal_low", "normal_high", 10)

# MANY JOBS / RJ HIGH VARIANCE PJ LOW VARIANCE
file_path = folder + "/many low variance/instance_M_HL_"
foo(file_path, num_jobs, "normal_high", "normal_low", 10)

# MANY JOBS / RJ UNIFORM PJ UNIFORM
file_path = folder + "/many uniform/instance_M_UU_"
foo(file_path, num_jobs, "uniform", "uniform", 10)

# MANY JOBS / Rj many far from zero
file_path = folder + "/many far from zero/instance_"
foo(file_path, num_jobs, "uniform_far", "uniform", 10)

# MANY JOBS / Rj many close to zero
file_path = folder + "/many close to zero/instance_"
foo(file_path, num_jobs, "uniform_close", "uniform", 10)

print("END")
