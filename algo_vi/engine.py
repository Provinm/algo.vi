#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: objs in this file performs like a hub, input a concret algorithm
#              dispatch it to corresponding visualization method 
# =================
from sortx import Bubble
from visualx import ViSort
import abc

class BaseEngine(metaclass=abc.ABCMeta):
    
    MAPPING = {
        'bubble_sort': [Bubble, ViSort]
    }
    def __init__(self, func_name, **kw):
        
        self.g_cls, self.v_cls = BaseEngine.MAPPING.get(func_name, [None, None])

        # assert self.g_cls, 'no corresponding class has been found'
        self.ipt = []
        # extract relevant input data
        if func_name.endswith('sort'):
            self.ipt = kw.get('sort_lst', [])

        # print(self.ipt)
        

    @abc.abstractmethod
    def show(self):
        ''''''

        
class Engine(BaseEngine):

    def __init__(self, func_name, **kw):
        super().__init__(func_name, **kw)
        self.kw = kw

    def _get_data(self):
        # print(self.kw)
        dt = self.g_cls(self.ipt, **self.kw).operate()
        return dt

    def _draw_animation(self):
        
        dt = self._get_data()

        return self.v_cls(od=dt, **self.kw)

    def show(self):
        
        return self._draw_animation().show()