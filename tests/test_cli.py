import pytest
import shutil
import threading
import time
import requests

from  hashstorage.cli import *

from tests.utils import * 

@pytest.fixture(scope='session')
def setupHashStorageThread():
    hashstorage_thread = threading.Thread(target=runHashStorageCli, args=(["-dir", TESTSTORAGEDIR],))
    hashstorage_thread.setDaemon(True)
    hashstorage_thread.start()

    time.sleep(1)
    
    yield hashstorage_thread

    time.sleep(1)
    if os.path.exists(TESTSTORAGEDIR):
       shutil.rmtree(TESTSTORAGEDIR)


def storeDummy():
    url = 'http://localhost:6666/store'
    data = {'value': "dummy"}
    response = requests.post(url, json=data)
    return response.json()

def test_startHashStorage(setupHashStorageThread):
    assert os.path.exists(TESTSTORAGEDIR) 
    
    response = requests.get("http://localhost:6666")
    assert response.text == "Simple Hash Storage v0.0.1 (C) Ryosuke Abe 2020" 

def test_storeToHashStorage(setupHashStorageThread):
    res = storeDummy()
    assert res["result"] == True
    assert res["key"] == sha256("dummy")

    data = loadJson(TESTSTORAGEDIR+"/storage.json") 
    assert data[res["key"]] == "dummy"
   
def test_geFromHashStorage(setupHashStorageThread):
    res = storeDummy()
    
    key = res["key"]
    url = 'http://localhost:6666/get'
    data = {"key": key}
    response = requests.post(url, json=data)
    res = response.json()
    
    assert res["result"] == True
    assert res["value"] == "dummy"


