# Batch
Catch vulnerable targets on the Internet~
## s2-032_Gsearch.py

使用google搜索批量找s2-032<br>
首先，您需要安装googleAPI库:<br>
git clone https://github.com/MarioVilas/google.git<br>
注意：您可能需要代理或者VPN来访问google，如果抛出503异常，请切换代理或者更换VPN接入点<br>
使用方法:<br>
python s2-032_Gsearch.py 'filetype:action 机构'<br>
python s2-032_Gsearch.py 'filetype:do 单位'<br>

##StrutSearch_db.py
使用google抓取使用Apache Struts2框架站点，并用mysql存储您的搜索结果<br>
注意，这也需要安装googleAPI库：https://github.com/MarioVilas/google.git<br>
您可能需要代理或者VPN来访问google，如果抛出503异常，请切换代理或者更换VPN接入点<br>
使用方法:<br>
首先，您需要安装mysql官方提供的python接口：<br>

http://dev.mysql.com/downloads/connector/python/1.0.html<br>

然后新建一个数据库(如果需要)：<br>

MySQL>create datebase google;<br>

新建表：
MySQL>CREATE TABLE `struts2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` text NOT NULL,
  `format_url` varchar(255) NOT NULL,
  `s2032` int(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8

注意：请更改代码中config信息为您的mysql连接信息

然后像这样:<br>
python StrutSearch_db.py 'filetype:do .com'<br>
python StrutSearch_db.py 'filetype:action .cn'<br>

然后看数据库中是不是有很多数据了，如果多执行几次会有很多的数据<br>

##s2-032_batch.py

多线程验证数据库中的url是否有S2-032（默认100个线程），如果捕获到，打印出url，并将表中对应的s2032列设为1<br>

注意：请更改代码中config信息为您的mysql连接信息<br>

使用方法：首先用StrutSearch_db.py尽可能多的获取数据，然后像这样：<br>
python s2-032_batch.py



