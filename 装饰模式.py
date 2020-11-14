#-*-coding:utf8-*-
#iniwaper@gmail.com
#装饰模式：Decorator,动态的给一个对象添加一些额外的职责，就增加功能来说，装饰模式比生成子类更灵活
class Component(object):
    def __init__(self):
        pass
    #@staticmethod
    def Operation(self):
        pass
class ConcreteComponent(Component):
    def __init__(self):
        pass
    def Operation(self):
        print("具体装饰对象的操作")
class Decorator(Component):
    def __init__(self):
        self._component = None
    def SetComponent(self,component):
        self._component = component
    def Operation(self):
        if(self._component != None):
            self._component.Operation()
class ConcreteDecoratorA(Decorator):
    #_addState = ""
    def __init__(self):
        self.__addState = ""
    def Operation(self):
        super(ConcreteDecoratorA,self).Operation()
        self.__addState = "New State"
        print("增加具体装饰对象A的操作")
class ConcreteDecoratorB(Decorator):
    def __init__(self):
        pass
    def Operation(self):
        super(ConcreteDecoratorB,self).Operation()
        self.AddBehavior()
        print("增加具体装饰对象B的操作")
    def AddBehavior(self):
        pass
if __name__ == "__main__":
    c = ConcreteComponent()
    dA = ConcreteDecoratorA()
    dB = ConcreteDecoratorB()

    dA.SetComponent(c)
    dB.SetComponent(dA)
    dB.Operation()
