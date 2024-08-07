# Plot Figure 6 to 8
import matplotlib.pyplot as plt

def draw_1():
    labelsize = 18
    parameters = [
        [5,10,15,20,25,30,35,40,45,50],
        [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
        [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
    ]
    R = [
        [0,4,8,12,16,20],
        [0,5,10,15,20,25],
        [0,4,8,12,16,20],
    ]
    files = ['N', 'Rate', 'U']
    labels = [r'$n_\pi$', r'$\alpha$',  r'$U_\pi$']
    for i in range(3):
        GAP = [[],[],[],[],[],[],[],[],[],[]]
        for j in range(10):
            filename = 'saved_Data_1\gap_'+files[i]+str(j)+'.txt'
            for line in open(filename):
                if len(line):
                    GAP[j].append(float(line)*100)
        plt.figure(figsize=(12, 5))
        plt.boxplot(GAP,notch=False, patch_artist=False, showmeans=False,widths=0.6,capwidths=0.3,showfliers=False,
                        boxprops={'linewidth': '1', 'color':'blue'},
                        medianprops = {'linewidth': '1', 'color':'red'},
                        meanprops = {'marker':'.', 'markerfacecolor':'black', 'markeredgecolor':'black','markersize':'4'},
                        whiskerprops={'linestyle': '--'},
                        flierprops = {'markersize':'7','marker':'+', 'markeredgecolor':'red'},
                        capprops={'linewidth': '1'})
        plt.xticks([1,2,3,4,5,6,7,8,9,10],parameters[i],fontname='Times New Roman',fontsize=labelsize)
        plt.xlabel(labels[i],fontname='Times New Roman', fontsize=labelsize, labelpad=-2)
        plt.ylabel('gap (%)',fontname='Times New Roman', fontsize=labelsize, labelpad=-2)
        plt.ylim(R[i][0],R[i][0]+(R[i][-1]-R[i][0])*1.1)
        plt.yticks(R[i],fontname='Times New Roman',fontsize=labelsize)
        plt.savefig('Pic1/'+files[i]+'.png',dpi=300)
