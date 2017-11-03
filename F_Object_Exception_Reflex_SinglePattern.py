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
