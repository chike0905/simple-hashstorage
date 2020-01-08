#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
#
# Copyright (C) 2020 Ryosuke Abe <chike@sfc.wide.ad.jp>
# 
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.

import pytest

import requests
import base64

import hashlib
import binascii

def sha256(keyword): 
    bytekey = binascii.hexlify(keyword.encode("utf-8"))
    hashvalue = hashlib.sha256(bytekey).digest()
    return hashvalue.hex()

def test_storetostorage():
    url = 'http://localhost:6666/store'
    data = {
            'file': base64.b64encode("hoge".encode()).decode()
            }

    response = requests.post(url, json=data)

    res = response.json()
    print(res)

def test_getfromstorage():
    # store test data
    url = 'http://localhost:6666/store'
    data = {
            'file': base64.b64encode("hoge".encode()).decode()
            }

    response = requests.post(url, json=data)

    res = response.json()
    filekey = res["result"]

    url = 'http://localhost:6666/get'
    data = {"key": filekey}
    response = requests.post(url, json=data)
    res = response.json()
    print(base64.b64decode(res["file"]).decode("utf-8"))
    assert filekey ==  sha256(base64.b64decode(res["file"]).decode("utf-8"))

def test_getundefinedkey():
    url = 'http://localhost:6666/get'
    data = {"key": "undefined"}
    response = requests.post(url, json=data)
    res = response.json()
    print(base64.b64decode(res["file"]).decode("utf-8"))
