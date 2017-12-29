# -*- coding: utf-8 -*-
#PS：在计算机内存中，统一使用Unicode编码。
#当需要保存到硬盘中或者需要传输的时候，转换成UTF-8编码
print( ord('敏'))

print( chr(25935))

#encode
print( "Miss".encode("ascii"))
print( "Miss敏敏".encode())
print( "Miss敏敏".encode("utf-8"))

#decode
print( b'Miss'.decode("ascii"))
print( b'Miss\xe6\x95\x8f\xe6\x95\x8f'.decode())
print( b'Miss\xe6\x95\x8f\xe6\x95\x8f'.decode("utf-8"))

#len()，对于str计算的是字符数；对于bytes计算的是字节数
print( len("Miss敏敏"))
print( len("Miss\xe6\x95\x8f\xe6\x95\x8f"))