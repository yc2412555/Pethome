import os

import celery
import pymysql

from PetHome import settings

pymysql.install_as_MySQLdb()

# 注册环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PetHome.settings')

# 创建Celery实例 - broker指定消息队列服务的位置
app = celery.Celery(
    'pethome',
    broker='redis://:1qaz2wsx@47.103.17.215:6379/15'
)

# 从项目的配置文件读取Celery配置信息
app.config_from_object('django.conf:settings')
# 从指定的文件(例如celery_config.py)中读取Celery配置信息
# app.config_from_object('celery_config')

# 让Celery自动从参数指定的应用中发现异步任务/定时任务
# app.autodiscover_tasks(['api', ])
# 让Celery自动从所有注册的应用中发现异步任务/定时任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)