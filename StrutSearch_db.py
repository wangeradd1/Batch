#coding=utf-8



from google import search

import mysql.connector

import re

import sys



url_action = re.compile(r'.*?//.*?/.*?\.action')

url_do = re.compile(r'.*?//.*?/.*?\.do')

action_replace = re.compile(r'!.*?\.action')

do_replace = re.compile(r'!.*?\.do')

quote = re.compile(r'\'')



def url_cut(url):

    if url_action.search(url):

        matched = url_action.search(url)

        if matched:

            replace = action_replace.search(matched.group())

            if replace:

                newurl = action_replace.sub('.action',matched.group())

                return newurl

            else:

                return matched.group()

    elif url_do.search(url):

        matched = url_do.search(url)

        if matched:

            replace = do_replace.search(matched.group())

            if replace:

                newurl = do_replace.sub('.do',matched.group())

                return newurl

            else:

                return matched.group()

    else:

        return None

        

config = {

'host':'127.0.0.1',

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

            print url

            format_url = url_cut(url)

            print format_url

            if format_url:

                url = quote.sub('%27',url)

                format_url = quote.sub('%27',format_url)

                sqlstr = "insert into struts2(url,format_url) values (\'{0}\',\'{1}\')".format(url,format_url)

                cursor.execute(sqlstr)

                con.commit()

    except mysql.connector.Error as e:

        print "Error: {}".format(e)

        exit()



