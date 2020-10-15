Simple Hash-based Storage
==
This is Simple Hash-based Storage implementation. You can store a file to the storage, and search by the sha256 hash value of the file.

## Motivation & Overview
To implement applications based on [IPFS](https://ipfs.io/)/DHT-based storage, you need to launch those nodes or depend on other nodes. However, when testing your application, because of some reason (e.g. flooding time to the network), sometimes you cannot store files immediately and you fail to test. I want to test my applications that based on those storages immediately.

I think those storages have a feature that when you input a file, you can get the hash value of the file. Additionally, you can also get the file by the hash value. This scheme achieves verifiability of the integrity of the file that you get from storage. You can verify the integrity by verifying the hash value as an input and the hash value of the file that you get from the storage.

## Enviroment
- Dependency is managed by poetry. see `pyproject.toml`.
### Develop
- Poetory 1.1.1
    - Python 3.7.3
### Test Enviroment
- pytest 6.0.1

## Installation
### From Source Code / Install via pip
- Clone this repository
```
https://github.com/chike0905/simple-hashstorage.git
```
- Build
    - Dumped install file in `dist`
    ```
    poetry build
    ```
    - Install via pip
    ```
    pip install dist/hashstorage-0.1.0.tar.gz 
    ```

## Usage
- Launch HashStorage.
    - You can specify storage dump dirctory. default: `$(pwd)/.hashstorage`
```
hashstorage-cli -d DATADIR
```
- Store & Get a file via HTTP
  - see `tests/test_cli.py`

## Licence
WTFPL
