# Django_Cloud_Album
Django学习项目——云相册学习

`本项目仅用于学习练习django的使用`

## 一. 代码使用说明
确认你的电脑已经正确安装 Python3.6.8-Python3.10。
### 1. 下载项目后,创建虚拟环境：
``` shell
python -m venv env
```
### 2. 运行虚拟环境:
``` shell
source env/bin/activate
```
### 3. 安装所有依赖项：
``` shell
pip3 install -r requirements.txt
```
### 4. 进行数据迁移与账号创建：
``` shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuse
```
### 5. 启动测试服务器：
``` shell
python3 manage.py runserver 0.0.0.0:9000
```
## 二. 项目学习地址
``` html
https://github.com/stacklens/django-album-tutorial
```
注意：请遵循源项目地址的许可协议