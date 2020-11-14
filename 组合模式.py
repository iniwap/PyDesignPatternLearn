#-*-coding:utf8-*-
#组合模式(Composite):将对象组合成树形结构以表示"部分--整体"的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性
#
class Component(object):
    '''
    为组合中的对象声明接口，在适当的情况下，实现所有类共有接口的默认行为。声明一个接口用于管理和访问Component子部
    '''
    def __init__(self,name):
        self.name = name
    def Add(self,c):
        pass
    def Remove(self,c):
        pass
    def Display(self,depth):
        pass
class Leaf(Component):
    def __init__(self,name):
        #self.name=super(Leaf,self).name
        #pass
        self.name = name
    def Add(self,c):
        print("不能向叶子节点添加")
    def Remove(self,c):
        print("不能从叶子节点删除")
    def Display(self,depth):
        print(depth,self.name)
class Composite(Component):
    __children = []
    def __init__(self,name):
        self.name = name
    def Add(self,c):
        self.__children.append(c)
    def Remove(self,c):
        self.__children.remove(c)
    def Display(self,depth):
        print(depth,self.name)
        for c in self.__children:
            c.Display(depth+2)
if __name__ == "__main__":
    root = Composite("root")
    root.Add(Leaf("A"))
    root.Add(Leaf("B"))

    comp = Composite("Composite X")
    comp.Add(Leaf("Leaf XA"))
    comp.Add(Leaf("Leaf XB"))

    root.Add(comp)

    comp2 = Composite("Composite XY")
    comp2.Add(Leaf("Leaf XYA"))
    comp2.Add(Leaf("Leaf XYB"))

    comp.Add(Leaf("Leaf C"))

    leaf = Leaf("Leaf D")
    root.Add(leaf)

    root.Display(1)
