import socket as sk
import uuid as ud

hostname = sk.gethostname()
IPAddr = sk.gethostbyname(hostname)
hexIP = sk.inet_aton(IPAddr).hex()
macAddr = ':'.join(['{:02x}'.format((ud.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

print("\n ********** INFORMATION LOADED **********")
print("\nYour computer name is: " + hostname)
print("Your computer IP Address is: " + IPAddr)
print("Your Hex Ip Address: " + hexIP)
print("Your computer Mac Address is: " + macAddr)
print("\n ********** PROGRAM FINISHED **********")