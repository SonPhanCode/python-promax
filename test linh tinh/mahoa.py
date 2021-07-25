from Crypto.Cipher import DES
key = 'abcdefgh'
def pad(text):
 while len(text) % 8 != 0:
 	text += ' '
 	return text
des = DES.new(key, DES.MODE_ECB)
text = 'Python rocks!'
padded_text = pad(text)
encrypted_text = des.encrypt(text)
encrypted_text = des.encrypt(padded_text)
encrypted_text
b'>\xfc\x1f\x16x\x87\xb2\x93\x0e\xfcH\x02\xd59VQ'