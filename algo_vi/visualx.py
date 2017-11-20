#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: objs in this file contains varity of visualization process methods
# =================

from matplotlib import pyplot as plt
from matplotlib import animation
import abc

class Visual(object, metaclass=abc.ABCMeta):

    def __init__(self, *args, **kw):
        self.fig = plt.figure()
        # print(vars(self.fig))
        self.frames = 200
        self.interval = 1000

    # @abc.abstractmethod
    # def _animate(self, item):
    #     '''animate func for animation'''

class ViSort(Visual):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._data = kw.get('od', [])  # od --> ordereddict
        self.frames = len(self._data)

    def _animate(self, item):
        
        data = self._data[item]
        height = data.keys()
        left = list(range(len(height)))
        base_color = []
        for i in data.values():
            if i:
                base_color.append('green')
            else:
                base_color.append('red')
        print('left={}, height={}, color={}'.format(left, height, base_color))
        return plt.bar(left, height, width=0.8, color=base_color)

    def show(self):
        # fig = self.fig
        # print(self._animate)
        anis = animation.FuncAnimation(self.fig, 
                                        func=self._animate, 
                                        frames=self.frames, 
                                        interval=self.interval,
                                        blit=True)
        plt.show()