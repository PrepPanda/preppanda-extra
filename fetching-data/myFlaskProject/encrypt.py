import hashlib


def encrypt_string(hash_string):
    md5_hash = hashlib.md5(hash_string.encode())
    return md5_hash.hexdigest()
