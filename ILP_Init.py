# The code in this file sets the variables and constraints of the ILP model
# Use Gurobi tool to construct and solve the ILP 
from DAG_Init import *
import gurobipy as gp
import math

# Initialize the ILP model proposed in Section V
def init_ILP(DAGx, alpha):
    ILP = gp.Model('M')
    ILP.setParam('OutputFlag',0)
    ILP, var_pri = set_var_of_pri(ILP, len(DAGx.V)) # Initialize the priority variables
    ILP = set_obj(ILP, DAGx, var_pri, alpha)        # Initialize the objective function of (54)
    ILP = add_cons_of_pri(ILP, len(DAGx.V), var_pri)        # add the constraint of (59) and (60)
    ILP = add_cons_of_latency(ILP, DAGx, var_pri, alpha)    # add the constraint of (56) and (67)
    ILP = add_cons_of_schedule(ILP, DAGx, var_pri, alpha)   # add the constraint of (55)
    return ILP

# Initialize the priority variables
def set_var_of_pri(ILP, n):
    Pri = []
    for i in range(n-1):
        temp = []
        for j in range(i+1):
            temp.append('')
        for j in range(i+1, n):
            temp.append(ILP.addVar(vtype=gp.GRB.BINARY, name = 'P_'+str(i)+'_'+str(j)))
        Pri.append(temp)
    return ILP, Pri

# Initialize the objective function of (54)
def set_obj(ILP, DAGx, var_pri, alpha):
    obj = 0
    cp = DAGx.cp
    for i in range(len(DAGx.V)):
        flag = 0
        for j in range(len(cp)):
            if i in cp[j]:
                flag = 1
                break
        if flag == 0:
            continue
        for j in range(len(DAGx.V)):
            if i < j:
                obj += math.ceil(alpha*DAGx.V[i].T/DAGx.V[j].T)*(1-var_pri[i][j])*DAGx.V[j].WCET
            elif i > j:
                obj += math.ceil(alpha*DAGx.V[i].T/DAGx.V[j].T)*(var_pri[j][i])*DAGx.V[j].WCET
    ILP.setObjective(obj, gp.GRB.MINIMIZE)
    return ILP


# add the constraint of (59) and (60)
def add_cons_of_pri(ILP, n, Pri):
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                con = Pri[i][j] + Pri[j][k] + (1-Pri[i][k])
                ILP.addConstr(con >= 0 + 0.001)
                ILP.addConstr(con <= 3 - 0.001)
    return ILP

# add the constraint of (56) and (67)
def add_cons_of_latency(ILP, DAGx, var_pri, alpha):
    cp = DAGx.cp
    for chain in cp:
        for i in range(len(chain)-1):
            task1 = chain[i]
            task2 = chain[i+1]
            con = DAGx.V[task2].T+(alpha-1)*DAGx.V[task1].WCET
            for j in range(len(DAGx.V)):
                if j < task1:
                    con -= (alpha-1)*math.ceil(alpha*DAGx.V[task1].T/DAGx.V[j].T)*DAGx.V[j].WCET*var_pri[j][task1]
                elif j > task1:
                    con -= (alpha-1)*math.ceil(alpha*DAGx.V[task1].T/DAGx.V[j].T)*DAGx.V[j].WCET*(1-var_pri[task1][j])
            B = 1e9
            if task1 > task2:
                ILP.addConstr(con <= (1-var_pri[task2][task1])*B)
                ILP.addConstr((1-var_pri[task2][task1])*B <= con + B)
            elif task1 < task2:
                ILP.addConstr(con <= var_pri[task1][task2]*B)
                ILP.addConstr(var_pri[task1][task2]*B <= con + B)
    return ILP

# add the constraint of (55)
def add_cons_of_schedule(ILP, DAGx, var_pri, alpha):
    cp = DAGx.cp
    for i in range(len(DAGx.V)):
        flag = 0
        for j in range(len(cp)):
            if i in cp[j]:
                flag = 1
                break
        if flag == 0:
            continue
        con = DAGx.V[i].WCET
        for j in range(len(DAGx.V)):
            if i < j:
                con += math.ceil(alpha*DAGx.V[i].T/DAGx.V[j].T)*(1-var_pri[i][j])*DAGx.V[j].WCET
            elif i > j:
                con += math.ceil(alpha*DAGx.V[i].T/DAGx.V[j].T)*var_pri[j][i]*DAGx.V[j].WCET
        ILP.addConstr(con <= alpha*DAGx.V[i].T)
    return ILP


