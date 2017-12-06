#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: objs in this file contains varity of sort algorithms
#              such as quick sort , selection sort and so on 
# =================

from collections import OrderedDict
from utils import VaList
import abc

from settings import COLOR_MAPPING

class BaseSort(object, metaclass=abc.ABCMeta):
    '''basesort class '''
    # MAX_LEN = 10
    lst = VaList()
    def __init__(self, raw_lst):
        self.lst = raw_lst

    # ordereddict container for O(n^2) sort
    def od_dct(self, ini_idx, match_idx, lst):
        # print(ini_idx, match_idx, lst)
        tem = []
        for idx, item in enumerate(lst):
            level = 'OUT1'
            if idx == ini_idx:
                level = 'IN1'
            elif idx == match_idx:
                level = 'IN2'

            tem.append((item, COLOR_MAPPING.get(level)))
        
        return OrderedDict(tem)

    @abc.abstractmethod
    def operate(self):
        ''''''


class Bubble(BaseSort):
    
    def __init__(self, raw_lst, **kw):
        # raw_lst = kw.get('sort_list', [])
        self.reverse = kw.get('reverse', False)
        super(Bubble, self).__init__(raw_lst)


    def _bubble(self, b_lst, reverse=False):
        '''code for bubble sort 
        :para b_lst: type: sequence, the list data waited to be sorted
        :para reverse, type: bool, the sort order is ascending if reverse is False
        or descending.
        :rtype : [OrderedDict(), OrderedDict()]
        '''
        length = len(b_lst)
        res = []
        for i in range(length-1):
            for j in range(length-1-i):
                
                res.append(self.od_dct(j, j+1, b_lst))
                if b_lst[j+1] > b_lst[j] and reverse:
                    b_lst[j+1], b_lst[j] = b_lst[j], b_lst[j+1]
                
                elif b_lst[j+1] < b_lst[j] and not reverse:
                    b_lst[j+1], b_lst[j] = b_lst[j], b_lst[j+1]

                res.append(self.od_dct(j, j+1, b_lst))

        res.append(self.od_dct(-1, -1, b_lst))
        return res

    def operate(self):
        
        return self._bubble(self.lst, self.reverse)

class SelectionSort(BaseSort):
    def __init__(self, raw_lst, **kw):
        self.reverse = kw.get('reverse', False)
        super().__init__(raw_lst)

    def od_dct(self, ini_idx, com_idx, match_idx, lst):
        tem = []
        for i, item in enumerate(lst):
            level = 'OUT1'
            if i == ini_idx:
                level = 'IN2'
            elif i == com_idx:
                level = 'IN1'
            elif i == match_idx:
                level = 'IN3'
            tem.append((item, COLOR_MAPPING.get(level)))
        return OrderedDict(tem)

    def _select(self, s_lst, reverse=False):
        length = len(s_lst)
        res = []
        for idx in range(length):
            
            sp_idx = idx
            for j in range(idx+1, length):
                
                res.append(self.od_dct(idx, sp_idx, j, s_lst))
                if s_lst[j] > s_lst[sp_idx] and reverse:
                    sp_idx = j 
                elif s_lst[j] < s_lst[sp_idx] and not reverse:
                    sp_idx = j
                
            s_lst[idx], s_lst[sp_idx] = s_lst[sp_idx],  s_lst[idx]
            res.append(self.od_dct(idx, sp_idx, j, s_lst))
        res.append(self.od_dct(-1, -1, -1, s_lst))
        return res

    def operate(self):
        return self._select(self.lst, self.reverse)

class InsertionSort(BaseSort):
    
    def __init__(self, raw_lst, **kw):
        
        self.reverse = kw.get('reverse', False)
        super().__init__(raw_lst)

    def _insert(self, i_lst, reverse=False):
        length = len(i_lst)
        res = []
        for i in range(1, length):
            idx = i
            while idx:
                res.append(self.od_dct(idx, idx-1, i_lst))
                if i_lst[idx] < i_lst[idx-1] and not reverse:
                    i_lst[idx], i_lst[idx-1] = i_lst[idx-1], i_lst[idx]
                elif i_lst[idx] > i_lst[idx-1] and reverse:
                    i_lst[idx], i_lst[idx-1] = i_lst[idx-1], i_lst[idx]
                else:
                    break
                res.append(self.od_dct(idx, idx-1, i_lst))
                idx -= 1
        res.append(self.od_dct(-1, -1, i_lst))
        return res

    def operate(self):
        return self._insert(self.lst, self.reverse)


class QuickSort(BaseSort):
    
    def __init__(self, raw_lst, **kw):
            
        self.reverse = kw.get('reverse', False)
        super().__init__(raw_lst)

    def _quick(self, q_lst, reverse=False):
        
        if not q_lst or len(q_lst) == 1:
            return q_lst

        pivot = q_lst[0]
        left = []
        right = []
        for i in q_lst[1:]:
            if pivot > i:
                left.append(i)
            else:
                right.append(i)

        return self._quick(left, reverse) + [pivot] + self._quick(right, reverse)

    def operate(self):
        return self._quick(self.lst, self.reverse)
        


if __name__ == '__main__':
    import random
    lst = list(range(1, 6))
    random.shuffle(lst)
    print(lst)
    bsort = QuickSort(lst, reverse=True)
    r = bsort.operate()
    print(r)
    # for i in r:
    #     print(i)