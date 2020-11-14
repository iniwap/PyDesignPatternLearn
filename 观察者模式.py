#-*-coding:utf8-*-
#观察者(Observer)、发布订阅模式(Publish/Subscribe):定义一种一对多的依赖关系，让多个观察者对象同时监听某一
#主题对象，这个主题对象在状态发生变化时，会通知所有观察者对象，使它们能够自动更新自己
#适用：当一个对象变化需要同时改变其他对象的时候，而且其不知道有多帅对象有待改变。其所做的工作就是解除耦合，让耦合双方都依赖于抽象，而不是依赖于具体，
#从而是一方变化不会影响到另一方变化。这是依赖倒转原则的最佳体现


class Subject(object):
    '''
    主题或者抽象通知类，一般用一个抽象类或者一个接口实现。它把所有对观察者对象的引用保存，每个
    主题可以有任何数量的观察者。抽象主题提供一个接口，可以增加和删除观察者对象
    '''
    def __init__(self):
        self._observers = []
    def Attach(self,observer):
        self._observers.append(observer)
    def Detach(self,observer):
        self._observers.remove(observer)
    def Notify(self):
        for observer in self._observers:
            observer.Update()
class Observer(object):
    '''
    抽象观察者，为所有具体观察者定义一个接口，在得到主题的通知时更新自己。这个接口叫做更新接口。
    抽象观察者一般用一个抽象类或者一个接口实现，更新接口通常包含一个Update()方法即更新方法
    '''
    def __init__(self):
        pass
    def Update(self):
        pass
class ConcreteSubject(Subject):
    '''
    具体主题或者具体通知者，将有关状态存入具体观察者对象，在具体主题的内部状态改变时，给所有登记过的观察者
    发出通知。通常用一个具体的子类实现
    '''
    def __init__(self):
        super(ConcreteSubject,self).__init__()
        self._subjectState = ""
    def getSubjectState(self):
        return self._subjectState
    def setSubjectState(self,subjectState):
        self._subjectState = subjectState
class ConcreteObserver(Observer):
    '''
    具体观察者，实现抽象观察者绝色所要求的更新接口，以便使本身的状态与主题的状态协调。
    具体观察者角色可以保存一个指向具体主题对象的引用，具体观察者角色通常用一个具体子类实现
    '''
    def __init__(self,subject,observer):
        self._observer = observer
        self._subject = subject
        self._observerState = ""
    def Update(self):
        self.observerState = self._subject._subjectState
        print(self.observerState)
    def GetSubject(self):
        return self._subject
    def SetSubject(self,subject):
        self._subject = subject
if __name__ == "__main__":
    cs = ConcreteSubject()
    co1 = ConcreteObserver(cs,"XState")
    co2 = ConcreteObserver(cs,"YState")
    co3 = ConcreteObserver(cs,"ZState")
    cs.Attach(co1)
    cs.Attach(co2)
    cs.Attach(co3)

    cs.Detach(co2)
    cs._subjectState = "NewState"
    cs.Notify()
    
