#!/usr/bin/python
#coding:utf-8

#####面向对象三大特性:封装、继承、多态@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#继承 __init__    派生类默认不继承基类__init__，需要用super声明
class AA(object):
    def __init__(self):
        self.name = "nick"
 
class BB(AA):
    def __init__(self):
        self.age = 18
        super(BB, self).__init__()  #super首先找到BB的父类AA，然后把类BB的对象self转换为类AA的对象，然后“被转换”的类AA对象调用自己的__init__函数
        # AA.__init__(self)          #指定运行AA中__init__，不推荐
 
obj = BB()
print(obj.__dict__)

# 多继承：
# Python的类可以继承多个类，Java和C#中则只能继承一个类
# Python3的类继承多个类的寻找方法的方式，Python 3中没有经典类、新式类之分
# 多继承
class A():
    def f1(self):
        print("A")
 
class B(A):
    def f(self):
        print("B")
 
class C(A):
    def f(self):
        print("C")
 
class D(B):
    def f(self):
        print("D")
 
class E(C):
    def f1(self):
        print("E")
 
class F(D,E):
    def f(self):
        print("F")
 
f1 = F()
f1.f1()

# 当类是经典类时，多继承情况下，会按照深度优先方式查找
# 当类是新式类时，多继承情况下，会按照广度优先方式查找
#经典类多继承
class ZD:
    def bar(self):
        print 'ZD.bar'
class ZC(ZD):
    def bar(self):
        print 'ZC.bar'
class ZB(ZD):
    def bar(self):
        print 'ZB.bar'
class ZA(ZB, ZC):
    def bar(self):
        print 'ZA.bar'
a = ZA()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去D类中找，如果D类中么有，则继续去C类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> D --> C
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

#新式类多继承
class YD(object):
    def bar(self):
        print 'YD.bar'
class YC(YD):
    def bar(self):
        print 'YC.bar'
class YB(YD):
    def bar(self):
        print 'YB.bar'
class YA(YB, YC):
    def bar(self):
        print 'YA.bar'
a = YA()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中么有，则继续去C类中找，如果C类中么有，则继续去D类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> C --> D
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

#多态
# 　　多态性（polymorphisn）是允许你将父对象设置成为和一个或更多的他的子对象相等的技术，赋值之后，父对象就可以根据当前赋值给它的子对象的特性以不同的方式运作。简单的说，就是一句话：允许将子类类型的指针赋值给父类类型的指针。
# 　　那么，多态的作用是什么呢？我们知道，封装可以隐藏实现细节，使得代码模块化；继承可以扩展已存在的代码模块（类）；它们的目的都是为了——代码重用。而多态则是为了实现另一个目的——接口重用！多态的作用，就是为了类在继承和派生的时候，保证使用“家谱”中任一类的实例的某一属性时的正确调用。
# 　　Pyhon不支持多态并且也用不到多态，多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”

#python伪代码实现java或C#多态     及  python"鸭子类型"
class F1:
    pass

class S1(F1):
    def show(self):
        print 'S1.show'

class S2(F1):
    def show(self):
        print 'S2.show'
# 由于在Java或C#中定义函数参数时，必须指定参数的类型
# 为了让Func函数既可以执行S1对象的show方法，又可以执行S2对象的show方法，所以，定义了一个S1和S2类的父类
# 而实际传入的参数是：S1对象和S2对象
def Func(obj):
    """Func函数需要接收一个F1类型或者F1子类的类型"""
    print obj.show()

s1_obj = S1()
Func(s1_obj) # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show
s2_obj = S2()
Func(s2_obj) # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show

