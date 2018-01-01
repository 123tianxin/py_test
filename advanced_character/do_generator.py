#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#
#定义：
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b  =  b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break