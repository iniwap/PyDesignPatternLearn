#-*-coding:utf8-*-
#原型模式(Prototype):用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新对象
#原型模式是从一个对象再创建另外一个可定制的对象，而且不需要指定任何创建的细节
#在初始化信息不发生变化的情况下，克隆是最好的方法，既隐藏了对象创建的细节，又对性能大大提高
import copy
class Prototype(object):
    def __init__(self,protoId):
        self.protoId = protoId
    def getId(self):
        return self.protoId
    def setId(self,protoId):
        self.protoId = protoId
    def Clone(self):#定义Clone方法
        pass
class ConcretePrototype1(Prototype):
    def __init__(self,*clone):
        if(clone[0] == None):
            self.protoId = clone[1]
            self.deepCopyOrCopy = DeepCopyOrCopy()
        else:
            self.deepCopyOrCopy = clone[0].Clone()
    def DoSome(self,value):
        self.deepCopyOrCopy.setId(value)
    def ShowSome(self):
        print(self.deepCopyOrCopy.getId())
    def Clone(self):
        #return copy.deepcopy(self)#直接深拷贝
        self.__init__(self.deepCopyOrCopy)
        return copy.copy(self)
class DeepCopyOrCopy(Prototype):#深拷贝和浅拷贝
    def __init__(self):
        self.DeepOrCopyID = ""
    def getId(self):
        return self.DeepOrCopyID
    def setId(self,DeepOrCopyID):
        self.DeepOrCopyID = DeepOrCopyID
    def Clone(self):
        return copy.copy(self)
if __name__ == "__main__":
    p1 = ConcretePrototype1(None,"I")
    #p1.DoSome(1)
    c1 = p1.Clone()
    c1.DoSome(2)
    c2 = p1.Clone()
    c2.DoSome(3)
    c3 = p1.Clone()
    c3.DoSome(4)
    print(c1.protoId)
    print(c2.protoId)
    print(c3.protoId)
    c1.ShowSome()
    c2.ShowSome()
    c3.ShowSome()
    
