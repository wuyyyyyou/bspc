from model.FileObject import *
from model.OperationIP import *

"""
OperationObject是一个比较复杂的类型，因为要考虑网络流量信息和日志信息的不同点，
我们获得的网络流量信息是可以知道它传输的是什么文件的（非加密流量）。
所以OperationObject类采用如下设计，object_content这个参数可以是OperationIP也可以是FileObject,
·如果是普通日志记录的操作信息，那么object_content是FileObject代表被操作的文件（也可以是自己的主机本身),object_append
是空文件。
·如果是流量下载信息，那么object_content代表着交互的主机，并且object_append代表着传输的文件。
"""


class OperationObject:
    HOST = "HOST"  # 如权限申请，硬件控制等操作操作对象是本机

    def __init__(self, object_content, object_append: FileObject):
        self.object_content = object_content
        self.object_append = object_append

    def __repr__(self):
        return "[{},{}]".format(self.object_content, self.object_append)

    def __str__(self):
        return "[{},{}]".format(self.object_content, self.object_append)


HostOperationObject = OperationObject(OperationObject.HOST, NoneFileObject)


# 一般来说操作对象以下几种形式种形式
def __test1():
    # 正常的操作文件的操作类型
    file = FileObject(FileObject.VIDEO, FileObject.NORMAL)
    m_object = OperationObject(file, NoneFileObject)
    print(m_object)

    # 申请权限操作
    object2 = HostOperationObject
    print(object2)

    # 网页下载文件操作
    file3 = FileObject(FileObject.FILE, FileObject.NORMAL)
    ip3 = OperationIp("111", OperationIp.EXTRANET, OperationIp.DANGEROUS)
    object3 = OperationObject(ip3, file3)
    print(object3)

    # 阅览网页操作
    file4 = NoneFileObject
    ip4 = OperationIp("110", OperationIp.EXTRANET, OperationIp.SECURE)
    object4 = OperationObject(ip4, file4)
    print(object4)


if __name__ == "__main__":
    __test1()
