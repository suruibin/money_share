# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:20:51 2019

@author: Suruibin
"""

import os,struct

def mkdir(path):
    path=path.strip()
    path=path.rstrip("/")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        #print path+' 创建成功'
        return True
    
mkdir("T0002/dlls/")
mkdir("T0002/blocknew/")

for i in range(1,21):
    dirs="T0002/signals/signals_user_"  +str(i)
    mkdir(dirs)

#创建通达信Signals数据函数
def Create_Tdx_Signals(stock_file_name,net_time,money):

    
    if not os.path.isfile(stock_file_name):
        with open(stock_file_name,"wb+") as newfile:
            write_data=struct.pack('if',net_time,money) #最新数据包
            newfile.write(write_data)
            return 0
    #创建通达信gignals数据
    with open(stock_file_name,'rb+') as fwr:
        fwr.seek(0,os.SEEK_END)
        #print(stock_file_name)
        if(fwr.tell() ==0):
            fwr.seek(0,os.SEEK_END)
            write_data=struct.pack('if',net_time,money) #最新数据包
            fwr.write(write_data)
        else:
            fwr.seek(-8,os.SEEK_END)
        read_lhb_data=fwr.read()
        lhbread_date,lhbread_data=struct.unpack("if",read_lhb_data)#读取文件时间
        #print num,lhbread_date,lhbread_data
        write_lhb_data=struct.pack('if',net_time,money) #最新数据包

        if net_time > lhbread_date:
            #print "新日期\n"
            fwr.seek(0,os.SEEK_END)
            fwr.write(write_lhb_data)
            
        if net_time == lhbread_date: #and lhbread_data != money:
            fwr.seek(-8,os.SEEK_END)
            fwr.write(write_lhb_data)