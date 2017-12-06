#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: objs in this file contains varity of visualization process methods
# =================

from matplotlib import pyplot as plt
from matplotlib import animation
import abc

from settings import COLOR_MAPPING

class Visual(object, metaclass=abc.ABCMeta):

    def __init__(self, *args, **kw):
        # basic matplotlib configuration
        self.fig, self.ax = plt.subplots()
        # self.fig = plt.figure()
        self.kw = kw

        # fig set
        self._fig_conf()

        # axis set
        self._axis_conf()

        # basic animation config
        self.frames = kw.get('frames', 200)
        self.interval = kw.get('interval', 500)

    def _fig_conf(self):
        '''as the method name says'''
        facecolor = self.kw.get('facecolor', 'white')
        title = self.kw.get('title', '')
        self.fig.set_facecolor(facecolor)
        plt.title(title)

    def _axis_conf(self):
        '''set axis paras'''
        self.ax.get_yaxis().set_visible(False)
        self.ax.set_frame_on(False)

class ViSort(Visual):

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._data = kw.get('od', [])  # od --> ordereddict
        self.frames = range(1, len(self._data))
        
    def _ini_animate(self):
        '''init func for animation'''
        data = self._data[0]
        length = len(data)

        height = data.keys()
        left = list(range(length))
        color = data.values()
        self.ax.set_xticklabels([0]+list(data.keys()))
        self.bar = plt.bar(left, height, color=color)
        return self.bar

    def _animate(self, item):
        '''animation func'''
        data = self._data[item]
        for patch, h, c in zip(self.bar, data.keys(), 
                               data.values()):
            patch.set_height(h)
            patch.set_color(c)
        self.ax.set_xticklabels([0]+list(data.keys()))
        return self.bar

    def show(self):
        '''show animation'''
        anis = animation.FuncAnimation(self.fig, 
                                        self._animate, 
                                        init_func=self._ini_animate,
                                        frames=self.frames, 
                                        interval=self.interval,
                                        repeat=False
                                        )
        plt.show()