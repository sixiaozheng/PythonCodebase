"""
类和对象
    python 支持面向对象的三大特征:封装、继承和多态
    子类继承父类同样可以继承到父类的变量和方法
    类中各成员之间的定义顺序没有任何影响，各成员之间可以相互调用。
    类变量：属于类本身，定义类本身的状态数据
    实例变量：属于对象本身，定义对象包含的状态数据
    方法：定义该类的对象的行为或功能实现
    python是动态语言，所以类变量,实例变量,方法可以动态增加或删除。
    可以在类体中（类变量）或任何地方位新变量赋值来增加变量，
    通过del语句删除变量。

    创建对象后，对象的作用：
    操作对象的实例变量（访问实例变量的值、修改实例变量、添加实例变量、删除实例变量）
    调用对象的方法

"""

################################################################

class Person:
    """
    类的说明文档
    """
    # 类变量
    hair = 'black'
    # self 被绑定到构造方法初始化的对象
    def __init__(self,name='Charlie',age=8):
        # 实例变量
        self.name = name
        self.age = age
    
    def say(self,content):
        print(content)

    def speech(self, content):
        self.say(content)

p=Person()
# 访问
p.name
print(p.name)
# 修改
p.name="zsx"
print(p.name)
# 增加
p.skills='swimming'
print(p.skills)
# 删除
del p.name


################################################################

# 动态增加方法
def intro_func(self, content):
    print(content)

from types import MethodType
p.intro = MethodType(intro_func, p)
p.intro("life in everywhere")


################################################################

# self参数作为对象的默认引用，可以像访问普通变量一样访问这个self参数，
# 也可以把self参数当成实例方法的返回值
# 如果在某个方法中把self参数作为返回值，则可以多次连续调用同一个方法，从而使得代码更加简洁

class ReturnSelf:
    def grow(self):
        if hasattr(self, 'age'):
            self.age+=1
        else:
            self.age=1
        return self

rs = ReturnSelf()
rs.grow().grow().grow().grow().grow()
print(rs.age)

################################################################
# 类方法 静态方法
# 推荐通过类进行调用，也可以使用对象调用
# 类方法会自动绑定类方法的第一个参数，cls会自动绑定类本身
# 静态方法不会自动绑定
# 一般不需要使用类方法或静态方法，程序完全可以使用函数来代替类方法或静态方法。
# 但是在特殊的场景(比如使用工厂模式)下，类方法或静态方法也是不错的选择 

class Bird:
    @classmethod
    def fly(cls):
        print('class method', cls)
    
    @staticmethod
    def info(p):
        print('static method', p)
    
# 调用类方法，Bird类会自动绑定到第一个参数
Bird.fly()
# 调用静态方法，不会自动绑定，因此程序必须手动绑定第一个参数
Bird.info('crazyit')

b=Bird()
# 使用对象调用fly()类方法，其实依然还是使用类调用的
# 第一个参数依然被自动绑定到 Bird 类
b.fly()
# 使用对象调用 info ()静态方法，其实依然还是使用类调用的 
# 因此程序必须为第一个参数执行绑定
b.info('fkit')


################################################################

# @函数装饰器
# 1) 将被修饰的函数(函数 B)作为参数传给@符号引用的函数(函数 A)。 
# 2）将函数 B 替换(装饰)成上一步的返回值 
# 在被修饰函数之前、之后、抛出异常后增加某种处理逻辑的方式，就是其他编程语言中的 AOP (Aspect Orient Programming，面向切面编程)。

################################################################
# python的类就像命名空间，默认处于全局命名空间内，类体则处于则处于类命名空间内

# 类变量：通过类访问和修改类变量
# 允许使用对象访问类变量，本质依然是通过类名进行访问
# 不能通过对象修改类变量，实际上是定义新的实例变量

################################################################
# @property 修饰方法，使之成为属性

class Cell:
    # 使用@property修饰方法， 相当于为该属性设置getter方法
    @property
    def state(self):
        return self._state
    # 为 state 属性设置 setter 方法
    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'
    # 为 is_dead 属性设置 getter 方法
    # 只有 getter 方法的属性是只读属性
    @property
    def is_dead(self):
        return not self._state.lower()=='alive'

c=Cell()
c.state='Alive'
print(c.state)
print(c.is_dead)


################################################################
# 隐藏
# 为了隐藏类中的成员， Python玩了一个小技巧: 只要将Python类的成员命名为以__开头的，Python就会把它们隐藏起来。
# python 其实没有真正的隐藏机制，双下画线只是Python的一个小技巧: Python会“偷偷”地改变以__开头的方法名，会在这些方法名前添加_和类名 
class Test:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def __print_info(self):
        print(self.__name, self.__age)

# 通过添加 _Test 可以直接访问__开头的成员
t = Test('as', 3)
print(t._Test__name, t._Test__age)
t._Test__print_info()

# 无法直接访问__开头的成员
t = Test('as', 3)
print(t.__name, t.__age)
t.__print_info()


################################################################
# 继承
# 继承的作用一一子类扩展(继承〉了父类， 将可以继承得到父类定义的方法，这样子类就可复用父类的方法了
# 在python不推荐使用多继承

class SubClass(SuperClass1, SuperClass2):
    pass

# 重写
# 子类包含与父类同名的方法的现象被称为方法重写( Override)，也被称为方法覆盖。
# 可以说子类重写了父类的方法，也可以说子类覆盖了父类的方法。
# 如何调用父类中被重写的方法？

class BaseClass: 
    def foo(self):
        print('父类中定义的 foo方法')
class SubClass(BaseClass):
    # 重写父类的 foo方法
    def foo(self):
        print('子类重写父类中的 foo方法')
    def bar(self):
        print('执行 bar 方法')
        # 直接执行 foo 方法，将会调用子类重写之后的 foo ()方法
        self.foo() 
        # 使用类名调用实例方法〈未绑定方法)调用父类被重写的方法 
        BaseClass.foo(self)
sc=Subclass()
sc.bar()

# Python要求: 如果子类重写了父类的构造方法，那么子类的构造方法必须调用父类的构造方法
# Manager 继承了 Employee、 Customer 
class Manager(Employee, Customer):
    #重写父类的构造方法
    def __init__(self, salary, favorite, address):
        print('一Manager 的构造方法一')
        # 通过 super()函数调用父类的构造方法
        super().__init__(salary=salary, favorite=favorite, address=address)
        # 与上一行代码的效果相同
        super(Manager, self).__init__(salary) 
        # 使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, address)

# 创建 Manager 对象
m = Manager(25000, 'IT 产品', '广州')
m.work() #1
m.info() #2