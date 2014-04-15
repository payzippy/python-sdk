import hashlib
import urllib

from payzippysdk import Config, Constants


class HashUtil:
    def __init__(self, params, hash_mode):
        self.params = params
        self.secret_key = Config.secret_key
        self.hash_mode = str(hash_mode)

    def generate_hash(self):
        str_val = ''
        key_list = sorted(self.params.keys())
        for key in key_list:
            if not key == Constants.HASH:
                if type(self.params.get(key)) is list:
                    str_val += self.get_list_as_str(self.params.get(key))
                elif type(self.params.get(key)) is dict:
                    str_val += self.get_dict_as_str(self.params.get(key))
                else:
                    val = self.params.get(key)
                    str_val += self.get_formatted_str(val)
        str_val += self.secret_key

        if self.hash_mode.lower() is "md5":
            m = hashlib.md5()
            m.update(str_val)
            return m.hexdigest()
        else:
            m = hashlib.sha256()
            m.update(str_val)
            return m.hexdigest()

    def get_formatted_str(self, str_param):
        val = urllib.unquote(str(str_param))
        val = urllib.unquote_plus(val)
        if val == "True" or val == "False":
            val = val.lower()
        return val + "|"

    def get_list_as_str(self, list_param):
        str_val = ''
        for each_data in list_param:
            if type(each_data) is dict:
                str_val += self.get_dict_as_str(each_data)
            else:
                str_val += self.get_formatted_str(each_data)
        return str_val

    def get_dict_as_str(self, dict_param):
        str_val = ''
        key_list = sorted(dict_param.keys())
        for key in key_list:
            val = dict_param.get(key)
            str_val += self.get_formatted_str(val)
        return str_val
