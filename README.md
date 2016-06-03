## 招聘网数据库查询系统说明
### 1系统介绍
1)操作系统 系统搭建在Ubuntu系统上。Ubuntu是一免费开源操作系统，是基于Linux的发行版本，具有开放性和高性价比等显著特点。同时Ubuntu具有庞大的社区力量支持，可以方便地从社区获得帮助。系统选用的是Ubuntu14.04版本，该版本代号为“Trusty Tahr”（值得信赖的塔尔羊），是一个长期支持版本，有很好的性能和交互性。

2）开发语言 系统主要使用python，python是一种完全面向对象、解释型计算机程序设计语言，语法简洁清晰，拥有丰富和强大的库，易读且易维护，提供API，能方便进行维护和管理。

3）数据库管理系统 
系统选用SQLite数据库，SQLite是遵守ACID的关系数据库管理系统，它包含在一个相对小的C程式库中。与许多其它数据库管理系统不同，SQLite不是一个客户端/服务器结构的数据库引擎，而是被集成在用户程序中。

4）开发框架 系统选用Django框架，Django是一个开放源代码的Web应用框架，由Python写成。采用了MVC的软件设计模式。它强调代码复用,多个组件可以很方便的以“插件”形式服务于整个框架，有许多功能强大的第三方插件，具有很强的可扩展性。
### 2界面展示
#### 2.1登陆界面
 ![登陆界面][4]
输入账号和密码，查询数据库并于密码匹配成功后可登陆

![登录失败1][5] ![登录失败2][6]
若查询失败则无法登陆
#### 2.2普通用户登录
 ![普通用户登录][7]
获得用户详细信息，和对应的简历列表

![简历的详细信息][8]
每份简历的详细信息
#### 2.3企业用户登录
 ![企业用户详细信息][9]
获得企业用户详细信息，和对应的发布的招聘信息列表

![详细招聘信息][10]
每条招聘的详细招聘信息

![对应该招聘投放的简历][11]
以及对应该招聘投放的简历

#### 2.4数据库后台管理
![此处输入图片的描述][12]

用来管理数据库的后台，实现增删查改。
### 3 系统使用说明
系统运行需求：

系统环境：ubuntu14.04/OS X

程序语言：python 2.7.+

框架: django 1.8.0+

系统下载:
使用github下载：

git clone https://github.com/Hareric/dbBigHW.git

直接下载：

https://github.com/Hareric/dbBigHW/archive/master.zip


系统运行：

进入该系统根目录，终端下执行python manage.py runserver开启本地服务器

浏览器访问: 127.0.0.1:8000/home 进入查询页面

浏览器访问: 127.0.0.1:8000/admin 进入数据库后台管理页面

管理员帐号: admin 密码: admin


  [4]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image007.png
  [5]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image009.png
  [6]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image011.png
  [7]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image013.png
  [8]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image015.png
  [9]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image017.png
  [10]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image019.png
  [11]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image021.png
  [12]: https://github.com/Hareric/dbBigHW/raw/master/recruitment/static/images/file/image023.png
