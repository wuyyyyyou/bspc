from typing import List
from model.OperationInfo import *

"""
单个操作生成操作信息列表，一般要输入的是：
1.操作的开始时间
2.操作的执行主机
3.操作的执行对象
4.操作的危险程度
"""


# 读文件操作
def read_file(o_time: OperationTime, o_ip: OperationIp, o_object: OperationObject, o_risk: str) -> List[OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType(OperationType.READ, OperationType.LOCAL), o_object, o_time, o_risk)]


# 写文件操作
def write_file(o_time: OperationTime, o_ip: OperationIp, o_object: OperationObject, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType(OperationType.WRITE, OperationType.LOCAL), o_object, o_time, o_risk)]


# 运行文件操作
def run_file(o_time: OperationTime, o_ip: OperationIp, o_object: OperationObject, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType(OperationType.RUN, OperationType.LOCAL), o_object, o_time, o_risk)]


# 开启摄像头
def open_camera(o_time: OperationTime, o_ip: OperationIp, o_risk: str) -> List[
    OperationInfo]:
    return [
        OperationInfo(-1, o_ip, OperationType(OperationType.CAMERA, OperationType.LOCAL), HostOperationObject, o_time,
                      o_risk)]


# 开启麦克风
def open_microphone(o_time: OperationTime, o_ip: OperationIp, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType(OperationType.MICROPHONE, OperationType.LOCAL), HostOperationObject,
                          o_time, o_risk)]


# 提升权限
def elevated_privileges(o_time: OperationTime, o_ip: OperationIp, o_risk: str) -> List[
    OperationInfo]:
    return [
        OperationInfo(-1, o_ip, OperationType(OperationType.APPLY, OperationType.LOCAL), HostOperationObject, o_time,
                      o_risk)]


# 远程登陆
def remote_login(o_time: OperationTime, login_ip: OperationIp, be_login_ip: OperationIp, o_risk: str,
                 is_secret: bool) -> List[
    OperationInfo]:
    o_list = []
    # 发起远程登陆生成的主机日志
    o_obj1 = OperationObject(be_login_ip, NoneFileObject)
    o_info1 = OperationInfo(-1, login_ip, OperationType(OperationType.REMOTE, OperationType.LOCAL), o_obj1, o_time,
                            o_risk)
    o_list.append(o_info1)

    # 发起远程操作后的日志信息
    if is_secret:
        # 如果是加密流量责不会出现操作类型
        o_info2 = OperationInfo(-1, login_ip, OperationType(OperationType.UNKNOWN, OperationType.INTENT), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info2)
    else:
        o_info3 = OperationInfo(-1, login_ip, OperationType(OperationType.REMOTE, OperationType.INTENT), o_obj1, o_time,
                                o_risk)
        o_list.append(o_info3)

    return o_list


# 阅览网页操作
def get_html(o_time: OperationTime, login_ip: OperationIp, be_login_ip: OperationIp, o_risk: str, is_secret: bool) -> \
        List[OperationInfo]:
    o_list = []
    # 阅览网页产生的日志信息
    o_obj1 = OperationObject(be_login_ip, NoneFileObject)
    o_info1 = OperationInfo(-1, login_ip, OperationType(OperationType.GET_HTML, OperationType.LOCAL), o_obj1, o_time,
                            o_risk)
    o_list.append(o_info1)
    if is_secret:
        o_info2 = OperationInfo(-1, login_ip, OperationType(OperationType.UNKNOWN, OperationType.INTENT), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info2)
    else:
        o_info3 = OperationInfo(-1, login_ip, OperationType(OperationType.GET_HTML, OperationType.INTENT), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info3)
    return o_list


# 远程下载文件
def get_file(o_time: OperationTime, login_ip: OperationIp, be_login_ip: OperationIp, o_risk: str, o_file: FileObject,
             is_secret: bool) -> List[OperationInfo]:
    o_list = []
    # 日志信息
    o_obj1 = OperationObject(be_login_ip, o_file)
    o_obj2 = OperationObject(login_ip, NoneFileObject)
    o_obj3 = OperationObject(login_ip, o_file)

    if o_file.file_type == FileObject.FILE:
        o_info1 = OperationInfo(-1, login_ip, OperationType(OperationType.GET_FILE, OperationType.LOCAL), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info1)
        if is_secret:
            o_info2 = OperationInfo(-1, be_login_ip, OperationType(OperationType.UNKNOWN, OperationType.INTENT), o_obj2,
                                    o_time, o_risk)
            o_list.append(o_info2)
        else:
            o_info3 = OperationInfo(-1, be_login_ip, OperationType(OperationType.SEND_FILE, OperationType.INTENT),
                                    o_obj3, o_time, o_risk)
            o_list.append(o_info3)

    elif o_file.file_type == FileObject.VIDEO:
        o_info1 = OperationInfo(-1, login_ip, OperationType(OperationType.GET_VIDEO, OperationType.LOCAL), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info1)
        if is_secret:
            o_info2 = OperationInfo(-1, be_login_ip, OperationType(OperationType.UNKNOWN, OperationType.INTENT), o_obj2,
                                    o_time, o_risk)
            o_list.append(o_info2)
        else:
            o_info3 = OperationInfo(-1, be_login_ip, OperationType(OperationType.SEND_VIDEO, OperationType.INTENT),
                                    o_obj3, o_time, o_risk)
            o_list.append(o_info3)

    elif o_file.file_type == FileObject.AUDIO:
        o_info1 = OperationInfo(-1, login_ip, OperationType(OperationType.GET_AUDIO, OperationType.LOCAL), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info1)
        if is_secret:
            o_info2 = OperationInfo(-1, be_login_ip, OperationType(OperationType.UNKNOWN, OperationType.INTENT), o_obj2,
                                    o_time, o_risk)
            o_list.append(o_info2)
        else:
            o_info3 = OperationInfo(-1, be_login_ip, OperationType(OperationType.SEND_AUDIO, OperationType.INTENT),
                                    o_obj3, o_time, o_risk)
            o_list.append(o_info3)

    elif o_file.file_type == FileObject.IMAGE:
        o_info1 = OperationInfo(-1, login_ip, OperationType(OperationType.GET_IMAGE, OperationType.LOCAL), o_obj1,
                                o_time, o_risk)
        o_list.append(o_info1)
        if is_secret:
            o_info2 = OperationInfo(-1, be_login_ip, OperationType(OperationType.UNKNOWN, OperationType.INTENT), o_obj2,
                                    o_time, o_risk)
            o_list.append(o_info2)
        else:
            o_info3 = OperationInfo(-1, be_login_ip, OperationType(OperationType.SEND_IMAGE, OperationType.INTENT),
                                    o_obj3, o_time, o_risk)
            o_list.append(o_info3)

    return o_list


# 远程Post传递信息
def get_post(o_time: OperationTime, login_ip: OperationIp, be_login_ip: OperationIp, o_risk: str, is_secret: bool) -> \
        List[OperationInfo]:
    o_obj = OperationObject(be_login_ip, NoneFileObject)
    o_type = OperationType(OperationType.SEND_POST, OperationType.INTENT)
    o_type2 = OperationType(OperationType.UNKNOWN, OperationType.INTENT)
    if is_secret:
        return [OperationInfo(-1, login_ip, o_type2, o_obj, o_time, o_risk)]
    else:
        return [OperationInfo(-1, login_ip, o_type, o_obj, o_time, o_risk)]


def __test1():
    pass


if __name__ == "__main__":
    __test1()
