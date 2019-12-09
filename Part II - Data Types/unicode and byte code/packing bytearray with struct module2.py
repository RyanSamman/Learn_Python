import struct
data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])
print(list(data))
print(struct.unpack('>i4sh',data)) #i4sh is the format of the data
