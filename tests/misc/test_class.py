class A():
    param = 'Yahia Jad'
    param_2 = 'untoched'


class B(A):
    param = 'from class B'

x = B()
x.param = 'from Run'

print (x.param, x.param_2)