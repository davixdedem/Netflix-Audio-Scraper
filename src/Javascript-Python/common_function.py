import random
import string
import hashlib
import datetime
from datetime import timedelta

"""
Use this class to handle Tools
"""
class CommonFunction():
    def fetch_cur_apikey(self):
        try:
            now = datetime.datetime.now()
            key= int(now.year)*int(now.month)* int(now.day)*int(now.hour)*int(now.minute)+6879
            key_enc = self.computeMD5hash(str(key))
            #print("token is {}".format(key_enc))
            return(key_enc)
        except Exception as e:
            return False
    def generate_token(self,stringLength=12):
        try:
            """Generate a random string of letters and digits """
            lettersAndDigits = string.ascii_letters + string.digits
            rndstr= ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
            return(self.computeMD5hash(rndstr))
        except Exception as e:
            return False
    def computeMD5hash(self,my_string):
        try:
            m = hashlib.md5()
            m.update(my_string.encode('utf-8'))
            return m.hexdigest()
        except Exception as e:
            return False