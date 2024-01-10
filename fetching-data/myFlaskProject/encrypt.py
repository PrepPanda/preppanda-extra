import hashlib
from datetime import datetime


def encrypt_string(name):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    combined_string = f"{name}{current_time}"

    md5_hash = hashlib.md5(combined_string.encode())
    return md5_hash.hexdigest()
