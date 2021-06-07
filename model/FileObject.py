class FileObject:
    FILE = "FILE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    # file_location
    SYSTEM = "SYSTEM"
    EXTERNAL = "EXTERNAL"
    NORMAL = "NORMAL"

    def __init__(self, file_type: str, file_location: str):
        self.file_type = file_type
        self.file_location = file_location

    def __repr__(self):
        return "[{},{}]".format(self.file_type, self.file_location)

    def __str__(self):
        return "[{},{}]".format(self.file_type, self.file_location)


NoneFileObject = FileObject("", "")
