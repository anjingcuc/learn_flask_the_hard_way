# -*- coding: UTF-8 -*-
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
