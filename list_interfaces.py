#!/usr/bin/env python

# Found at <https://gist.github.com/pklaus/289646#file-enumerate_interfaces-py-L27>
# all_interfaces renamed to list_interfaces

import socket
import fcntl
import struct
import array

def list_interfaces():
	max_possible = 128  # arbitrary. raise if needed.
	bytes = max_possible * 32
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	names = array.array('B', '\0' * bytes)
	outbytes = struct.unpack('iL', fcntl.ioctl(
		s.fileno(),
		0x8912,  # SIOCGIFCONF
		struct.pack('iL', bytes, names.buffer_info()[0])
	))[0]
	namestr = names.tostring()
	lst = []
	for i in range(0, outbytes, 40):
		name = namestr[i:i+16].split('\0', 1)[0]
		ip   = namestr[i+20:i+24]
		lst.append((name, ip))
	return lst

def format_ip(addr):
	return str(ord(addr[0])) + '.' + \
		   str(ord(addr[1])) + '.' + \
		   str(ord(addr[2])) + '.' + \
		   str(ord(addr[3]))

if __name__ == "__main__":
	ifs = list_interfaces()
	for i in ifs:
		print "%12s   %s" % (i[0], format_ip(i[1]))
	
