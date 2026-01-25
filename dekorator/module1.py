def yskorenie(v0, v, t):
    if t==0:
        raise ValueError('Значение должно быть положительным')
    a = (v - v0) / t
    print('Ускорение:', a, 'м/с2')
    return a

def distance(f):

    def wrapper(v0, v, t):
        res = f(v0, v, t)
        a = res
        s = ((v0 + v)/2)*t
        print('Расстояние пройденное объектом:', s, 'м')
        return res
    return wrapper

@distance
def yskorenie(v0, v, t):
    a = (v - v0) / t
    print('Ускорение:', a,' м/с2')
    return a

result = yskorenie(10, 20, 2)