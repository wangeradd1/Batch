#coding=utf-8

from google import search
import mysql.connector
import re
import sys

url_action = re.compile(r'.*?\.action')
url_do = re.compile(r'.*?\.do')
url_replace = re.compile(r'!.*?\.action')

def url_cut(url):
    matched = None
    if url_action.search(url):
        matched = url_action.search(url)
        if matched:
            replace = url_replace.search(matched.group())
            if replace:
                newurl=url_replace.sub('.action',matched.group())
                return newurl
            else:
                return matched.group()
    elif url_do.search(url):
        matched = url_do.search(url)
        return matched.group()
    else:
        return None
        
config = {
'host':'192.168.149.136',
'user':'toor',
'password':'changeme',
'port':'3306',
'database':'google'
}

if len(sys.argv) ==2:
    keywords = sys.argv[1]
    try:
        con = mysql.connector.connect(**config)
        cursor=con.cursor()
        for url in search(keywords,tld = 'hk',lang = 'zh',num = 100,stop = 1000):
            format_url = url_cut(url)
            if format_url:
                sqlstr = "insert into struts2(url,format_url) values (\'{0}\',\'{1}\')".format(url,format_url)
                cursor.execute(sqlstr)
        con.commit()
    except mysql.connector.Error as e:
        print "Error: {}".format(e)
        exit()