#通过python模拟的多态
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def talk(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
 
class Cat(Animal):
    def talk(self):
        return 'Meow!'
 
class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'
 
animals = [Cat('Missy'),
           Dog('Lassie')]
 
for animal in animals:
    print animal.name + ': ' + animal.talk()
    
    
#####类的方法@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#类的成员可以分为三大类：字段(普通字段、静态字段)、方法(普通方法、类方法、静态方法)和属性(普通属性)。
#一、字段  包括：普通字段和静态字段，普通字段属于对象，静态字段属于类
#静态字段在内存中只保存一份,普通字段在每个对象中都要保存一份
#应用场景： 通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段
class Foo:
    # 静态字段
    country = "China"
    def __init__(self, name):
        # 普通字段
        self.name = name
# 直接访问静态字段
Foo.country
# 直接访问普通字段
obj = Foo("山西")

#二、方法  包括：普通方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同
# 普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；
# 类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；
# 静态方法：由类调用；无默认参数
class Foo_2:
    #静态方法
    @staticmethod
    def xo(arg1, arg2):     #无默认参数，可不传参数，可传任意参数
        print("xo")
    #类方法
    @classmethod
    def xxoo(cls):             #定义类方法，至少有一个cls参数
        print(cls)
    #普通方法，类中
    def show(self):           #定义普通方法，至少有一个self参数
        print("show")
# 调用静态方法
Foo_2.xo(1,2)
# 调用类方法
Foo_2.xxoo()
# 调用普通方法
obj = Foo_2()
obj.show()
# 相同点：对于所有的方法而言，均属于类（非对象）中，所以，在内存中也只保存一份。
# 不同点：方法调用者不同、调用方法时自动传入的参数不同。

#三、属性
# 定义时，在普通方法的基础上添加 @property 装饰器；
# 定义时，属性仅有一个self参数
# 调用时，无需括号
#            方法：foo_obj.func()
#            属性：foo_obj.prop
# 属性存在意义是：访问属性时可以制造出和访问字段完全相同的假象
# 属性由方法变种而来，如果Python中没有属性，方法完全可以代替其功能。
class Foo_3:
    def __init__(self, name):
        self.name = name
    # 属性，将方法伪造成一种字段
    @property
    def end(self):
        return self.name
    # 修改end值
    @end.setter
    def end(self, new_name):
        self.name = new_name

obj = Foo_3("nick")
# 调用属性，不需要加括号
result2 = obj.end
print(result2)
# 调用修改end.setter属性（自动将jenny传入当参数new_name）
obj.end = "jenny"
result3 = obj.end
print(result3)

#属性的两种定义方式
# 装饰器 即：在方法上应用装饰器
#经典类，具有一种@property装饰器
class Goods:
    @property
    def price(self):
        return "nick"
obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值

#新式类，具有三种@property装饰器
class Goodss(object):
    @property
    def price(self):
        print '@property'
    @price.setter
    def price(self, value):
        print '@price.setter'
    @price.deleter
    def price(self):
        print '@price.deleter'
obj = Goodss()
obj.price          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price      # 自动执行 @price.deleter 修饰的 price 方法

#实例
class Goodsss(object):
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8
    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price
    @price.setter
    def price(self, value):
        self.original_price = value
    @price.deleter
    def price(self):
        del self.original_price
        del self.discount
obj = Goodsss()
obj.price         # 获取商品价格
obj.price = 200   # 修改商品原价
del obj.price     # 删除商品原价

# 静态字段 即：在类中定义值为property对象的静态字段
class Foo4:
    def get_bar(self):
        return 'nick'
    BAR = property(get_bar)

obj = Foo4()
reuslt = obj.BAR        # 自动调用get_bar方法，并获取方法的返回值
print reuslt
# property的构造方法中有个四个参数
# 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
# 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
# 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
class Foo5:
    def get_bar(self):
        return 'nick'
    # *必须两个参数
    def set_bar(self, value): 
        return 'set value' + value
    def del_bar(self):
        return 'nick'
    BAR = property(get_bar, set_bar, del_bar, 'description...')
obj = Foo5()
obj.BAR              # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "jenny"    # 自动调用第二个参数中定义的方法：set_bar方法，并将“jenny”当作参数传入
obj.BAR.__doc__      # 自动获取第四个参数中设置的值：description...
del obj.BAR          # 自动调用第三个参数中定义的方法：del_bar方法
# 由于静态字段方式创建属性具有三种访问方式，我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
class Goodssss(object):
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8
    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price
    def set_price(self, value):
        self.original_price = value
    def del_price(self):
        del self.original_price
        del self.discount
    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

obj = Goodssss()
obj.PRICE         # 获取商品价格
obj.PRICE = 200   # 修改商品原价
del obj.PRICE     # 删除商品原价

#####类成员的修饰符@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 每一个类的成员都有两种形式：
# 公有成员，在任何地方都能访问
# 私有成员，只有在类的内部才能方法
# 私有成员和公有成员的定义不同：私有成员命名时，前两个字符是下划线。（特殊成员除外，例如：__init__、__call__、__dict__等）

# 私有成员和公有成员的访问限制不同：
# 静态字段
# 公有静态字段：类可以访问；类内部可以访问；派生类中可以访问
# 私有静态字段：仅类内部可以访问；
class CC:
    name = "公有静态字段"
    def func(self):
        print CC.name

class DD(CC):
    def show(self):
        print CC.name

CC.name         # 类访问
obj = CC()
obj.func()      # 类内部可以访问
obj_son = DD()
obj_son.show()  # 派生类中可以访问

class CCC:
    __name = "私有静态字段"
    def func(self):
        print CCC.__name

class DDD(CCC):
    def show(self):
        print CCC.__name

# CCC.__name       # 类访问            ==> 错误
obj = CCC()
obj.func()     # 类内部可以访问     ==> 正确
obj_son = DDD()
# obj_son.show() # 派生类中可以访问   ==> 错误

# 普通字段
# 公有普通字段：对象可以访问；类内部可以访问；派生类中可以访问；
# 私有普通字段：仅类内部可以访问；
class CA:
    def __init__(self):
        self.foo = "公有字段"
    def func(self):
        print self.foo  #　类内部访问

class DA(CA):
    def show(self):
        print self.foo  # 派生类中访问

obj = CA()
obj.foo     # 通过对象访问
obj.func()  # 类内部访问
obj_son = DA()
obj_son.show()  # 派生类中访问

class CB:
    def __init__(self):
        self.__foo = "私有字段"
    def func(self):
        print self.__foo    # 类内部访问

class DB(CB):
    def show(self):
        print self.__foo    # 派生类中访问

obj = CB()
# obj.__foo   # 通过对象访问    ==> 错误
obj.func()  # 类内部访问        ==> 正确
obj_son = DB()
# obj_son.show()  # 派生类中访问  ==> 错误

# 方法、属性的访问于上述方式相似，即：私有成员只能在类内部使用
# ps：如果想要强制访问私有字段，可以通过 【对象._类名__私有字段明 】访问（如：obj._C__foo），不建议强制访问私有成员。

#####类的特殊成员@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#1、__doc__  表示类的描述信息
class Fooo:
    """描述类信息 """
    def func(self):
        pass
print Fooo.__doc__  #输出：类的描述信息

#2. __module__ 和  __class__
# 　　__module__表示当前操作的对象在那个模块
# 　　__class__ 表示当前操作的对象的类是什么

# lib/aa.py
# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# class CD:
#     def __init__(self):
#         self.name = 'nick'
    
# index.py
# from lib.aa import C
# obj = C()
# print obj.__module__  # 输出 lib.aa，即：输出模块
# print obj.__class__   # 输出 lib.aa.C，即：输出类

#3. __init__    构造方法，通过类创建对象时，自动触发执行。
class Foox:
    def __init__(self, name):
        self.name = name
        self.age = 18

obj = Foox('nick')     # 自动执行类中的 __init__ 方法

#4. __del__
# 析构方法，当对象在内存中被释放时，自动触发执行。
# 注：此方法一般无须定义，因为Python是一门高级语言，程序员在使用时无需关心内存的分配和释放，因为此工作都是交给Python解释器来执行，所以，析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。
class Foos:
    def __del__(self):
        pass

#5. __call__
# 对象后面加括号，触发执行。
# 注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
class Fooa:
    def __init__(self):
        print("This is init")

    def __call__(self, *args, **kwargs):
        print("This is call")
        return "CC"

obj = Fooa()        # 执行 __init__
obj()               # 执行 __call__

result = Fooa()()   # 执行 __call__
print(result)

#6. __dict__    类或对象中的所有成员
class Province:
    country = 'China'
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def func(self, *args, **kwargs):
        print 'func'

# 获取类的成员，即：静态字段、方法、
print Province.__dict__
# 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}
obj1 = Province('shangxi',10000)
print obj1.__dict__
# 获取 对象obj1 的成员
# 输出：{'count': 10000, 'name': 'shangxi'}
obj2 = Province('shangdong', 3888)
print obj2.__dict__
# 获取 对象obj1 的成员
# 输出：{'count': 3888, 'name': 'shangdong'}

#7. __str__    如果一个类中定义了__str__方法，那么在打印对象时，默认输出该方法的返回值。
class FooB:
    def __str__(self):
        return 'nick'

obj = FooB()
print obj

#8、__getitem__、__setitem__、__delitem__    用于索引操作，如字典。以上分别表示获取、设置、删除数据
class FooC:
    def __getitem__(self, item):
        print(item)
    def __setitem__(self, key, value):
        print(key, value)
    def __delitem__(self, key):
        print(key)
obj = FooC()
obj["nick"]                     # 自动触发执行 __getitem__
obj["nick"] = "jenny"           # 自动触发执行 __setitem__
del obj["nick"]                 # 自动触发执行 __delitem__

#9、__getslice__、__setslice__、__delslice__    该三个方法用于分片操作，如：列表
class FooD(object):
    def __getslice__(self, i, j):
        print '__getslice__',i,j
    def __setslice__(self, i, j, sequence):
        print '__setslice__',i,j
    def __delslice__(self, i, j):
        print '__delslice__',i,j
obj = FooD()
obj[-1:1]                   # 自动触发执行 __getslice__
obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
del obj[0:2]                # 自动触发执行 __delslice__

#10. __iter__    用于迭代器，之所以列表、字典、元组可以进行for循环，是因为类型内部定义了 __iter__
class FooE(object):
    def __init__(self, sq):
        self.sq = sq
    def __iter__(self):
        return iter(self.sq)

obj = FooE([11,22,33,44])
for i in obj:
    print i
    
obj = iter([11,22,33,44])
i = 0
while i < 3:
    val = obj.next()
    i = i + 1
    print val
    
#11. __mro__ 和__slot__   在解析父类的__init__时，定义解析顺序的是子类的__mro__属性，内容为一个存储要解析类顺序的元组。
class AX(object):
    def __init__(self):
        print '    -> Enter A'
        print '    <- Leave A'

class BX(AX):
    def __init(self):
        print '    -> Enter B'
        # A.__init__(self)
        super(BX, self).__init__()
        print '    <- Leave B'

class CX(AX):
    def __init__(self):
        print "    -> Enter C"
        # A.__init__(self)
        super(CX, self).__init__()
        print "    <- Leave C"

class DX(BX, CX):
    def __init__(self):
        print "    -> Enter D"
        # B.__init__(self)
        # C.__init__(self)
        super(DX, self).__init__()
        print "    <- Leave D"

if __name__ == "__main__":
    d = DX()
    print "MRO:", [x.__name__ for x in DX.__mro__]
    print type(DX.__mro__)
# __slot__定义类中可以被外界访问的属性。
# 当父类中定义了__slot__时，不能向父类中添加属性。如果子类中没有定义__slot__，则子类不受父类__slot__定义的限制。
# 如果父类与子类中都定义了__slot__，则邮箱的结果为父类与子类__slot__的合集。

#12. __new__ 和 __metaclass__ 
# 阅读以下代码：
# class Foo(object):
#     def __init__(self):
#         pass
# obj = Foo()   # obj是通过Foo类实例化的对象
# 上述代码中，obj 是通过 Foo 类实例化的对象，其实，不仅 obj 是一个对象，Foo类本身也是一个对象，因为在Python中一切事物都是对象。
# 如果按照一切事物都是对象的理论：obj对象是通过执行Foo类的构造方法创建，那么Foo类对象应该也是通过执行某个类的 构造方法 创建。
# print type(obj) # 输出：<class '__main__.Foo'>     表示，obj 对象由Foo类创建
# print type(Foo) # 输出：<type 'type'>              表示，Foo类对象由 type 类创建
# 所以，obj对象是Foo类的一个实例，Foo类对象是 type 类的一个实例，即：Foo类对象 是通过type类的构造方法创建。
# 那么，创建类就可以有两种方式：
# 1> 普通方式
# class Foo(object):
#     def func(self):
#         print 'hello word'
# 2> 特殊方式（type类的构造函数）
# def func(self):
#     print 'hello word'
#   
# Foo = type('Foo',(object,), {'func': func})
# #type第一个参数：类名
# #type第二个参数：当前类的基类
# #type第三个参数：类的成员
# ＝＝》 类 是由 type 类实例化产生
# 那么问题来了，类默认是由 type 类实例化产生，type类中如何实现的创建类？类又是如何创建对象？
# 答：类中有一个属性 __metaclass__，其用来表示该类由 谁 来实例化创建，所以，我们可以为 __metaclass__ 设置一个type类的派生类，从而查看 类 创建的过程。
# class MyType(type):
#     def __init__(self, what, bases=None, dict=None):
#         super(MyType, self).__init__(what, bases, dict)
# 
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__(self, *args, **kwargs)
#         self.__init__(obj)
# 
# class Foo(object):
#     __metaclass__ = MyType
#     def __init__(self, name):
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls, *args, **kwargs)
# # 第一阶段：解释器从上到下执行代码创建Foo类
# # 第二阶段：通过Foo类创建obj对象
# obj = Foo()

