from model.FileObject import *
from model.OperationIP import *
from model.OperationObject import *
from model.OperationTime import *
from model.OperationType import *


class OperationInfo:
    IS_RISK = "IS_RISK"
    NOT_RISK = "NOT_RISK"

    def __init__(self, o_id: int, o_ip: OperationIp, o_type: OperationType, o_object: OperationObject,
                 o_time: OperationTime, is_risk: str):
        self.o_id = o_id
        self.o_ip = o_ip
        self.o_type = o_type
        self.o_object = o_object
        self.o_time = o_time
        self.is_risk = is_risk

    def __repr__(self):
        return "[{},{},{},{},{},{}]".format(self.o_id, self.o_ip, self.o_type, self.o_object, self.o_time, self.is_risk)

    def __str__(self):
        return "[{},{},{},{},{},{}]".format(self.o_id, self.o_ip, self.o_type, self.o_object, self.o_time, self.is_risk)


def __test1():
    id1 = 1
    ip1 = OperationIp("000", OperationIp.INTRANET, OperationIp.USER)
    type1 = OperationType(OperationType.READ, OperationType.LOCAL)
    object_content = FileObject(FileObject.FILE, FileObject.NORMAL)
    object1 = OperationObject(object_content, NoneFileObject)
    time1 = OperationTime("0", "0", "1", "16", "26")
    risk1 = OperationInfo.NOT_RISK
    operation = OperationInfo(id1, ip1, type1, object1, time1, risk1)
    print(operation)
    print(str(operation))


if __name__ == "__main__":
    __test1()
