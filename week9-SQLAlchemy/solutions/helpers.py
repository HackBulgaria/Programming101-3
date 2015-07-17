import hashlib


def hash_password(password):
    sha256 = hashlib.sha256()

    sha256.update(password.encode("utf-8"))

    return sha256.hexdigest()
