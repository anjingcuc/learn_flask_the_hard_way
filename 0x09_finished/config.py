# -*- coding: UTF-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'LearnFlaskTheHardWay.by.JanCUC'
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    BCRYPT_LOG_ROUNDS = 12


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'data-dev.sqlite')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}