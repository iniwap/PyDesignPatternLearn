#-*-coding:utf8-*-
#状态模式(State):当一个对象的内在状态改变时运行改变其行为，这个对象看起来像是改变了其类
#用处：将特定状态相关的行为局部化，并且将不同状态的行为分割开来。通过把各种状态逻辑转移到State子类之间，从而减少相互依赖
#当一个对象的行为取决于它的状态，并且它必须在运行时刻根据状态改变它的行为时，就可以考虑使用状态模式
class State(object):
    '''
    抽象状态类，定义一个接口以封装与Context的一个特定状态相关的行为
    '''
    def __init__(self):
        pass
    def Handle(self,context):
        pass
class ConcreteStateA(State):
    '''
    具体状态，每一个子类实现一个与Context的一个状态相关的行为
    '''
    def __init__(self):
        print("状态A")
    def Handle(self,context):
        context.State = ConcreteStateB()
class ConcreteStateB(State):
    def __init__(self):
        print("状态B")
    def Handle(self,context):
        context.State = ConcreteStateA()
class Context(object):
    '''
    维护一个ConcreteState子类实例，这个实例定义当前的状态
    '''
    def __init__(self,state):
        self.State=state
    def getState(self):
        return self.State
    def setState(self,state):
        self.State=state
        print("当前的状态是"+self.State)
    def Request(self):
        self.State.Handle(self)
if __name__ == "__main__":
    c=Context(ConcreteStateA())
    c.Request()
    c.Request()
    c.Request()
    c.Request()
    c.Request()
    
