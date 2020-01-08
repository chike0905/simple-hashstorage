Simple Hash-based Storage
==
This is Simple Hash-based Storage implementation. You can store a file to the storage, and search by the sha256 hash value of the file.

## Motivation & Overview
To implement applications based on [IPFS](https://ipfs.io/)/DHT-based storage, you need to launch those nodes or depend on other nodes. However, when testing your application, because of some reason (e.g. flooding time to the network), sometimes you cannot store files immediately and you fail to test. I want to test my applications that based on those storages immediately.

I think those storages have a feature that when you input a file, you can get the hash value of the file. Additionally, you can also get the file by the hash value. This scheme achieves verifiability of the integrity of the file that you get from storage. You can verify the integrity by verifying the hash value as an input and the hash value of the file that you get from the storage.

## Environment
- Python 3.6.5
    - Flask 1.1.1

## Usage
- Install Flask
```
pip install Flask
```
- Lanch Hashstorage
    - Hashstorage lanched at `localhost:6666`
```
python hashstorage.py
```

- Store & Get a file via HTTP
    - You can store a base64 encoded file via HTTP.
    - You can see how to encode in python scripts in `test_hashstorage.py`.
    - When you terminate Hashstorage, Stored files are dumped in `storage.json`.

## Licence
WTFPL
