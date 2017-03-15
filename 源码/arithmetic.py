'''
模拟数学数组
'''
def checkIndex(key):
    if not isinstance(key,int):
        raise TypeError
    if key<0:
        raise IndexError

class ArithmeticSequence:
    def __init__(self,start=0,step=0):
        self.start = start
        self.step =step
        self.changed = {}
    '''
    保存变化的内容
    '''
    def __getitem__(self,key):
        checkIndex(key)
        try :
            return self.changed[key]
        except KeyError:
            return self.start+self.step*key

    def __setitem__(sef,key,value):
        checkIndex(key)
        self.changed[key] = value