#####isinstance(obj, cls) & issubclass(sub, super)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##isinstance(obj, cls) 检查是否obj是否是类 cls 的对象
class FooF(object):
    pass
obj = FooF()
print isinstance(obj, FooF)

##issubclass(sub, super) 检查sub类是否是 super 类的派生类
class FooG(object):
    pass
class Bar(FooG):
    pass
print issubclass(Bar, FooG)

#####异常处理@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##2、异常种类
# AttributeError          试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError                 输入/输出异常；基本上是无法打开文件
# ImportError             无法引入模块或包；基本上是路径问题或名称错误
# IndentationError        语法错误（的子类） ；代码没有正确对齐
# IndexError              下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError                试图访问字典里不存在的键
# KeyboardInterrupt       Ctrl+C被按下
# NameError               使用一个还未被赋予对象的变量
# SyntaxError             Python代码非法，代码不能编译(个人认为这是语法错误，写错了） 
# TypeError               传入对象类型与要求的不符合
# UnboundLocalError       试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError              传入一个调用者不期望的值，即使值的类型是正确的
# ...

# 未捕获到异常，程序直接报错
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print e
except (KeyError, ValueError) as e:
    print e
# 万能异常
except Exception,e:
    print e

##3、异常其他结构
try:
    # 主代码块
    pass
