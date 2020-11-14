#-*-coding:utf8-*-
#外观模式(Facade):为子系统中的一组接口提供一个一致的界面，此模式定义了一个高层接口，这个接口使得子系统更加容易使用
#体现了依赖倒转和迪米特法则
#适用：首先在设计初级阶段应将不同的两个层分离，考虑到三层架构的数据访问层，业务逻辑层，表示层的层层
#之间建立门面(Facade),为复杂子系统提供简单的接口，使得耦合度降低；其次开发阶段，子系统往往因不断重构而变得
#复杂，增加门面可以提供一个简单的接口，减少其之间的依赖；第三，在维护一个遗留的大型系统时，可能
#该系统已经非常难以维护和扩展，可以为新系统开发一个Facade类，来提供设计粗糙或高度复杂的遗留代码的比较清晰
#简单的接口，让系统与Facade对象交互，Facade与遗留代码交互所有复杂的工作
class SubSystem1(object):
    def __init__(self):
        pass
    def Method1(self):
        print("子系统方法1")
class SubSystem2(object):
    def __init__(self):
        pass
    def Method2(self):
        print("子系统2方法2")
class Facade(object):
    def __init__(self):
        self._s1 = SubSystem1()
        self._s2 = SubSystem2()
    def MethodA(self):
        print(u"方法组合A")
        self._s1.Method1()
        self._s2.Method2()
    def MethodB(self):
        print(u"方法组合B")
        self._s2.Method2()
if __name__ == "__main__":
    facade = Facade()
    facade.MethodA()
    facade.MethodB()
        
