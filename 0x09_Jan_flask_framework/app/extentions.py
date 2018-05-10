# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(use_native_unicode="UTF-8")  # 实例化SQLAlchemy,传入app对象
