#coding: GBK
#md5 SHA1�ļ�У��ֵ����
#ʹ�÷����� python �ļ�.py  ��֤�ļ�
import hashlib
import sys
import os
def md5_sum(filename):     #�ļ�У��ֵ���㷽��
    fd=open(filename,"rb") #���ļ�
    fd.seek(0)             #���ļ����������Ƶ�offset��λ��
    line=fd.readline()     #��ȡ�ļ���һ�н���line
    
    #md5У��ֵ����
    md5=hashlib.md5()
    md5.update(line)
    #SHA1У��ֵ����
    sha1=hashlib.sha1()
    sha1.update(line)
    
    while line:         #ѭ����ȡ�ļ�
        line=fd.readline()
        md5.update(line)
        sha1.update(line)
        
    fmd5=md5.hexdigest()  #�����ļ�MD5У��ֵ
    fsha1=sha1.hexdigest()#�����ļ�SHA1У��ֵ
    
    fsum=[fmd5,fsha1]

    fd.close()
    
    return fsum

def m_help():            #�����������
    st_help='''
**************************************************
**  MD5 SHA1 У��ʹ�ð���                
**  �ļ�У��ֵ�� python md5.py file         
**  Example: python md5.py d:/1/1.txt
**  �ļ��Աȣ� python md5.py �ļ�1 �ļ�2
**  Example: python md5.py d:/1/1.txt d:/1/2.txt
***************************************************'''
    print st_help

def dis_view(fmd5,filename): #�������
    print 'File: {}'.format(filename)
    print 'MD5 : {}'.format(fmd5[0])
    print 'SHA1: {}'.format(fmd5[1])

def file_err():  #������ʾ����
    er='''
====================�������======================'''
    print er
    m_help()
    
    
def file_check(file1,file2): #�ļ��Աȷ���
    f1_md5=md5_sum(file1)
    f2_md5=md5_sum(file2)
    
    dis_view(f1_md5,file1)
    dis_view(f2_md5,file2)

    if f1_md5[0]==f2_md5[0] and f1_md5[1]==f2_md5[1]:
        print "�ļ���{} ���ļ�:{}MD5��SHA1У��ֵ��ͬ��".format(file1,file2)
    else:
        print "�ļ���{} ���ļ�:{}MD5��SHA1У��ֵ����ͬ��".format(file1,file2)
        
       

if __name__ == "__main__":
    try:
        file2=sys.argv[2]
        file1=sys.argv[1]

        if os.path.isfile(file1) and os.path.isfile(file2):     #�ļ�·��У��
           file_check(file1,file2)  #�����ļ��Աȷ���
        else:                   #�������˵�
            file_err()
    except Exception:
        try:
            file1=sys.argv[1]
            if file1=='--help' or file1=='':  #���ð�������
                m_help() 
            elif os.path.isfile(file1):     #�ļ�·��У��
                fmd5=md5_sum(file1)   #�����ļ�У��ֵ���㷽��
                dis_view(fmd5,file1)
            else:                   #���ô���˵�
                file_err()
        except:
            m_help()




    
    

