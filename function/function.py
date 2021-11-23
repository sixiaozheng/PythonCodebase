"""
函数
    函数的目的：代码复用
    函数，就是指为一段实现特定功能的代码“取”一个名字，以后即可通过该名字来执行(调用)该函数。

    输入：0个或多个参数
    返回：0个或多个值

    定义函数的语法：
    def function_name(形参列表):
        pass
        [return [返回值]]

"""


def sum_and_avg(a, b, message="sum and average", *args, **kwargs):
    """
    说明文档：求和 均值函数
    a: 位置参数
    b: 位置参数
    message="sum and average": 默认参数
    *args: 可变参数，类型：tuple
    **kwargs: 可变关键字参数，类型：dict
    """
    print(message)
    print(args, type(args), len(args))
    print(kwargs, type(kwargs), len(kwargs))
    c = a+b
    for n in args:
        c += n
    for k, v in kwargs.items():
        c += v
    return c, c/(2+len(args)+len(kwargs))  # 多个返回值被封装成 tuple


print('#'*30)
# 说明文档
# help(sum_and_avg)
print(sum_and_avg.__doc__)

# 返回值
# res 是一个 tuple
res = sum_and_avg(1, 2)
# 序列解包
s, avg = sum_and_avg(1, 2)

# 参数
# 位置参数
print(sum_and_avg(1, 2))
# 关键字参数
print(sum_and_avg(a=1, b=2))
print(sum_and_avg(1, b=2))
# 可变参数 *args
print(sum_and_avg(1, 2, "可变参数 *args", 3, 4, 5, 6, 7))
# 可变关键字参数 **kwargs
print(sum_and_avg(1, 2, "可变关键字参数 **kwargs", 3,
      4, 5, 6, 7, aa=8, bb=9, cc=10, dd=11))
print(sum_and_avg(1, 2, aa=8, bb=9, cc=10, dd=11))
# 参数解包
# 把list 或 tuple 通过 * 解包后传递给形参，然后*args将对应参数收集成tuple
my_args = [1, 2, "解包 可变参数 *args", 3, 4, 5, 6, 7]
print(sum_and_avg(*my_args))
# 把dict通过 ** 解包后传递给形参，然后**kwargs将对应参数收集成dict
my_args = (1, 2, "解包 可变关键字参数 **kwargs", 3, 4, 5, 6, 7)
my_dict = {"aa": 8, "bb": 9, "cc": 10, "dd": 11}
print(sum_and_avg(*my_args, **my_dict))

"""
参数传递机制
python是 值传递，即传入副本（复制品），所以在函数中对传入副本进行操作，不影响函数外的参数
对于可变对象list或dict，传入的是对象引用的副本，在函数中对传入的list或dict进行操作，会影响
可变对象本身，不影响函数外的对象引用。
如果需要让函数修改某些数据，可以把数据包装成list 或 dict等可变对象，然后将list或dict作为参数传入函数
"""


"""
变量作用域
globals(): 返回全局范围内所有变量组成的变量字典
locals(): 返回当前局部范围内所有变量组成的变量字典
vars(object): 返回指定对象范围内所有变量组成的变量字典，如果不指定object，vars() 和 locals() 作用一样
一般来说，使用 locals()和 globals()获取的“变量字典”只应该被访问，不应该被修改。但实际上，都可以被修改。
对globals()的字典进行修改会改变全局变量本身
对locals()的字典进行修改不会改变局部变量本身
"""


print('#'*30)
name = 'haha'


def test():
    # global 语句声明全局变量，以便后面修改全局变量
    global name
    print(name)
    name = 'hihi'


test()
print(name)

"""
局部函数
函数将局部函数返回，且使用变量保存了返回的局部函数，则局部函数的作用域被扩大，
"""
print('#'*30)


def foo():
    name = "Charlie"

    def bar():
        # nonlocal 声明访问当前函数所在函数内的局部变量
        nonlocal name
        print(name)
        name = 'Mark'
        print(name)
    bar()


foo()


"""
函数的高级内容
函数可以赋值给变量，作为参数，作为函数的返回值
1. 函数赋值给变量后，可以使用变量调用函数
2. 当希望函数被调用时某些代码可以动态变化时，可以将动态变化部分封装成函数后作为参数传入。也就是函数中哪里需要变化，哪里就转化为参数
3. 将函数作为其他函数的返回值，可以实现根据参数，返回不同的参数
"""


"""
lambda表达式
    可作为 表达式，函数参数，函数返回值。可以使程序更加简洁
    如果函数名的生命周期短，可以考虑使用lambda表达式来简化局部函数的写法
    lambda 表达式只是单行函数的简化版本，因此 lambda 表达式的功能比较简单
    语法格式：
        lambda [parameter_list]:表达式
        eg：
            lambda : 1+2+3
            lambda x : x**2
            lambda x,y: x*y
"""
print('#'*30)
x = map(lambda x: x*x, range(10))
print(list(x))
