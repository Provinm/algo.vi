#coding=utf-8
# =================
# author: zhouxin
# start_date： 171112
# description: objs in this file contains varity of sort algorithms
#              such as quick sort , selection sort and so on 
# =================

from collections import OrderedDict
from utils import VaList


class BaseSort(object):
    '''basesort class 
    '''

    # MAX_LEN = 10
    lst = VaList()
    def __init__(self, raw_lst):
        # raw_lst = list(raw_lst)
        # is_valid = all([isinstance(i, (int, float)) for i in raw_lst])
        # assert is_valid, 'invalid data provided'
        # if len(raw_lst) > BaseSort.MAX_LEN:
        #     print('the lst exceeds max length, automatically intercepts \
        #            first 10 items')
        #     raw_lst = raw_lst[:BaseSort.MAX_LEN]
        self.lst = raw_lst

    # ordereddict container for O(n^2) sort
    def od_dct(self, ini_idx, match_idx, lst):
        dct = OrderedDict([(k, False) for k in lst])
        dct[lst[ini_idx]] = True
        dct[lst[match_idx]] = True

        return dct


class Bubble(BaseSort):
    
    def __init__(self, raw_lst):
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
        for i in range(length):
            for j in range(i+1, length):
                
                res.append(self.od_dct(i, j, b_lst))
                if b_lst[i] > b_lst[j] and not reverse:
                    b_lst[i], b_lst[j] = b_lst[j], b_lst[i]
                
                elif b_lst[i] < b_lst[j] and reverse:
                    b_lst[i], b_lst[j] = b_lst[j], b_lst[i]

                res.append(self.od_dct(i, j, b_lst))

        return res

    def operate(self, reverse=False):
        
        return self._bubble(self.lst, reverse)


if __name__ == '__main__':
    import random
    lst = list(range(1, 6))
    random.shuffle(lst)
    bsort = Bubble(lst)
    r = bsort.operate(True)
    for i in r:
        print(i)