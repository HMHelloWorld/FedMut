import matplotlib.pyplot as plt
import numpy as np
import datetime

def plot(data, ylabel):
        plt.figure()   
        marker = ['^','v','o','s','x']
        # linestyle = [':', '--', '-', '-.', 'solid', 'dashed', 'dashdot', 'dotted']
        # color = ['gray', 'black']
        i = 0 
        # plt.figure(figsize=(11, 6)) #ps
        plt.figure(figsize=(10, 6)) #new
        # plt.tick_params(labelsize=18)
        plt.yticks(fontproperties = 'Times New Roman', size = 16)
        plt.xticks(fontproperties = 'Times New Roman', size = 16)
        # plt.rc('font',family='Times New Roman') 
        for label in data:
            arr1 = data[label][0:len(data[label]):1]
            plt.plot(range(0,len(data[label]),1), arr1,  label=label, linewidth=1)  #linestyle = linestyle[i],
            # x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
            # plt.plot(x, arr1,  label=label, linewidth=1)
            # plt.plot(range(0, 500, 1), arr1, label=label, linestyle='-', linewidth=0.8, marker = marker[i], markersize = 2, markevery=10)
            # plt.plot(range(len(data[label])), data[label], label=label, linestyle=':', linewidth=1)
            i = i + 1
            print(arr1)
        font1 = {'family' : 'Times New Roman', 'weight' : 'normal', 'size' : 16, }
        plt.ylabel(ylabel, font1)
        plt.xlabel("Communication Round (#)", font1)
        # plt.xlabel("The Threshold Value", font1)
        plt.grid(ls='--')
        box = plt.gca().get_position()
        plt.gca().set_position([box.x0, box.y0, box.width, box.height*0.9]) #code_dim
        # for a, b in zip(x, arr1):
        #     plt.text(a, b, b, ha='center', va='bottom', fontsize=16)
        
        # plt.legend(loc=9, bbox_to_anchor=(0.5, 2.4),ncol=2, fontsize=18, columnspacing=0.5)
        # plt.gca().set_position([box.x0, box.y0, box.width, box.height*0.8]) #ps
        # plt.legend(loc=9, bbox_to_anchor=(0.44, 1.4),ncol=3, fontsize=24, columnspacing=0.5) #ps
        # plt.legend(fontsize=20)
        # plt.gca().set_position([box.x0, box.y0, box.width, box.height*0.7])  #code_dim
        plt.legend(loc=9, bbox_to_anchor=(0.5, 1.15),ncol=4, prop={'family' : 'Times New Roman', 'size'   : 16}, columnspacing=1)  #code_dim
        # plt.legend(loc=9, bbox_to_anchor=(0.5, 1.5),ncol=3, fontsize=20, columnspacing=0.5)  #new
        plt.savefig('./output/5/0.5/ling.pdf')

if __name__ == '__main__':
    labels = []
    items2 = []
    data = {}
    i=0
    with open(r'./output/5/0.5/100_10.txt', 'r') as f:
        for item in f.readlines():
            item1 = np.array(item.split())
            label = item1[0]
            labels.append(label)
            item2 = np.delete(item1, 0).astype('float32')
            items2.append(item2)
    f.close()


    for label in labels:
        data[label] = items2[i]
        i = i+1

    plot(data, 'Test Accuracy (%)')
    
