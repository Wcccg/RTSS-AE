This progream is intended to reproduce the main experimental results from the paper 'Priority Optimization for Autonomous Driving Systems to Meet End-to-End Latency Constraints'.

# Prerequisites
1. Python version 3.10 or higher with the following packages:
- Ghostscript, matplotlib
- networkx==2.6.3, pydot==1.4.2
- numpy>=1.22.0, schema>=0.7.5, PyYAML>=5.3.1
2. The latest Gurobi tool with the gurobipy package.
3. The latest graphviz tool.

# Experiment Instructions
To clear historical data and restart all experiments, please double-click the 'run python.bat' script. By default, the program runs a batch of 100 experiments per data point and will take approximately 8 hours to complete. Upon completion, the output text files for Figures 6 through 8 and Figures 9 through 15 will be saved in the 'saved_Data_1' and 'saved_Data_2' folders, respectively. The corresponding figures will be stored in the 'Pic1' and 'Pic2' folders.

# About Experiments Execution Time
Given the substantial time required to complete the experiments, we have prepared simplified versions by reducing the batch size. If you need to adjust the number of experiments per batch, modify the 'batchsize1' and 'batchsize2' parameters in 'main.py'. Note that the default batch size has been reduced from 1000 to 100 compared to the experiments described in the manuscript. Please be aware that further reduction in batch size may result in less accurate experimental results.

# Notes
If you have any questions or need further assistance, please contact me at the following email address:

22209229@mail.dlut.edu.cn

