import numpy as np
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

class Logger():
    def __init__(self, initial):
        self.log = {}
        for item in initial.keys():
            for level in initial[item].keys():
                self.log['desired', item, level] = []
                self.log['current', item, level] = []


    def log_data(self, desired, current):
        for item in desired.keys():
            for level in desired[item].keys():
                self.log['desired', item, level].append(desired[item][level])
                self.log['current', item, level].append(current[item][level])

    def initialize_plot(self, frequency=1):
        self.frequency = frequency
        self.plot_info = [
            {'axis': 0, 'batch': 'desired', 'item': 'com', 'level': 'pos', 'dim': 0, 'color': 'blue' , 'style': '-' },
            {'axis': 0, 'batch': 'current', 'item': 'com', 'level': 'pos', 'dim': 0, 'color': 'blue' , 'style': '--'},
            {'axis': 0, 'batch': 'desired', 'item': 'zmp', 'level': 'pos', 'dim': 0, 'color': 'green', 'style': '-' },
            {'axis': 0, 'batch': 'current', 'item': 'zmp', 'level': 'pos', 'dim': 0, 'color': 'green', 'style': '--'},
            {'axis': 1, 'batch': 'desired', 'item': 'com', 'level': 'pos', 'dim': 1, 'color': 'blue' , 'style': '-' },
            {'axis': 1, 'batch': 'current', 'item': 'com', 'level': 'pos', 'dim': 1, 'color': 'blue' , 'style': '--'},
            {'axis': 1, 'batch': 'desired', 'item': 'zmp', 'level': 'pos', 'dim': 1, 'color': 'green', 'style': '-' },
            {'axis': 1, 'batch': 'current', 'item': 'zmp', 'level': 'pos', 'dim': 1, 'color': 'green', 'style': '--'},
            {'axis': 2, 'batch': 'desired', 'item': 'com', 'level': 'pos', 'dim': 2, 'color': 'blue' , 'style': '-' },
            {'axis': 2, 'batch': 'current', 'item': 'com', 'level': 'pos', 'dim': 2, 'color': 'blue' , 'style': '--'},
            {'axis': 2, 'batch': 'desired', 'item': 'zmp', 'level': 'pos', 'dim': 2, 'color': 'green', 'style': '-' },
            {'axis': 2, 'batch': 'current', 'item': 'zmp', 'level': 'pos', 'dim': 2, 'color': 'green', 'style': '--'},
        ]

        plot_num = np.max([item['axis'] for item in self.plot_info]) + 1
        self.fig, self.ax = plt.subplots(plot_num, 1, figsize=(6, 8))

        labels = ['x-pos [m]', 'y-pos [m]', 'z-pos [m]']
        for i in range(plot_num):
            self.ax[i].set_ylabel(labels[i])
            self.ax[i].grid(True)
        self.ax[-1].set_xlabel('time [steps]')
        self.fig.suptitle('real-time CoM and ZMP tracking', fontsize=14)

        self.lines = {}
        for item in self.plot_info:
            key = item['batch'], item['item'], item['level'], item['dim']
            self.lines[key], = self.ax[item['axis']].plot([], [], color=item['color'], linestyle=item['style'])
        
        #self.ax[0].legend(['desired CoM', 'current CoM', 'desired ZMP', 'current ZMP'], loc='upper right', fontsize='small')
        legend_elems = [
            Line2D([0], [0], color='blue', linestyle='-', label='CoM Desired'),
            Line2D([0], [0], color='blue', linestyle='--', label='CoM Current'),
            Line2D([0], [0], color='green', linestyle='-', label='ZMP Desired'),
            Line2D([0], [0], color='green', linestyle='--', label='ZMP Current')
        ]
        self.fig.legend(handles=legend_elems, loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=4, fontsize='small', frameon=False)
        self.fig.subplots_adjust(top=0.88)

        plt.ion()
        plt.show()

    def update_plot(self, time):
        if time % self.frequency != 0:
            return

        for item in self.plot_info:
            trajectory_key = item['batch'], item['item'], item['level']
            trajectory = np.array(self.log[trajectory_key]).T[item['dim']]
            line_key = item['batch'], item['item'], item['level'], item['dim']
            self.lines[line_key].set_data(np.arange(len(trajectory)), trajectory)

        # set limits
        for i in range(len(self.ax)):
            self.ax[i].relim()
            self.ax[i].autoscale_view()
            
        # redraw the plot
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()