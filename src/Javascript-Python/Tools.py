import os
import base64
import requests

"""
Use this class to handle tools
"""
class TOOLS():
    def __init__(self):
        self.user = self.get_user()
    def get_as_base64(self,url):
        try:
            return base64.b64encode(requests.get(url).content)
        except Exception as e:
            return False
    def get_profile(self,
                        profile1,
                        profile1_is_busy,
                        profile2,
                        profile2_is_busy,
                        profile3,
                        profile3_is_busy,
                        profile4,
                        profile4_is_busy,
                        profile5,
                        profile5_is_busy
                        ):
        try:
            if profile1_is_busy == False:
                return profile1
            elif profile2_is_busy == False:
                return profile2
            elif profile3_is_busy == False:
                return profile3
            elif profile4_is_busy == False:
                return profile4
            elif profile5_is_busy == False:
                return profile5
        except Exception as e:
            return False
    def get_user_data_dir(self,profile):
        try:
            if profile == "Default":
               return "/home/{}/.config/google-chrome/".format(self.user)
            elif profile == "Profile 1":
               return "/home/{}/.config/google-chrome2/".format(self.user)
            elif profile == "Profile 2":
               return "/home/{}/.config/google-chrome3/".format(self.user)       
            elif profile == "Profile 3":
               return "/home/{}/.config/google-chrome4/".format(self.user)                           
            elif profile == "Profile 4":
               return "/home/{}/.config/google-chrome5/".format(self.user)       
        except Exception as e:
               return False
    def get_user(self):
        try:
            return os.environ.get("USER")
        except Exception as e:
            return False
