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
import os
import shutil

from hashstorage.hashstorage import *
from hashstorage.utils import *

from tests.utils import *

@pytest.fixture(scope='function')
def setupHashStorage():
    hs = HashStorage(TESTSTORAGEDIR)
    
    yield hs

    shutil.rmtree(TESTSTORAGEDIR)

def test_createHashStorage(setupHashStorage):
    hs = setupHashStorage

    assert hs.datadir == TESTSTORAGEDIR
    assert os.path.exists(TESTSTORAGEDIR) 

def test_store(setupHashStorage):
    hs = setupHashStorage
    dummydata = "dummy"

    key = hs.store(dummydata)
    
    assert key == sha256(dummydata)
    assert hs.storage[key] == dummydata

def test_get(setupHashStorage):
    hs = setupHashStorage
    dummydata = "dummy"
    key = hs.store(dummydata)
   
    assert hs.get(key) == "dummy"

def test_get_unstored_value(setupHashStorage):
    hs = setupHashStorage
    key = sha256("dummy")
   
    assert hs.get(key) == None

def test_shutdown(setupHashStorage):
    hs = setupHashStorage
    dummydata = "dummy"
    key = hs.store(dummydata)

    hs.shutdown()
    assert os.path.exists(TESTSTORAGEDIR+"/storage.json") 
    
    data = loadJson(TESTSTORAGEDIR+"/storage.json") 
    assert data[key] == "dummy"
