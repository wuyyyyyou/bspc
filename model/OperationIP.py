class OperationIp:
    # belong_to
    INTRANET = "INTRANET"  # 内网主机IP
    EXTRANET = "EXTRANET"  # 外网域名IP
    # ip_safety_level
    USER = "USER"  # 普通用户主机
    ADMINISTRATOR = "ADMINISTRATOR"  # 管理员主机
    SECURE = "SECURE"  # 公有域名
    DANGEROUS = "DANGEROUS"  # 危险域名

    def __init__(self, ip_address: str, ip_belong_to: str, ip_safety_level: str):
        self.ip_address = ip_address
        self.ip_belong_to = ip_belong_to
        self.ip_safety_level = ip_safety_level

    def __repr__(self):
        return "[{},{},{}]".format(self.ip_address, self.ip_belong_to, self.ip_safety_level)

    def __str__(self):
        return "[{},{},{}]".format(self.ip_address, self.ip_belong_to, self.ip_safety_level)
