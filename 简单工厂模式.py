#-*-coding:utf8-*-
#简单工厂模式：单独的对象来创建实例化的过程
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
class OperationFactory(object):
    def __init__(self):
        pass
    @staticmethod
    def CreateOperation(opr):
        operation  = None
        if(opr == "+"):
            operation  = OperationAdd()
        elif(opr == "-"):
            operation  = OperationSub()
        elif(opr == "*"):
            operation  = OperationMul()
        elif(opr == "/"):
            operation  = OperationDiv()
        return operation
if __name__ == "__main__":
    operation  = OperationFactory.CreateOperation("*")
    operation.setA(2)
    operation.setB(2)
    result = operation.GetResult()
    print(result)

    operation  = OperationFactory.CreateOperation("/")
    operation.setA(2)
    operation.setB(0)
    result = operation.GetResult()
    print(result)
    
