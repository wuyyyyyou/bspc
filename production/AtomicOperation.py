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
    return [OperationInfo(-1, o_ip, OperationType.READ, o_object, o_time, o_risk)]


# 写文件操作
def write_file(o_time: OperationTime, o_ip: OperationIp, o_object: OperationObject, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType.WRITE, o_object, o_time, o_risk)]


# 运行文件操作
def run_file(o_time: OperationTime, o_ip: OperationIp, o_object: OperationObject, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType.RUN, o_object, o_time, o_risk)]


# 开启摄像头
def open_camera(o_time: OperationTime, o_ip: OperationIp, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType.CAMERA, HostOperationObject, o_time, o_risk)]


# 开启麦克风
def open_microphone(o_time: OperationTime, o_ip: OperationIp, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType.MICROPHONE, HostOperationObject, o_time, o_risk)]


# 提升权限
def elevated_privileges(o_time: OperationTime, o_ip: OperationIp, o_risk: str) -> List[
    OperationInfo]:
    return [OperationInfo(-1, o_ip, OperationType.APPLY, HostOperationObject, o_time, o_risk)]


# 远程登陆
def remote_login(o_time: OperationTime, login_ip: OperationIp, be_login_ip: OperationIp, o_risk: str):
    pass
