
class PyWay2SmsError(Exception):
    pass

class ConfigNotInitializedError(PyWay2SmsError):
    def __str__(self):
        return "Configuration initialization did not happen."

class ConfigFileNotFoundError(PyWay2SmsError):
    def __init__(self,cfg_file,cfg_path):
        self.cfg_file = cfg_file
        self.cfg_path = cfg_path
    def __str__(self):
        return "Configuration file not found: {}\n"+\
               "  Path:{}".format(self.cfg_file,self.cfg_path)

class ConfigFileInvalidError(PyWay2SmsError):
    def __init__(self,file_name,explanation=None):
        self.file_name = file_name
        self.explanation = explanation
    def __str__(self):
        s = "Configuration file is invalid: {} ".format(self.file_name)
        if self.explanation is not None:
            s+="\n  More Info:{}".format(self.explanation)
        return s

class Way2SmsAuthError(PyWay2SmsError):
    def __init__(self,username):
        self.username = username
    def __str__(self):
        return "Way2SMS Authentication Failed:\n  Username={} Password=******"\
            .format(self.username)
    pass

class InvalidInputError(PyWay2SmsError):
    def __init__(self,var_name,var_val,explanation):
        self.var_name = var_name
        self.var_val = var_val
        self.explanation = explanation
    def __str__(self):
        return "Invalid Input: {}={}".format(self.var_name,self.var_val) +\
               "\n  More Info: {}".format(self.explanation)

class MessageSendingFailedError(PyWay2SmsError):
    def __init__(self,explanation):
        self.explanation = explanation
    def __str__(self):
        return "Could not send message.\n" +\
                "  Explanation: {}".format(self.explanation)

