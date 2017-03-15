'''
采用generator实现8皇后
'''

def conflict(state,nextX):
    '''
    冲突检测函数，检测是否在同一列，同一对角线上
    '''
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0,nextY-i):
            return True
    return False


def queens(num = 8,state = ()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for reasult in queens(num,state + (pos,)):
                    yield (pos,) + reasult

print(list(queens(4)))
