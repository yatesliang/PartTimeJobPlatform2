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

BLOCKCHAIN_USERINFO_CHAINCODE_ID = "f942ddb30891258d548b6ca7ebf184d305c563c7b91adbbe5f27a7b19b9685dc0e7ae1cdc05c44810d66391f89ebd40a5a955757a71e015d8494a34b679afabc"
BLOCKCHAIN_JOBINFO_CHAINCODE_ID = "6053c8cfd1429d03c6bcec3e66d00bc3eb465f8a54c27944062e50ff446eba6f3f07f6081c45d4a570053ce0590686bb1bdfc32e8f77adc667ed427380ab3926"
BLOCKCHAIN_TX_CHAINCODE_ID = "8e7d7632ebcc9cbb2ea58870047c4035337e5eb7ad96164a736046d2260f9a1f3a724c9994841a0ff8382eced5e423c2399856e0b7325a2905d1c62d77178875"


def main():
    pass


if __name__ == '__main__':
    main()
