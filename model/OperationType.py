class OperationType:
    READ = "READ"
    WRITE = "WRITE"
    RUN = "RUN"
    CAMERA = "CAMERA"
    MICROPHONE = "MICROPHONE"
    APPLY = "APPLY"  # 申请权限
    REMOTE = "REMOTE"  # 远程登陆
    GET_HTML = "GET_HTML"  # 阅览网页
    GET_FILE = "GET_FILE"
    GET_VIDEO = "GET_VIDEO"
    GET_AUDIO = "GET_AUDIO"
    GET_IMAGE = "GET_IMAGE"
    GET_POST = "GET_POST"
    SEND_FILE = "SEND_FILE"
    SEND_VIDEO = "SEND_VIDEO"
    SEND_AUDIO = "SEND_AUDIO"
    SEND_IMAGE = "SEND_IMAGE"
    SEND_POST = "SEND_POST"
    UNKNOWN = "UNKNOWN"
    # belong_to
    INTENT = "INTENT"
    LOCAL = "LOCAL"

    def __init__(self, operation_type: str, o_type_belong_to: str):
        self.operation_type = operation_type
        self.o_type_belong_to = o_type_belong_to

    def __repr__(self):
        return "[{},{}]".format(self.operation_type, self.o_type_belong_to)

    def __str__(self):
        return "[{},{}]".format(self.operation_type, self.o_type_belong_to)
