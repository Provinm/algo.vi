#coding=utf-8
# =================
# author: zhouxin
# start_date： 171115
# description: apis for external
# =================

from engine import Engine
from functools import wraps


# sort algorithm decorator
def sort_algo(func):
    @wraps(func)
    def inner(*args, **kw):
        func_name = func.__name__
        kw.update({'sort_lst': lst})
        kw.setdefault('title', func_name)
        e = Engine(func_name, **kw)
        e.show()
        
    return inner

@sort_algo
def bubble_sort(lst, **kw):
    '''bubble sort api'''
    pass

@sort_algo
def selection_sort(lst, **kw):
    pass

@sort_algo
def insertion_sort(lst, **kw):
    pass

def quick_sort(lst, **kw):
    pass

def merge_sort(lst, **kw):
    pass

if __name__ == '__main__':
    import random
    lst = random.sample(range(100), 8)
    random.shuffle(lst)

    # bubble_sort(lst)
    # selection_sort(lst)
    insertion_sort(lst)
