class FileSignatureEntity(object):
    def __init__(self):
        self.skip = 0
        self.codes_str = ""
        self.codes = []
        self.file_type = ""
        self.code_desc = ""
        self.desc = ""

    def __init__(self, skip, codes_str, file_type, code_desc, file_desc):
        self.skip = skip
        self.codes_str = codes_str
        if codes_str:
            self.codes = codes_str.split(" ")
        else:
            self.codes = []
        self.file_type = file_type
        self.code_desc = code_desc
        self.desc = file_desc
