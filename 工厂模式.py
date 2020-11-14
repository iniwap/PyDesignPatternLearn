#-*-coding:utf8-*-
#工厂方法模式:定义一个创建对象的接口，让子类决定实例化哪一个类。使得实例化延迟到子类
#与简单工厂的比较：
#简单工厂最大的有点在于工厂类中包含必要的逻辑判断，根据客户端选择动态的实例化相关的类，
#对于客户端来说，去除了与具体产品的依赖，这其实是违背开放-封闭原则的
#工厂方法将简单工厂的内部逻辑移到了客户端，则需要改动客户端，与简单工厂的修改工厂类不同之处。
class Operation(object):
    def __init__(self):
        self._numA = 0
        self._numB = 0
    def getA(self):
        return self._numA
    def setA(self,numA):
        self._numA = numA
    def getB(self):
        return self._numB
    def setB(self,numB):
        self._numB = numB
    def GetResult(self):
        pass
class OperationAdd(Operation):
    def __init__(self):
        pass
    def GetResult(self):
        result = self._numA + self._numB
        return result
class OperationSub(Operation):
    def __init__(self):
        pass
    def GetResult(self):
        result = self._numA - self._numB
        return result
class OperationMul(Operation):
    def __init__(self):
        pass
    def GetResult(self):
        result = self._numA * self._numB
        return result
class OperationDiv(Operation):
    def __init__(self):
        pass
    def GetResult(self):
        result = 0
        if(self._numB != 0):
            result = self._numA / self._numB
        else:
            #print("除数不能为0")
            return "除数不能为0"
        return result
class IFactory(object):
    '''
    定义工厂接口，其他各建一个具体工厂去实现这个接口
    '''
    def __init__(self):
        pass
    def CreateOperation(self):
        pass
class AddFactory(IFactory):
    def __init__(self):
        pass
    def CreateOperation(self):
        return OperationAdd()
class SubFactory(IFactory):
    def __init__(self):
        pass
    def CreateOperation(self):
        return OperationSub()
class MulFactory(IFactory):
    def __init__(self):
        pass
    def CreateOperation(self):
        return OperationMul()
class DivFactory(IFactory):
    def __init__(self):
        pass
    def CreateOperation(self):
        return OperationDiv()
if __name__ == "__main__":
    operation = AddFactory().CreateOperation()
    operation.setA(4)
    operation.setB(2)
    result = operation.GetResult()
    print(result)
