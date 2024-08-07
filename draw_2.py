# Plot Figure 9 to 15
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def draw_2():
    labelsize = 18
    ticksize = 18
    barwidth = 0.75
    files = ['N','Ne','Ns','Degree', 'U','Rate', 'Bound',]
    parameters = [
        [10,15,20,25,30,35,40,45,50,55],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,7,8,9,10],
        [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.1],
        [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],
        [0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0,1.05,1.1]
    ]
    R = [0,20,40,60,80,100]
    times = [
        [0,3,6,9,12,15],
        [0,0.5,1.0,1.5,2.0, 2.5],
        [0,0.5,1.0,1.5,2.0, 2.5],
        [0,1,2,3,4,5],
        [0,0.5,1.0,1.5,2.0, 2.5],
        [0,0.5,1.0,1.5,2.0, 2.5],
        [0,0.5,1.0,1.5,2.0, 2.5],
    ]
    labels = [r'$n$', r'$n_s$', r'$n_c$', r'$D$', r'$U$', r'$\omega$', r'$\mu$']
    pos = np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5])
    for i in range(7):
        sc = [[],[],[],[]]
        t = []
        RR = 1.25
        filename = 'saved_Data_2/'+files[i]+'.txt'
        for line in open(filename):
            data = line.split()
            if len(data):
                sc[0].append(float(data[0])*100)
                sc[1].append(float(data[1])*100)
                sc[2].append(float(data[2])*100)
                t.append(float(data[3]))
        
        fig, ax1 = plt.subplots(figsize=(10,5.5))
        ax2 = ax1.twinx()  
        ax1.set_ylabel('Succ Rate (%)',fontname='Times New Roman', fontsize=labelsize,labelpad=-5)
        ax1.set_ylim(0,RR*R[-1])
        ax1.set_yticks(R)
        ax1.set_yticklabels(R,fontname='Times New Roman', fontsize=ticksize)
        ax1.set_xlim(0,10)
        ax1.set_xticks(pos)
        ax1.set_xticklabels(parameters[i],fontname='Times New Roman', fontsize=ticksize)
        ax1.bar(pos - 0.33 * barwidth, sc[2], width = 0.33 * barwidth, color = 'green')
        ax1.bar(pos , sc[1], width = 0.33 * barwidth, color = 'orange')
        ax1.bar(pos + 0.33 * barwidth, sc[0], width = 0.33 * barwidth, color = 'red')
        ax1.set_xlabel(labels[i],fontname='Times New Roman', fontsize=labelsize, labelpad=-2)
        ax2.set_ylabel('Comp Time (s)',fontname='Times New Roman', fontsize=labelsize, labelpad=5)
        ax2.set_ylim(times[i][0],times[i][0]+(times[i][-1]-times[i][0])*RR)
        ax2.set_yticks(times[i])
        ax2.set_yticklabels(times[i],fontname='Times New Roman', fontsize=ticksize)
        ax2.plot(pos,t,c='black',marker='^', linewidth=2)
        plt.savefig('Pic2/'+files[i]+'.png',dpi=300)
        
