#!/usr/bin/python
# -*- coding: utf-8 -*-

# mysql

DEBUG = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

GONGXIANGDANCHE_TOKEN = ''

TRY_REQ = True

REDIS_URL = "redis://:@localhost:6379/0"
REDIS_QUEUE_KEY = "my_queue"

MONGOALCHEMY_DATABASE = 'library'
MONGOALCHEMY_SERVER_AUTH = False

RUN_IN_PYTHON_SERVER = False  # False for nginx server and True for command `python manage.py runserver -h 0.0.0.0`

BLOCKCHAIN_USERINFO_URL = "http://10.60.42.201:7050/chaincode"
BLOCKCHAIN_TX_URL = "http://10.60.42.201:7050/chaincode"
BLOCKCHAIN_JOBINFO_URL = "http://10.60.42.201:7050/chaincode"

BLOCKCHAIN_USERINFO_CHAINCODE_ID = "4d1f0248bdc9b4cf13214d023bafd2862aea2c8fd52de6d0092876a962b4dccafa6b23ffdceaa394c243a15402f3b7157785fe9ba69048f7b224baf93a100bfb"
BLOCKCHAIN_JOBINFO_CHAINCODE_ID = "e32311a3130907157213865f7b19c9f2a8e0209b2092321f0cfabd3b3e267336a5b1ac62c6d6df926bde908d9b68cc41c9be8ecbe08b4986c5dd89761cb02d49"
BLOCKCHAIN_TX_CHAINCODE_ID = "5a2dbac78322093b856eafc20faa9cfc6a3770acf41936f784042515d203c0ed6b5c83ba1f39c7d254cf1fab7d74902ab2158ee24718e6c0283b962d87ecf05c"


def main():
    pass


if __name__ == '__main__':
    main()
