import hashlib

md5 = hashlib.md5()
md5.update('Miss 敏敏！Meeting you was a blessing in my life'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('Miss 敏敏！'.encode('utf-8'))
sha1.update('Meeting you was a blessing in my life'.encode('utf-8'))
print(sha1.hexdigest())

sha2 = hashlib.sha1()
sha2.update('Miss 敏敏！Meeting you was a blessing in my life'.encode('utf-8'))
print(sha2.hexdigest())