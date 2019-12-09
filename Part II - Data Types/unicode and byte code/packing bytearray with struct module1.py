import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)  #pack(fmt, .....)
print(packed)     # >: big-endian, std. size & alignment  ????
                  # i: int #4s: string with length 4  #h: short  # l: long (can also be used but takes more memory)
                  # so...4sh is a short string with length 4
file = open('data.bin', 'wb')
file.write(packed)
file.close()