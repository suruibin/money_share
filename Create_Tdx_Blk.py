# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:00:37 2019

@author: Suruibin
"""
import os

def mkdir(path):
    path=path.strip()
    path=path.rstrip("/")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        #print path+' 创建成功'
        return True
    
def Init_Tdx_Blks(blk):
    #print(__name__)
    blk_dir="T0002/blocknew/"
    blk_name=blk_dir+blk
    if not os.path.exists(blk):
        mkdir(blk_dir)
        bk=open(blk_name,'w')
        bk.close()

def Create_Tdx_Blks(code,blk): #创建预警池
    headers = {'User-Agent': 'Mozilla/7.2 (Linux; U; Android 8.1; zh-cn; EVA-AL10 Build/HUAWEIEVA) AppleWebKit/647.16 (KHTML, like Gecko)Version/7.0 Chrome/65.6.1.2 MQQBrowser/9.9 Mobile Safari/834.44',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': '_hc.v=aee6087a-12cy-5d94-975f-405a135f8ibb.1285063275; s_ViewType=10; _tr.u=tTd0c7RuJVVi5yyF; download_banner=on; cityid=2; __mta=55208432.1688472762111.1489540176986.1489530849254.7; PHOENIX_ID=4a120948-25c65are8fa-30a99b7; aburl=1; cy=2; cye=beijing; default_ab=shop%3AA%3A1%7Cshopreviewlist%3AA%3A1; __mta=55808532.1489472362111.1489570116986.1492060873556.7'}
    blk_name="./T0002/blocknew/" +blk
    with open(blk_name,"r+") as frw:
        frw.seek(0,os.SEEK_END)
        if code[0] == '0' or code[0] =='3' :
            code_data = "0"+code+"\n"
        else:
            code_data = "1"+code+"\n"
        frw.write(code_data)