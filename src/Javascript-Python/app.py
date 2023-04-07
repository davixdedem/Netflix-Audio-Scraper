#!/usr/bin/env python3
import json
import asyncio
from Tools import TOOLS
from flask_cors import CORS
from Intercept import INTERCEPT
from flask.json import JSONEncoder
from common_function import CommonFunction
from datetime import datetime,timedelta,date
from flask import Flask,jsonify,request,abort,flash,redirect,url_for,render_template

"""
Konst
"""
HOST = '0.0.0.0'
PORT = '8889'

"""
Manipulate date object flask to avoid translation
"""
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

"""
Main class
"""
class MyFlaskApp:
    def __init__(self):
        self.app = Flask(__name__,template_folder='html_template')
        self.app.json_encoder = CustomJSONEncoder
        self.app.add_url_rule(rule="/instapi/v2.0/GetUserTag",view_func=self.create_task_GetUsersTagsList,methods=['POST'])
        self.app.add_url_rule(rule="/instapi/v2.0/GetUserMedia",view_func=self.create_task_GetUserMedia,methods=['POST'])
        self.app.add_url_rule(rule="/instapi/v2.0/GetTagMedia",view_func=self.create_task_GetTagMedia,methods=['POST'])
        CORS(self.app)
        self.profile_one_is_busy = False
        self.profile_two_is_busy = False
        self.profile_three_is_busy = False
        self.profile_four_is_busy = False
        self.profile_five_is_busy = False
        self.profile_one = "Default"
        self.profile_two = "Profile 1"
        self.profile_three = "Profile 2"
        self.profile_four = "Profile 3"
        self.profile_five = "Profile 4"
        self.app.run(HOST,PORT,debug=True)
    def create_task_GetUsersTagsList(self):
        free_profile = TOOLS().get_profile(profile1=self.profile_one,
                                                profile2=self.profile_two,
                                                profile3=self.profile_three,
                                                profile4=self.profile_four,
                                                profile5=self.profile_five,
                                                profile1_is_busy=self.profile_one_is_busy,
                                                profile2_is_busy=self.profile_two_is_busy,
                                                profile3_is_busy=self.profile_three_is_busy,
                                                profile4_is_busy=self.profile_four_is_busy,
                                                profile5_is_busy=self.profile_five_is_busy)
        user_data_dir = TOOLS().get_user_data_dir(profile=free_profile)
        if free_profile == self.profile_one:
            self.profile_one_is_busy = True
        elif free_profile == self.profile_two:
            self.profile_two_is_busy = True      
        elif free_profile == self.profile_three:
            self.profile_three_is_busy = True   
        elif free_profile == self.profile_four:
            self.profile_four_is_busy = True      
        elif free_profile == self.profile_five:
            self.profile_five_is_busy = True  
        client_ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        list_mandatory_keys=['insta_id','searchkey']
        if request.method == 'POST':
            if not request.json or not 'token':
                print("Missing Token In Request from client {}".format(client_ip),"warning")
                abort(400)
            if (request.json.get('token')!=CommonFunction().fetch_cur_apikey()):
                print("Wrong Token In Request from client {}".format(client_ip),"warning")
                abort(400)
            print("Session Token IS VALID from ip  {}. GOING ON ".format(client_ip),"info")
            for element in list_mandatory_keys:
                if request.json.get(element) is None:
                    print("Missing Mandatory Data  {}".format(element),"warning")
                    abort(400)
            print("Requested GetUsersList from ce {}".format(request.json.get('insta_id')))
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            data = loop.run_until_complete(INTERCEPT().return_user_tag_list(q=request.json.get('searchkey'),type="user_tag_list",headless=True,profile=free_profile,user_data_dir=user_data_dir))
            if free_profile == self.profile_one:
                self.profile_one_is_busy = False
            elif free_profile == self.profile_two:
                self.profile_two_is_busy = False      
            elif free_profile == self.profile_three:
                self.profile_three_is_busy = False   
            elif free_profile == self.profile_four:
                self.profile_four_is_busy = False      
            elif free_profile == self.profile_five:
                self.profile_five_is_busy = False  
            return jsonify({"exit-code":True,"reason":"ALL FUCKING FINE","data":data}),200
    def create_task_GetUserMedia(self):
        free_profile = TOOLS().get_profile(profile1=self.profile_one,
                                                profile2=self.profile_two,
                                                profile3=self.profile_three,
                                                profile4=self.profile_four,
                                                profile5=self.profile_five,
                                                profile1_is_busy=self.profile_one_is_busy,
                                                profile2_is_busy=self.profile_two_is_busy,
                                                profile3_is_busy=self.profile_three_is_busy,
                                                profile4_is_busy=self.profile_four_is_busy,
                                                profile5_is_busy=self.profile_five_is_busy)
        user_data_dir = TOOLS().get_user_data_dir(profile=free_profile)
        if free_profile == self.profile_one:
            self.profile_one_is_busy = True
        elif free_profile == self.profile_two:
            self.profile_two_is_busy = True      
        elif free_profile == self.profile_three:
            self.profile_three_is_busy = True   
        elif free_profile == self.profile_four:
            self.profile_four_is_busy = True      
        elif free_profile == self.profile_five:
            self.profile_five_is_busy = True  
        client_ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        list_mandatory_keys=['insta_id','searchkey']
        if request.method == 'POST':
            if not request.json or not 'token':
                print("Missing Token In Request from client {}".format(client_ip),"warning")
                abort(400)
            if (request.json.get('token')!=CommonFunction().fetch_cur_apikey()):
                print("Wrong Token In Request from client {}".format(client_ip),"warning")
                abort(400)
            print("Session Token IS VALID from ip  {}. GOING ON ".format(client_ip),"info")
            for element in list_mandatory_keys:
                if request.json.get(element) is None:
                    print("Missing Mandatory Data  {}".format(element),"warning")
                    abort(400)
            print("Requested GetUsersList from ce {}".format(request.json.get('insta_id')))
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            data = loop.run_until_complete(INTERCEPT().return_user_media(q=request.json.get('searchkey'),type="user_media",headless=True,profile=free_profile,user_data_dir=user_data_dir))
            if free_profile == self.profile_one:
                self.profile_one_is_busy = False
            elif free_profile == self.profile_two:
                self.profile_two_is_busy = False      
            elif free_profile == self.profile_three:
                self.profile_three_is_busy = False   
            elif free_profile == self.profile_four:
                self.profile_four_is_busy = False      
            elif free_profile == self.profile_five:
                self.profile_five_is_busy = False  
            return jsonify({"exit-code":True,"reason":"ALL FUCKING FINE","data":data}),200
    def create_task_GetTagMedia(self):
        free_profile = TOOLS().get_profile(profile1=self.profile_one,
                                                profile2=self.profile_two,
                                                profile3=self.profile_three,
                                                profile4=self.profile_four,
                                                profile5=self.profile_five,
                                                profile1_is_busy=self.profile_one_is_busy,
                                                profile2_is_busy=self.profile_two_is_busy,
                                                profile3_is_busy=self.profile_three_is_busy,
                                                profile4_is_busy=self.profile_four_is_busy,
                                                profile5_is_busy=self.profile_five_is_busy)
        user_data_dir = TOOLS().get_user_data_dir(profile=free_profile)
        if free_profile == self.profile_one:
            self.profile_one_is_busy = True
        elif free_profile == self.profile_two:
            self.profile_two_is_busy = True      
        elif free_profile == self.profile_three:
            self.profile_three_is_busy = True   
        elif free_profile == self.profile_four:
            self.profile_four_is_busy = True      
        elif free_profile == self.profile_five:
            self.profile_five_is_busy = True  
        client_ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        list_mandatory_keys=['insta_id','searchkey']
        if request.method == 'POST':
            if not request.json or not 'token':
                print("Missing Token In Request from client {}".format(client_ip),"warning")
                abort(400)
            if (request.json.get('token')!=CommonFunction().fetch_cur_apikey()):
                print("Wrong Token In Request from client {}".format(client_ip),"warning")
                abort(400)
            print("Session Token IS VALID from ip  {}. GOING ON ".format(client_ip),"info")
            for element in list_mandatory_keys:
                if request.json.get(element) is None:
                    print("Missing Mandatory Data  {}".format(element),"warning")
                    abort(400)
            print("Requested GetUsersList from ce {}".format(request.json.get('insta_id')))
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            data = loop.run_until_complete(INTERCEPT().return_data_tag(q=request.json.get('searchkey'),type="tag_media",headless=True,profile=free_profile,user_data_dir=user_data_dir))
            if free_profile == self.profile_one:
                self.profile_one_is_busy = False
            elif free_profile == self.profile_two:
                self.profile_two_is_busy = False      
            elif free_profile == self.profile_three:
                self.profile_three_is_busy = False   
            elif free_profile == self.profile_four:
                self.profile_four_is_busy = False      
            elif free_profile == self.profile_five:
                self.profile_five_is_busy = False  
            return jsonify({"exit-code":True,"reason":"ALL FUCKING FINE","data":data}),200   

if __name__ == '__main__': 
    MyFlaskApp()
