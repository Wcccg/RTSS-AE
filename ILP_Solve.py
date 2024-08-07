# Solve the ILP model, calculate the response time and end-to-end latency bounds
from ILP_Init import *
import math
import gurobipy as gp

# Use Alg.2 to solve the ILP model
def solve_ILP(DAGx, B, x):
    lb = 0
    ub = int(B/x)
    Alpha = 0
    SILP = -1
    while lb < ub:
        mid = math.ceil((ub+lb)/2)
        alpha = mid*x
        ILP = init_ILP(DAGx, alpha)
        ILP.optimize()
        if ILP.status == 2:
            SILP = ILP
            Alpha = mid*x
            ub = mid-1
        else:
            lb = mid+1
    if SILP == -1:
        SILP = ILP
        Alpha = mid*x
    return Alpha, SILP

        
# Calculate the task priority based on the ILP solution results
def get_priority(n, ILP):
    priority = []
    solution = ILP.getVars()
    for i in range(n):
        priority.append(0)
    index = 0
    for i in range(n-1):
        for j in range(i+1, n):
            var = int(solution[index].X)
            index += 1
            if var == 1:
                priority[i] += 1
            else:
                priority[j] += 1
    return priority

# Calculate end-to-end latency of task chains based on task priority
def get_latency(DAGx, Pri):
    cp = DAGx.cp
    Latencys = []
    for chain in cp:
        latency = DAGx.V[chain[0]].T
        for i in range(len(chain)-1):
            if Pri[chain[i]] > Pri[chain[i+1]]:
                latency += max(get_R(DAGx, chain[i], Pri), DAGx.V[chain[i+1]].T)
            else:
                latency += get_R(DAGx, chain[i], Pri) + DAGx.V[chain[i+1]].T
        Latencys.append(int(latency/100))
    return Latencys

# Calculate end-to-end latency of task chains based on task priority
def get_latency_2(DAGx, Pri):
    cp = DAGx.cp
    Latencys = []
    for chain in cp:
        latency = DAGx.V[chain[0]].T
        for i in range(len(chain)-1):
            if Pri[chain[i]] > Pri[chain[i+1]]:
                latency += max(get_R(DAGx, chain[i], Pri), DAGx.V[chain[i+1]].T)
            else:
                Maxlat = 0
                R_i = get_R(DAGx, chain[i], Pri)
                T = DAGx.V[chain[i]].T
                TT = DAGx.V[chain[i+1]].T
                UB = []
                ub = min(R_i, TT)
                X = 0
                GCD = gcd(T, TT)
                while X < ub:
                    UB.append(X)
                    X += GCD
                for x in UB:
                    Maxlat = max(Maxlat, math.floor((R_i-x)/TT)*TT+x)
                latency += Maxlat + TT
        Latencys.append(int(latency/100))
    return Latencys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Calculate response time of given task based on task priority
def get_R(DAGx, k, Pri):
    R0 = 0
    R = DAGx.V[k].WCET
    while R != R0:
        R0 = R
        R = DAGx.V[k].WCET
        for i in range(len(DAGx.V)):
            if Pri[i] >= Pri[k]:
                R += math.ceil(R0/DAGx.V[i].T)*DAGx.V[i].WCET
    return R

# baseline, descending priority (DP) policy
def get_pri_baseline1(DAGx):
    n = len(DAGx.V)
    Pri = []
    for i in range(n):
        Pri.append(n-i-1)
    return Pri

# baseline, rate monotonic (RM) policy
def get_pri_baseline2(DAGx):
    n = len(DAGx.V)
    Ind = []
    TM = []
    for i in range(n):
        Ind.append(i)
        TM.append(DAGx.V[i].T)
    for i in range(n-1):
        for j in range(n-i-1):
            if TM[j] >= TM[j+1]:
                temp = TM[j]
                TM[j] = TM[j+1]
                TM[j+1] = temp
                temp2 = Ind[j]
                Ind[j] = Ind[j+1]
                Ind[j+1] = temp2
    Pri = []
    for i in range(n):
        for j in range(n):
            if Ind[j] == i:
                Pri.append(n-j)
                break
    return Pri

# Calculate the latency boundary constraints of task chains
def get_latency_boundary(DAGx,lbd):
    cp = DAGx.cp
    Latencys = []
    for chain in cp:
        HP = get_HP(chain,DAGx)
        L = len(chain)
        latency = HP*L*lbd
        Latencys.append(int(latency/100))
    return Latencys

# Calculate the hyper-period of given task chain
def get_HP(chain,DAGx):
    hp = 1
    for task in chain :
        hp = math.lcm(hp,DAGx.V[task].T)
    return hp
