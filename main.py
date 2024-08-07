# Call functions from other files to conduct experiments and generate figures.
from DAG_Init import *
from ILP_Init import *
from ILP_Solve import *
from exp import *
from draw_1 import *
from draw_2 import *



if __name__ == '__main__':
    batchsize1 = 100
    batchsize2 = 100
    exp_1(batchsize1)
    draw_1()
    exp_2(batchsize2)
    draw_2()
    print('The experiment is complete, all figures are stored in the Pic1 and Pic2 folders.')