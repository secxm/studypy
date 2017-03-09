#coding: GBK
#md5 SHA1文件校验值计算
#使用方法： python 文件.py  验证文件
import hashlib
import sys
import os
def md5_sum(filename):     #文件校验值计算方法
    fd=open(filename,"rb") #打开文件
    fd.seek(0)             #将文件打操作标记移到offset的位置
    line=fd.readline()     #读取文件第一行进入line
    
    #md5校验值计算
    md5=hashlib.md5()
    md5.update(line)
    #SHA1校验值计算
    sha1=hashlib.sha1()
    sha1.update(line)
    
    while line:         #循环读取文件
        line=fd.readline()
        md5.update(line)
        sha1.update(line)
        
    fmd5=md5.hexdigest()  #生成文件MD5校验值
    fsha1=sha1.hexdigest()#生成文件SHA1校验值
    
    fsum=[fmd5,fsha1]

    fd.close()
    
    return fsum

def m_help():            #程序帮助方法
    st_help='''
**************************************************
**  MD5 SHA1 校验使用帮助                
**  文件校验值： python md5.py file         
**  Example: python md5.py d:/1/1.txt
**  文件对比： python md5.py 文件1 文件2
**  Example: python md5.py d:/1/1.txt d:/1/2.txt
***************************************************'''
    print st_help

def dis_view(fmd5,filename): #输出方法
    print 'File: {}'.format(filename)
    print 'MD5 : {}'.format(fmd5[0])
    print 'SHA1: {}'.format(fmd5[1])

def file_err():  #错误显示方法
    er='''
====================输入错误======================'''
    print er
    m_help()
    
    
def file_check(file1,file2): #文件对比方法
    f1_md5=md5_sum(file1)
    f2_md5=md5_sum(file2)
    
    dis_view(f1_md5,file1)
    dis_view(f2_md5,file2)

    if f1_md5[0]==f2_md5[0] and f1_md5[1]==f2_md5[1]:
        print "文件：{} 与文件:{}MD5、SHA1校验值相同！".format(file1,file2)
    else:
        print "文件：{} 与文件:{}MD5、SHA1校验值不相同！".format(file1,file2)
        
       

if __name__ == "__main__":
    try:
        file2=sys.argv[2]
        file1=sys.argv[1]

        if os.path.isfile(file1) and os.path.isfile(file2):     #文件路径校验
           file_check(file1,file2)  #调用文件对比方法
        else:                   #进入错误菜单
            file_err()
    except Exception:
        try:
            file1=sys.argv[1]
            if file1=='--help' or file1=='':  #调用帮助方法
                m_help() 
            elif os.path.isfile(file1):     #文件路径校验
                fmd5=md5_sum(file1)   #调用文件校验值计算方法
                dis_view(fmd5,file1)
            else:                   #调用错误菜单
                file_err()
        except:
            m_help()




    
    

