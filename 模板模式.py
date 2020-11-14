#-*-coding:utf8-*-
#模板方法模式(TemplateMethod):定义一个操作中的算法骨架，而将一些步骤延迟到子类中。
#这使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤
#通过把不变行为搬移到超类，去除子类中的重复代码是其优势所在
#适用：当要完成在某一细节层次一致的一个过程或一系列步骤，但其个别步骤在更详细的层次上的实现可能不同时
#当不变的和可变的行为在方法的子类实现中混合在一起时，不变的行为就会在子类中重复出现，通过模板把
#这些行为搬移到单一的地方，使得子类摆脱重复不变行为的纠缠
class AbstractClass(object):
    '''
    抽象模板，定义并实现一个模板方法，是一个具体方法，给出了一个顶级逻辑骨架，而逻辑的组成
    步骤在相应的抽象操作中，推迟到子类实现，顶级逻辑也可能调用具体方法
    '''
    def __init__(self):
        pass
    def PrimitiveOperation1(self):
        pass
    def PrimitiveOperation1(self):
        pass
    def TemplateMethod(self):
        self.PrimitiveOperation1()
        self.PrimitiveOperation2()
        print("模板方法给出了逻辑骨架，推迟到子类实现")
class ConcreteClassA(AbstractClass):
    def __init__(self):
        pass
    def PrimitiveOperation1(self):
        print("具体类A 方法1的实现")
    def PrimitiveOperation2(self):
        print("具体类A 方法2的实现")
class ConcreteClassB(AbstractClass):
    def __init__(self):
        pass
    def PrimitiveOperation1(self):
        print("具体类B 方法1的实现")
    def PrimitiveOperation2(self):
        print("具体类B 方法2的实现")
if __name__ == "__main__":
    c = ConcreteClassA()
    c.TemplateMethod()

    c = ConcreteClassB()
    c.TemplateMethod()
    
