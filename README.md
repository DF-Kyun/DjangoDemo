# DjangoDemo
一个Django Demo工程

基于python3.8，Django3.0开发，搭建一个博客

#### 安装python依赖
```
pip install -r requirement.txt
```

#### 创建数据模型
更改DjangoDemo目录下的DATABASES，数据库设置好之后，我们就依次输入下面的命令进行数据库迁移：

```
python manage.py makemigrations
python manage.py migrate
```

#### 创建管理账号
输入下面命令创建管理帐号和密码：
```
python manage.py createsuperuser
```

#### 启动项目

```
python manage.py runserver 
```

提示启动成功，然后我们在浏览器里输入：http://127.0.0.1:8000/，可进入页面，http://127.0.0.1:8000/admin，可进入后台管理

