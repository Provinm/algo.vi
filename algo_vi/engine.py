#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: objs in this file performs like a hub, input a concret algorithm
#              dispatch it to corresponding visualization method 
# =================

import threading

import pyaudio
from sortx import Bubble, SelectionSort, InsertionSort, QuickSort, MergeSort
from visualx import ViSort
import abc
# from makesound import play_tone


class BaseEngine(metaclass=abc.ABCMeta):
    '''base engine for algo-vi project
    
    MAPPING: key-value for method: [get-data-cls, visual-cls]

    '''

    MAPPING = {
        'bubble_sort': [Bubble, ViSort],
        'selection_sort': [SelectionSort, ViSort],
        'insertion_sort': [InsertionSort, ViSort],
        'quick_sort': [QuickSort, ViSort],
        'merge_sort': [MergeSort, ViSort],
    }
    def __init__(self, func_name, **kw):
        
        self.g_cls, self.v_cls = BaseEngine.MAPPING.get(func_name, [None, None])
        
        self.ipt = []
        # extract relevant input data
        if func_name.endswith('sort'):
            self.ipt = kw.get('sort_lst', [])

    @abc.abstractmethod
    def show(self):
        ''''''
        
class Engine(BaseEngine):
    '''engine for algo-vi project
    this cls will automatically implements correct 'get-data' cls 
    and 'visualization' cls for incoming algorithm, no matter it is 
    a sort algo or others
    '''

    def __init__(self, func_name, **kw):
        super().__init__(func_name, **kw)
        self.kw = kw
        self.audio = pyaudio.PyAudio()

    def _get_data(self):
        '''implement assigned cls to get data which prepared for visualization'''
        dt = self.g_cls(self.ipt, **self.kw).operate()
        return dt

    def _draw_animation(self, dt):
        '''implement assigned cls to show animation for corresponding algorithm'''
        # dt = self._get_data()
        return self.v_cls(od=dt, **self.kw).show()

    # def _play_tone(self, tones):
    #     stream = self.audio.open(format=pyaudio.paFloat32,
    #                 channels=1, rate=44100, output=1)
        
    #     interval = self.kw.get('interval', 100)
    #     interval = interval // 1000
    #     fre = tones
    #     for f in fre:
    #         play_tone(stream, frequency=f)

    #     stream.close()
    #     self.audio.terminate()
        

    def show(self):
        '''visualization'''
        # return self._draw_animation().show()
        dt = self.g_cls(self.ipt, **self.kw).operate()
        self._draw_animation(dt)