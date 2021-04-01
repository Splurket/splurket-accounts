import base64
from Crypto.Cipher import AES
from Crypto import Random

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw, iv ):
        raw = pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( cipher.encrypt( raw ) )

    def decrypt( self, enc, iv ):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc ))

a = AESCipher('fce4aa4dcf0d2b27fe4ffdafa602c81d1930c410f48ada5c763d4c4052a939eb'.decode('hex_codec'))
print a.encrypt("This bloody encryption engine won't work !", 'c75271d593ca86ca785e3bb25e8d02cb'.decode('hex_codec'))

b = AESCipher('fce4aa4dcf0d2b27fe4ffdafa602c81d1930c410f48ada5c763d4c4052a939eb'.decode('hex_codec'))
print b.decrypt('44FsQIcqM412+YXZBwwoQSCz2uB9QPQMXJ410Xpw1f/M5RTRS7N6yfziAGq/Fd/E', 'c75271d593ca86ca785e3bb25e8d02cb'.decode('hex_codec'))