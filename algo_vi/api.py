#coding=utf-8
# =================
# author: zhouxin
# start_date： 171115
# description: apis for external
# =================

from engine import Engine
import inspect


def bubble_sort(lst, **kw):
    '''bubble sort api 
    
    '''
    func_name = inspect.stack()[0][3]
    kw.update({'sort_lst': lst})
    e = Engine(func_name, **kw)
    e.show()

if __name__ == '__main__':
    import random
    lst = random.sample(range(100), 8)
    random.shuffle(lst)

    bubble_sort(lst)
