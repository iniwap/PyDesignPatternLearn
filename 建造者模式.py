#-*-coding:utf8-*-
#建造者-生成器模式(Builder):将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示时
#建造者模式是在创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时适用的模式
class Product(object):
    '''
    产品类，由多个部件组成
    '''
    def __init__(self):
        self._parts=[]
    def AddPart(self,part):
        self._parts.append(part)
    def show(self):
        print(u"产品创建")
        for i in self._parts:
            print(i)
class Builder(object):
    '''
    抽象建造者类，确定产品由哪些部件组成，并声明一个产品建造后的方法
    '''
    def __init__(self):
        pass
    def BuildPartA(self):
        pass
    def BuildPartB(self):
        pass
    def GetProduct(self):
        pass
class ConcreteBuilder1(Builder):
    '''
    具体建造者类，继承建造者类，重写建造方法
    '''
    def __init__(self):
         self._product = Product()
    def BuildPartA(self):
        self._product.AddPart(u"部件X1")
    def BuildPartB(self):
        self._product.AddPart(u"部件Y1")
    def GetProduct(self):
        return self._product
class ConcreteBuilder2(Builder):
    def __init__(self):
         self._product = Product()
    def BuildPartA(self):
        self._product.AddPart(u"部件X2")
    def BuildPartB(self):
        self._product.AddPart(u"部件Y2")
    def GetProduct(self):
        return self._product
class Director(object):
    '''
    指挥者类，控制建造的具体步骤
    '''
    def __init__(self):
        pass
    def Construct(self,builder):
        builder.BuildPartA()
        builder.BuildPartB()
if __name__ == "__main__":
    director = Director()
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()
    
    director.Construct(b1)
    p1 = b1.GetProduct()
    p1.show()
        
    director.Construct(b2)
    p2 = b1.GetProduct()
    p2.show()
