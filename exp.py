# Clear the historical data, configure the parameters, and conduct the experiment
from DAG_Init import *
from ILP_Init import *
from ILP_Solve import *
import time
import shutil
import os

def clear_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)


parameters1 = [
    [5,10,15,20,25,30,35,40,45,50],
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99],
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
]

def getPre_1(i, j):
    PRE = [parameters1[0][1], parameters1[1][4], parameters1[2][4]]
    PRE[i] = parameters1[i][j]
    n = PRE[0]
    ns = 1
    ne = 1
    O_degree = 1
    I_degree = 1
    sumU = PRE[1]
    Rate = PRE[2]
    return n, ns, ne, O_degree, I_degree, sumU, Rate


name1 = ['N', 'U', 'Rate']

# The experiment of Fig. 6, Fig. 7 and Fig. 8
def exp_1(times):
    folder_path = 'saved_Data_1'
    clear_folder(folder_path)
    times = int(times)
    for i in range(3):
        for j in range(10):
            L = 0
            L2 = 0
            for k in range(times):
                n, ns, ne, O_degree, I_degree, sumU, Rate = getPre_1(i, j)
                newDAG = initDAG(n, ns, ne, O_degree, I_degree, sumU, 1)
                Pri = get_pri_baseline1(newDAG)
                N = math.ceil((n-1)*Rate)
                change_list = random.sample(range(0, n-1), N)
                change_list.sort()
                for X in change_list:
                    if Pri[X] > Pri[X+1]:
                        temp = Pri[X]
                        Pri[X] = Pri[X+1]
                        Pri[X+1] = temp
                        while X:
                            X -= 1
                            if Pri[X] < Pri[X+2] and Pri[X] > Pri[X+1]:
                                temp = Pri[X]
                                Pri[X] = Pri[X+1]
                                Pri[X+1] = temp
                            else:
                                break
                l1 = get_latency(newDAG, Pri)[0]
                l2 = get_latency_2(newDAG, Pri)[0]
                gap1 = (l1-l2)/l1
                filename = 'saved_Data_1/gap_'+name1[i]+str(j)+'.txt'
                f = open(filename, 'a')
                print(round(gap1, 4), file=f)
                f.close()




name = ['N', 'Ns', 'Ne', 'Degree', 'U', 'Rate', 'Bound']

parameters2 = [
    [10,15,20,25,30,35,40,45,50,55],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.99],
    [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
    [0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0,1.05,1.1]
]

def getPre2(i, j):
    PRE = [parameters2[0][4], parameters2[1][2], parameters2[2][2], parameters2[3][2], parameters2[4][4], parameters2[5][4], parameters2[6][4]]
    PRE[i] = parameters2[i][j]
    n = PRE[0]
    ns = PRE[1]
    ne = PRE[2]
    O_degree = PRE[3]
    I_degree = PRE[3]
    sumU = PRE[4]
    Rate = PRE[5]
    lbd = PRE[6]
    return n, ns, ne, O_degree, I_degree, sumU, Rate, lbd

# # The experiment of Fig. 9 to Fig. 15
def exp_2(times):
    folder_path = 'saved_Data_2'
    clear_folder(folder_path)
    times = int(times)
    for i in range(7):
        for j in range(10):
            n, ns, ne, O_degree, I_degree, sumU, Rate, lbd = getPre2(i, j)
            SCILP = 0
            SCB1 = 0
            SCB2 = 0
            T = 0

            for k in range(times):
                newDAG = initDAG(n, ns, ne, O_degree, I_degree, sumU, Rate)
                BOUND = get_latency_boundary(newDAG,lbd)
                time1 = time.perf_counter()
                alpha, ILP = solve_ILP(newDAG, 3, 0.1)
                comp_time = time.perf_counter()-time1
                Pri = get_priority(n, ILP)
                Lat = get_latency(newDAG, Pri)
                sc = 1
                for j in range(len(Lat)):
                    if Lat[j] >= BOUND[j]:
                        sc = 0
                        break
                SCILP += sc       
                T += comp_time

                baseline_Pri1 = get_pri_baseline1(newDAG)
                LB1 = get_latency(newDAG, baseline_Pri1)
                sc = 1
                for j in range(len(LB1)):
                    if LB1[j] >= BOUND[j]:
                        sc = 0
                        break
                SCB1 += sc 

                baseline_Pri2 = get_pri_baseline2(newDAG)
                LB2 = get_latency(newDAG, baseline_Pri2)
                sc = 1
                for j in range(len(LB2)):
                    if LB2[j] >= BOUND[j]:
                        sc = 0
                        break
                SCB2 += sc

            filename = 'saved_Data_2/'+name[i]+'.txt'
            f = open(filename, 'a')
            print(round(SCILP/times, 4),round(SCB1/times, 4),round(SCB2/times, 4),round(T/times, 4), file=f)
            f.close()
    return

