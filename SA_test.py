# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: gyy
import math
from random import random
import matplotlib.pyplot as plt

def func(x, y,z):
    # num = 6.452 * (x + 0.125 * y) * (math.cos(x) - math.cos(2 * y)) ** 2
    # den = math.sqrt(0.8 + (x - 4.2) ** 2 + 2 * (y - 7) ** 2)
    num=
    return - (num / den + 3.226 * y)

class SimulateAnnealing:
    def __init__(self, func, iter=10, T0=100, Tf=1e-8, alpha=0.99):
        """
        Annealing parameters
        :param iter: Number of internal cycles
        :param T0: Initial temperature
        :param Tf: Final temperature
        :param alpha: Cooling factor
        """
        self.func = func
        self.iter = iter
        self.alpha = alpha
        self.T0 = T0
        self.Tf = Tf
        self.T = T0
        self.x = [random() * 10 for i in range(iter)]
        self.y = [random() * 10 for i in range(iter)]
        self.history = {'f': [], 'T': []}

    def generate_new(self, x, y):
        while True:
            x_new = x + self.T * (random() - random())
            y_new = y + self.T * (random() - random())
            if (0 <= x_new <= 10) & (0 <= y_new <= 10):
                break
        return x_new, y_new

    def Metrospolis(self, f, f_new):
        if f_new <= f:
            return 1
        else:
            p = math.exp((f - f_new) / self.T)
            if random() < p:
                return 1
            else:
                return 0

    def get_optimal(self):
        f_list = []
        for i in range(self.iter):
            f = self.func(self.x[i], self.y[i])
            f_list.append(f)
        f_best = min(f_list)
        idx = f_list.index(f_best)
        return - f_best, idx

    def plot(self, xlim=None, ylim=None):
        plt.plot(sa.history['T'], sa.history['f'])
        plt.title('Simulate Annealing')
        plt.xlabel('Temperature')
        plt.ylabel('f value')
        if xlim:
            plt.xlim(xlim[0], xlim[-1])
        if ylim:
            plt.ylim(ylim[0], ylim[-1])
        plt.gca().invert_xaxis()
        plt.show()

    def run(self):
        count = 0
        # annealing
        while self.T > self.Tf:
            # iteration
            for i in range(self.iter):
                f = self.func(self.x[i], self.y[i])
                x_new, y_new = self.generate_new(self.x[i], self.y[i])
                f_new = self.func(x_new, y_new)
                if self.Metrospolis(f, f_new):
                    self.x[i] = x_new
                    self.y[i] = y_new
            # save to history
            ft, _ = self.get_optimal()
            self.history['f'].append(ft)
            self.history['T'].append(self.T)
            # cooling
            self.T = self.T * self.alpha
            count += 1
        # get optimal solution
        f_best, idx = self.get_optimal()
        print(f"F={f_best}, x={self.x[idx]}, y={self.y[idx]}")

if __name__ == '__main__':
    # run
    sa = SimulateAnnealing(func)
    sa.run()
    # plot
    sa.plot()
    sa.plot([0, 1], [99, 100])
    # result:
    # F=99.99522530386253, x=6.090887224877577, y=7.798623593311333
