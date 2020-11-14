#-*-coding:utf8-*-
#iniwaper@gmail.com
#代理模式(Proxy)：为其他对象提供一种代理以控制对这个对象的访问
#适用：1，远程代理，即为一个对象在不同的地址空间提供局部代表，这样可以隐藏一个对象存在于不同的地址空间的事实
#2，虚拟代理，是根据需要创建开销很大的对象，通过它来存放实例化需要很长时间的真实对象
#3，安全代理，用来控制真实对象访问的权限
#4，智能指引，当调用真实的对象时，代理处理另外一些事
class Subject(object):
    '''
    定义RealSybject和Proxy的共用接口
    使得任何使用RealSubject的地方都可以使用Proxy
    '''
    def __init__(self):
        pass
    def Request(self):
        pass
class RealSubject(Subject):
    '''
    定义Proxy所代表的真实实体
    '''
    def __init__(self):
        pass
    def Request(self):
        print("真实的请求")
class Proxy(Subject):
    def __init__(self):
        self._realSubject = None
    def Request(self):
        if(self._realSubject == None):
            self._realSubject = RealSubject()
        self._realSubject.Request()
if __name__ == "__main__":
    proxy = Proxy()
    proxy.Request()
