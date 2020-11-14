#-*-coding:utf8-*-
#备忘录模式(Memento):在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，这样可以恢复到原先状态
#适用：功能复杂，但需要维护或记录属性历史的类，或者需要保存的属性只是众多属性中的一小部分时，Originator
#可以根据保存的Memento信息还原到前一状态
class Originator(object):
    '''
    发起人，负责创建一个备忘录Memento,用以记录当前时刻它的内部状态，并可使用备忘录恢复内部状态
    Originator可根据需要决定Memento存储Originator的哪些内部状态
    '''
    state = None
    def __init__(self):
        pass
    def CreateMemento(self):
        return Memento(self.state)
    def SetMemento(self,memento):
        self.state = memento.State
    def Show(self):
        print("当前状态是"+self.state)
class Memento(object):
    '''
    负责存储Originator对象的内部状态，并可防止Originator以外的其他对象访问备忘录Memento
    有两个接口，Caretaker只能看到备忘录的窄接口，它只能将备忘录传递给其他对象
    Originator能够看到一个宽接口，允许它访问返回到先前状态所要的所有数据
    '''
    State = None
    def __init__(self,state):
        self.State = state
    #getattr()
class Caretaker(object):
    '''
    管理者，负责保存好备忘录Memento，不能对备忘录的内容进行操作或者检查
    '''
    memento = None
    def __init__(self):
        pass
    #getattr
    #setattr
if __name__ == "__main__":
    o = Originator()
    o.state = "On"
    o.Show()

    c = Caretaker()
    c.memento = o.CreateMemento()

    o.state = "off"
    o.Show()
    
    o.SetMemento(c.memento)
    o.Show()
    
