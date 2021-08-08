import hashlib

class Encrypt():
    """encrypting data which is not easy to be decrypt and is one-way hashing"""

    def __init__(self, arg):
        self.arg = bytes(arg,'utf-8')

    def hash(self):
        result = hashlib.md5(self.arg)
        return (result.digest())
