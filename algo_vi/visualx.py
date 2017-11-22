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
        # self.fig = plt.figure()
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
        # self.bar = plt.bar(range(8), [0]*8)
        

    def _ini_animate(self):
        data = self._data[0]
        height = data.keys()
        left = list(range(len(height)))
        base_color = []
        for i in data.values():
            if i:
                base_color.append('green')
            else:
                base_color.append('red')
        self.bar = plt.bar(left, height, color=base_color)
        self.text = []
        for patch in self.bar:
            i = plt.text(patch.get_x(), patch.get_height()+5, str(patch.get_height()))
            self.text.append(i)
            # self.text = plt.text()
        return self.bar


    def _animate(self, item):
        
        data = self._data[item+1]
        for patch, h, c, t in zip(self.bar, data.keys(), 
                               data.values(), self.text):
            patch.set_height(h)
            if c:
                patch.set_color('red')

            else:
                patch.set_color('green')
            
            t.set_text(str(h))

        return self.bar
            
        # height = data.keys()
        # tick_label = data.keys()
        # left = list(range(len(height)))
        # base_color = []
        # for i in data.values():
        #     if i:
        #         base_color.append('green')
        #     else:
        #         base_color.append('red')
        # print('left={}, height={}, color={}'.format(left, height, base_color))
        # return plt.bar(left, height, tick_label=tick_label, color=base_color, animated=True)

    def show(self):
        # fig = self.fig
        # print(self._animate)
        anis = animation.FuncAnimation(self.fig, 
                                        self._animate, 
                                        init_func=self._ini_animate,
                                        frames=self.frames, 
                                        interval=self.interval,
                                        blit=True)
        plt.show()