except KeyError,e:
    # 异常时，执行该块
    pass
else:
    # 主代码块成功执行完，执行该块
    pass
finally:
    # 无论异常与否，最终执行该块
    pass

##4、主动触发异常
try:
    raise Exception('错误了。。。')
except Exception,e:
    print e
    
##5、自定义异常
class NickException(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise NickException('我的异常')
except NickException,e:
    print e
    
##6、断言
# assert 条件
# 条件成立则pass，条件不成立则报错
# assert 1 == 1
# assert 1 == 2

#####反射@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#python中的反射功能是由以下四个内置函数提供：hasattr、getattr、setattr、delattr，改四个函数分别用于对对象内部执行：检查是否含有某成员、获取成员、设置成员、删除成员。
# # commons.py 文件
# name = "nick"
# def f1():
#     return "This is f1."
# def f2():
#     return "This is f2."
# def nb():
#     return "This is niubily."
#  
# # index.py 文件
# import commons
# #根据字符串的形式去某个模块中寻找东西
# target_func = getattr(commons,"f1")     # 找函数
# result = target_func()
# print(result)
# target_func = getattr(commons,"name")   # 找全局变量
# print(target_func)
# target_func = getattr(commons,"age",None)   # 找不到返回None
# print(target_func)
# #根据字符串的形式去某个模块中判断东西是否存在
# tarhas_func = hasattr(commons,"f5")     # 找函数
# print("before:",tarhas_func)
# # tarhas_func = hasattr(commons,"name") # 找全局变量
# # print(tarhas_func)
# #根据字符串的形式去某个模块中设置东西
# setattr(commons,"f5","lambda x: return \"This is new func.\"")  # 设置一个函数
# setattr(commons,"age",18)               # 设置全局变量
# tarhas_func = hasattr(commons,"f5")     # 检查函数是否存在
# print("after:",tarhas_func)
# #根据字符串的形式去某个模块中删除东西
# delattr(commons,"f5")                   # 删除一个函数
# tarhas_func = hasattr(commons,"f5")     # 检查函数是否存在
# print("end:",tarhas_func)

##补充__import__
# # 通过字符串的形式，导入模块。起个别名 ccas。
# comm = input("Please:")
# ccas = __import__(comm)
# ccas.f1()
# # 需要做拼接导入时后加 fromlist=True（否则只导入lib）
# ccas = __import__("lib."+comm, fromlist=True)

##路由系统
# ##### 路由系统 #####
# 
# # 输入 模块名/函数名  （例如：commons/nb）
# url = input("Please input you want url:")
# target_module, target_func = url.split("/")
# #m = __import__("lib."+target_module,fromlist=True)
# m = __import__(target_module)
# 
# if hasattr(m,target_func):
#     target_func = getattr(m,target_func)
#     result = target_func()
#     print(result)
# else:
#     print("Sorry,it's 404 not found.")

#####单例模式@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 单例模式存在的目的是保证当前内存中仅存在单个实例，避免内存浪费！！！
# （程序如果并发量大的话，内存里就会存在非常多功能上一模一样的对象。存在这些对象肯定会消耗内存，对于这些功能相同的对象可以在内存中仅创建一个，需要时都去调用）
# 单例模式
class FooH:
    __n = None
    def __init__(self):
        self.name = "nick"
        self.age = 18
        self.job = "pythoner"
    @staticmethod
    def dl():
        if FooH.__n:
            return FooH.__n
        else:
            FooH.__n = FooH()
            return FooH.__n
# 创建对象时不能再直接使用：obj = Foo()，而应该调用特殊的方法：obj = Foo.dl() 。
f1 = FooH.dl()
print(f1)
f2 = FooH.dl()
print(f2)
f3 = FooH.dl()
print(f3)
# 运行结果
# <__main__.Foo object at 0x0000000001142390>
# <__main__.Foo object at 0x0000000001142390>
# <__main__.Foo object at 0x0000000001142390>

#装饰器方式单例模式
# 装饰器方式单例模式
def singleton(argv):
    dic = {}
    def s(*args, **kwargs):
        if argv not in dic:
            dic[argv] = argv(*args, **kwargs)
            return dic[argv]
        else:
            return dic[argv]
    return s
 
# 类上加单例装饰器
@singleton
class FooI:
    pass
@singleton
class FooJ:
    pass