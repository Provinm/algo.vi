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
        # basic matplotlib configuration
        self.fig, self.ax = plt.subplots()
        self.kw = kw

        # fig set
        self._fig_conf()

        # axis set
        self._axis_conf()

        # basic animation config
        self.frames = kw.get('frames', 200)
        self.interval = kw.get('interval', 1000)

    def _fig_conf(self):
        '''as the method name says'''
        facecolor = self.kw.get('facecolor', 'white')
        title = self.kw.get('title', '')
        self.fig.set_facecolor(facecolor)
        plt.title(title)

    def _axis_conf(self):
        '''set axis paras, default is off'''
        _axis = self.kw.get('axis', 'off')
        self.ax.axis(_axis)


class ViSort(Visual):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._data = kw.get('od', [])  # od --> ordereddict
        self.frames = len(self._data)

    def _animate(self, item):
        
        data = self._data[item]
        height = data.keys()
        tick_label = data.keys()
        print(tick_label)
        left = list(range(len(height)))
        base_color = []
        for i in data.values():
            if i:
                base_color.append('green')
            else:
                base_color.append('red')
        # for x, y in enumerate(height):
        #     self.ax.text(x, y+5, str(y), ha='center', va='bottom')

        # print('left={}, height={}, color={}'.format(left, height, base_color))
        return plt.bar(left, height, tick_label=tick_label, color=base_color, animated=True)

    def show(self):
        # fig = self.fig
        # print(self._animate)
        anis = animation.FuncAnimation(self.fig, 
                                        func=self._animate, 
                                        frames=self.frames, 
                                        interval=self.interval,
                                        blit=True)
        plt.show()