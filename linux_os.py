#!/usr/bin/env python
#coding:utf-8
#get linux io infomation
#inverval 1 m exec py write log
#make:muxinqin@jkzl mxq 2017\06\09
#run linux_os.py must install iotop
#program del 3 before log
#linux_os.py version:1.0
"""

structure

class get_sys_io(object):


        def linux_io(self,num):

            '''''''''''''''''''''''
        def remove_log(self):
            ''''''''''''''''''''
Call two methods

linux_get.linux_io(90)
IO higher than 90

linux_get.remove_log()

delete io before 2 day log


"""
import os
import re
import time
import traceback



class get_sys_io(object):
    
    
    def __init__(self):
        self.local_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        self.log_path='/usr/local/script/'
        
    
    def linux_io(self,num):
        try:


            io_data=os.popen("iotop -Patbn1|awk '{print $1,$2,$5,$7,$11,$13}'|grep -v T").read()
    

    
            #io_data_l=[]
            list_io_data=((io_data).strip()).split('\n')
            n=0
            for m in range(len(list_io_data)):
                io_per=float(list_io_data[m].split(' ')[4])

                    
                if int(io_per)>num:
                    if n==0:
                        with open('{path}{log}io_get.log'.format(path=self.log_path,log=self.local_time),'a') as f:
                            head='time  pid  DISK READ  DISK WRITE  per program\n'
                            f.write(head)
                            f.write('\n')
                    n +=1
    
                    #io_data_l.append(list_io_data[m]+'\n')
                    
                    io_d=open('{path}{log}io_get.log'.format(path=self.log_path,log=self.local_time),'a')
    
                    io_d.write('  '+list_io_data[m]+'\n')
                    io_d.close()
        
        except Exception as e:
            traceback.print_exc()
            print e
        return 0
                
    def remove_log(self):
        record=os.system('find %s -mtime +3 -name "*.log" -exec rm {} \;'%(self.log_path) )
        with open('{path}{log}io_get.log'.format(path=self.log_path,log=self.local_time),'a') as f:
            f.write('delte time:'+self.local_time+'\n')
            if record==0:
                f.write("delte before 3 day log ok\n")
            else:
                f.write("delte before 3 day log fal\n")
        
        return 0
                
                

        
                #io_d.close()

                #io_data_l.append(list_io_data[m])
                
        #with open('/home/io_get_data.log','wta') as io_d:
            #io_d.write(list_io_data[m]+'\n')
         #   io_d.write(io_data_l)
        
if __name__=='__main__':
    
    src_time_num=time.time()
    while True:
        
        time.sleep(180)
        linux_get=get_sys_io()
        linux_get.linux_io(90)
        if time.time()>src_time_num:
            print 100
            src_time_num  +=15552000
        
            linux_get.remove_log()
            
