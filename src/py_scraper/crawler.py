import asyncio
import pyppeteer
from json import dumps
from Tools import TOOLS
from urllib import response
from pyppeteer import launch,connect

"""
Use this class to handle crawler
"""
class CRAWLER():
    def __init__(self): pass
    def open_page(self,url): pass
    def close_page(self): pass
    def open_tab(self): pass
    def scroll(self,type): pass

"""
Use this class to do request and intercept response(json ecc..)
"""
class INTERCEPT():
    def __init__(self):
        self.list_return_pics = []
        self.list_return_udata=[]
        self.list_return_hashdata=[]
        self.data_user_list = None
        self.data_tag_list = None
        self.next_max_id = None
        self.list_return_hashmedia = []
        self.viewport = { 'width': 960, 'height': 929}
        # self.executable_Path = "/usr/bin/google-chrome"
        self.executable_Path = "/snap/bin/firefox"
    """
    async def interceptResponse(self,response,type,json_tag=None):
        try:
            if "application/json" in response.headers.get("content-type", ""):
                try:
                    content = await response.json()
                    if type == "get_data_user_list":
                        self.data_user_list = content
                    elif type == "get_data_tag_list":
                        self.data_tag_list = content
                    else:
                        await self.scrape_json(json=content,type=type,json_tag=json_tag)
                except Exception as e:
                    pass
        except Exception as e:
            return False
    """
    """
    async def scrape_json(self,json,type,json_tag=None):
        try:
            if type == "user_media":
                if "data" in json or "user" in json:
                    await self.get_user_post_is22(data=json)
            elif type == "users_list":
                await self.search_profile_tags_is22(data=json)
            elif type == "tag_media":
                await self.search_ht_is22(data=json)
            elif type == "tag_list":
                await self.search_profile_tags_is22(data=json,need_tag=True)
            elif type == "user_tag_list":
                await self.search_profile_tags_is22(data=json,data_tag=json_tag)
        except Exception as e:
            return False
    """
    """
    async def get_user_post_is22(self,data):
        try:
            if data is not None:
                for nodes in data.get('data').get('user').get('edge_owner_to_timeline_media').get('edges'):
                    node =nodes.get('node')
                    if node.get('__typename') =='GraphImage':
                        media={
                            'original_image_dimensions':node.get('dimensions'),
                            'original_image': node.get('display_url'),
                            'image_id' : node.get('id'),
                            'image_shortcode':node.get('shortcode'),
                            'original_thumbnail':node.get('thumbnail_src')
                        }
                        try:
                            display_resources=node.get('display_resources')
                            if len(display_resources) >= 3:
                                media['crop_image_height']=display_resources[1].get('config_height')
                                media['crop_image_width']=display_resources[1].get('config_width')
                                media['crop_image']=display_resources[1].get('src')
                        except Exception as e:
                            pass
                        try:
                            list_thumbs = node.get('thumbnail_resources')
                            if len(list_thumbs)>=5:
                                media['crop_thumb_height']=list_thumbs[3].get('config_height')
                                media['crop_thumb_width']=list_thumbs[3].get('config_width')
                                media['crop_thumb'] =list_thumbs[3].get('src')
                        except Exception as e:
                            pass
                        self.list_return_pics.append(media)
                    else:
                        pass
                        #print("Media Type Video. Skipping")
            else:
                self.list_return_pics=[]
        except Exception as e:
            return False
    """
    """
    async def search_profile_tags_is22(self,
                                            data,
                                            data_tag,
                                            need_tag=True,
                                            need_user_list=True
                                            ):
            if data is not None:
                self.list_return_udata=[]
                self.list_return_hashdata=[]
                if need_tag:
                    for taglist in data_tag.get('hashtags'):
                        dict_hashdata={}
                        dict_hashdata['id']=taglist.get('hashtag').get('id')
                        dict_hashdata['media_count']=taglist.get('hashtag').get('media_count')
                        dict_hashdata['username']=taglist.get('hashtag').get('name')
                        dict_hashdata['profile_pic_url']=taglist.get('hashtag').get('profile_pic_url')
                        self.list_return_hashdata.append(dict_hashdata)
                if need_user_list:
                    for userlist in data.get('users'):
                        if not userlist.get('user').get('is_private'):
                            dict_udata = {}
                            position = userlist.get('position')
                            dict_udata['id']=userlist.get('user').get('pk')
                            dict_udata['username']=userlist.get('user').get('username')
                            dict_udata['fullname']=userlist.get('user').get('fullname')
                            dict_udata['profile_pic_url']=userlist.get('user').get('profile_pic_url')
                            self.list_return_udata.append(dict_udata)
                        else:
                            print("Private Profile {}- Skipping".format(userlist.get('user').get('username')))
            else:
                self.list_return_udata=[]
                self.list_return_hashdata=[]
    """
    """
    async def search_ht_is22(self,
                                data,
                                searchkey=None,
                                next_cursor=None,
                                translateurl=False,
                                minimum=20,
                                cur_iteration=0,
                                maxiteration=4
                                ):
        try:
            if data is not None:
                if self.next_max_id == None:
                    self.next_max_id=data.get('next_max_id')
                for tag_data in data.get('data').get('top').get('sections'):
                    dict_tagdata  ={}
                    for inner_obj in tag_data.get('layout_content').get('medias'):
                        mediadata = inner_obj.get('media')
                        try:
                            text = mediadata.get('caption').get('text')
                            if text is not None:
                                h_list = []
                                for element in text.split(' '):
                                    if element.startswith('#'):
                                        h_list.append(element.strip())
                                text = ' '.join(h_list)
                            dict_tagdata['text']=text
                        except Exception as text_error:
                            dict_tagdata['text']=None
                        if mediadata.get('image_versions2') is not None:
                            #has single media
                            dict_tagdata['id'] = mediadata.get('id')
                            listimages = mediadata.get('image_versions2').get('candidates')
                            if len(listimages)>=2:
                                #first in lisst is the big one then the thumbs
                                image_h = listimages[0].get('height')
                                image_w = listimages[0].get('width')
                                if translateurl:
                                    image=str(TOOLS().get_as_base64(listimages[0].get('url')))
                                else:
                                    image=listimages[0].get('url')

                                thumb_h = listimages[1].get('height')
                                thumb_w = listimages[1].get('width')
                                if translateurl:
                                    thumb=str(TOOLS().get_as_base64(listimages[1].get('url')))
                                else:
                                    thumb=listimages[1].get('url')
                            else:
                                #first in lisst is the big one then the thumbs
                                image_h = listimages[0].get('height')
                                image_w = listimages[0].get('width')
                                if translateurl:
                                    image=str(TOOLS().get_as_base64(listimages[0].get('url')))
                                else:
                                    image=listimages[0].get('url')

                                thumb_h = listimages[0].get('height')
                                thumb_w = listimages[0].get('width')
                                if translateurl:
                                    thumb=str(TOOLS().get_as_base64(listimages[0].get('url')))
                                else:
                                    thumb=listimages[0].get('url')
                        elif mediadata.get('carousel_media') is not None:
                            #has carousel medias
                            for fuckingcarousel in mediadata.get('carousel_media'):
                                dict_tagdata['id']=fuckingcarousel.get('id')

                                listimages = fuckingcarousel.get('image_versions2').get('candidates')
                                if len(listimages)>=2:
                                    #first in lisst is the big one then the thumbs
                                    image_h = listimages[0].get('height')
                                    image_w = listimages[0].get('width')
                                    if translateurl:
                                        image=str(TOOLS().get_as_base64(listimages[0].get('url')))
                                    else:
                                        image=listimages[0].get('url')

                                    thumb_h = listimages[1].get('height')
                                    thumb_w = listimages[1].get('width')
                                    if translateurl:
                                        thumb=str(TOOLS().get_as_base64(listimages[1].get('url')))
                                    else:
                                        thumb=listimages[1].get('url')
                                else:
                                    #first in lisst is the big one then the thumbs
                                    image_h = listimages[0].get('height')
                                    image_w = listimages[0].get('width')
                                    if translateurl:
                                        image=str(TOOLS().get_as_base64(listimages[0].get('url')))
                                    else:
                                        image=listimages[0].get('url')

                                    thumb_h = listimages[0].get('height')
                                    thumb_w = listimages[0].get('width')
                                    if translateurl:
                                        thumb=str(TOOLS().get_as_base64(listimages[0].get('url')))
                                    else:
                                        thumb=listimages[0].get('url')
                        dict_tagdata['image']={"image_h":image_h,"image_w":image_w,"image":image}
                        dict_tagdata['thumbnail']={"thumb_h":thumb_h,"thumb_w":thumb_w,"thumbnail":thumb}
                    self.list_return_hashmedia.append(dict_tagdata)
                    #rescounter+=1
                #if rescounter < minimum:
                    #newminimum = minimum-rescounter
                    #print("Not Enough Results still missing {} elements, running again".format(newminimum))
                    #search_ht_is22(searchkey,timeout,next_cursor=next_max_id,translateurl=translateurl,minimum=newminimum,list_return_hashmedia=list_return_hashmedia,cur_iteration=cur_iteration,maxiteration=4)
        except Exception as tagerror:
            #print("Error While Searching for Tag Media ->{}".format(tagerror))
            pass
        """
    async def return_user_media(self,q,type,user_data_dir,profile,headless=True):
        try:
            #https://www.netflix.com/browse/genre/34399?so=az #--> Movie A->Z
            browser = await launch({"headless":headless,"userDataDir":user_data_dir,"executablePath":self.executable_Path},
                                    handleSIGINT=False,
                                    handleSIGTERM=False,
                                    handleSIGHUP=False,
                                    args=[
                                    "--profile-directory={}".format(profile),
                                    '--no-sandbox',
                                    '--disable-setuid-sandbox',
                                    '--disable-dev-shm-usage',
                                    '--ignore-certificate-errors'
                                    ])
            page = await browser.newPage()
            await page.setViewport(self.viewport)
            #await page.goto(('https://www.instagram.com/{}/').format(q))
            await page.goto({}).format(q)
            await page.cookies()
            await page.content()
            new_results = page.on('response', lambda response: asyncio.ensure_future(self.interceptResponse(response,type)))
            await asyncio.sleep(3)
            await page.evaluate("""{window.scrollBy(0, document.body.scrollHeight);}""")
            await asyncio.sleep(2)
            await(browser.close())
            return self.list_return_pics
        except Exception as e:
            print(e)
            await(browser.close())
    async def return_users_list(self,q,type,user_data_dir,profile,headless=True):
        browser = await launch({"headless":headless,"userDataDir":user_data_dir,"executablePath":self.executable_Path},
                                handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                args=[
                                "--profile-directory={}".format(profile),
                                '--no-sandbox',
                                '--disable-setuid-sandbox',
                                '--disable-dev-shm-usage',
                                '--ignore-certificate-errors'
                                ])
        page = await browser.newPage()
        await page.goto(('https://www.instagram.com/web/search/topsearch/?context=blended&query={}&rank_token=0.8554460534132958&include_reel=true').format(q),{'waitUntil' : ['load', 'domcontentloaded']})
        await page.cookies()
        await page.content()
        new_results = page.on('response', lambda response: asyncio.ensure_future(self.interceptResponse(response,type="get_data_user_list")))
        await page.reload()
        await asyncio.sleep(3)
        await(browser.close())
        return self.data_user_list
    async def return_data_tag(self,q,type,user_data_dir,profile,headless=True):
        browser = await launch({"headless":headless,"userDataDir":user_data_dir,"executablePath":self.executable_Path},
                                handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                args=[
                                "--profile-directory={}".format(profile),
                                '--no-sandbox',
                                '--disable-setuid-sandbox',
                                '--disable-dev-shm-usage',
                                '--ignore-certificate-errors'
                                ])
        page = await browser.newPage()
        await page.setViewport(self.viewport)
        await page.goto(('https://www.instagram.com/explore/tags/{}/').format(q))
        await page.cookies()
        await page.content()
        new_results = page.on('response', lambda response: asyncio.ensure_future(self.interceptResponse(response,type)))
        await asyncio.sleep(3)
        await page.evaluate("""{window.scrollBy(0, document.body.scrollHeight);}""")
        await asyncio.sleep(2)
        await(browser.close())
        return({"next_max_id":self.next_max_id,"data":self.list_return_hashmedia})
    async def return_tag_list(self,q,type,user_data_dir,profile,headless=True):
        browser = await launch({"headless":headless,"userDataDir":user_data_dir,"executablePath":self.executable_Path},
                                handleSIGINT=False,
                                handleSIGTERM=False,
                                handleSIGHUP=False,
                                args=[
                                "--profile-directory={}".format(profile),
                                '--no-sandbox',
                                '--disable-setuid-sandbox',
                                '--disable-dev-shm-usage',
                                '--ignore-certificate-errors'
                                ])
        page = await browser.newPage()
        await page.setViewport(self.viewport)
        await page.goto(('https://www.instagram.com/web/search/topsearch/?context=blended&query=%23{}&rank_token=0.6237372945211862&include_reel=true').format(q),{'waitUntil' : ['load', 'domcontentloaded']})
        await page.cookies()
        await page.content()
        new_results = page.on('response', lambda response: asyncio.ensure_future(self.interceptResponse(response,type="get_data_tag_list")))
        await page.reload()
        await asyncio.sleep(2)
        await(browser.close())
        return self.data_tag_list
    async def return_user_tag_list(self,q,user_data_dir,type,profile,headless=True):
        data_user_list = await self.return_users_list(q=q,type=type,headless=headless,user_data_dir=user_data_dir,profile=profile)
        data_tag_list = await self.return_tag_list(q=q,type=type,headless=headless,user_data_dir=user_data_dir,profile=profile)
        for taglist in data_tag_list.get('hashtags'):
            dict_hashdata={}
            dict_hashdata['id']=taglist.get('hashtag').get('id')
            dict_hashdata['media_count']=taglist.get('hashtag').get('media_count')
            dict_hashdata['username']=taglist.get('hashtag').get('name')
            dict_hashdata['profile_pic_url']=taglist.get('hashtag').get('profile_pic_url')
            self.list_return_hashdata.append(dict_hashdata)
        for userlist in data_user_list.get('users'):
            if not userlist.get('user').get('is_private'):
                dict_udata = {}
                position = userlist.get('position')
                dict_udata['id']=userlist.get('user').get('pk')
                dict_udata['username']=userlist.get('user').get('username')
                dict_udata['fullname']=userlist.get('user').get('fullname')
                dict_udata['profile_pic_url']=userlist.get('user').get('profile_pic_url')
                self.list_return_udata.append(dict_udata)
            else:
                print("Private Profile {}- Skipping".format(userlist.get('user').get('username')))
        return (dumps({"hash":self.list_return_hashdata,"user":self.list_return_udata}))