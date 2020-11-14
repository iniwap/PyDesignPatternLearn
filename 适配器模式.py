#-*-coding:utf8-*-
#适配器(Adapter):将一个类的接口转换成客户希望的另一个接口，使得原来由于接口不兼容而不能一起工作的类可以一起工作
#系统的数据和行为都是正确的，但接口不符，考虑使用适配器，目的是使控制范围之外的一个原有对象与某个
#接口匹配。主要用于希望复用一些现存的类，但是接口又与复用环境要求不一致的情况
class Target(object):
    def __init__(self):
        pass
    def Request(self):
        print("普通请求")
class Adaptee(object):
    def __init__(self):
        pass
    def SpecificRequest(self):
        print("特殊请求")
class Adapter(Target):
    adaptee = Adaptee()
    def __init__(self):
        pass
    def Request(self):
        self.adaptee.SpecificRequest()
if __name__ == "__main__":
    target = Adapter()
    target.Request()
