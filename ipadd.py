#https://docs.python.org/3/library/ipaddress.html
import ipaddress

ioa=ipaddress.ip_address('10.10.10.1') # Class A private address
iob=ipaddress.ip_address('172.16.33.33') # Class B private address
iop=ipaddress.ip_address('55.55.55.55') # Public address
iom=ipaddress.ip_address('224.0.0.1') # Multicast address

print(type(ioa))
print(ioa)

# is it private?
print(ioa.is_private)
print(iop.is_private)

# is it public?
print(iop.is_global)

# is it multicast?
print(iop.is_multicast) # not multicast
print(iom.is_multicast) # is multicast

# Operators

#Greater than
print(ipaddress.ip_address('172.16.33.33') > ipaddress.ip_address('10.10.10.1'))

#Greater than or equal to
print(ipaddress.ip_address('10.10.10.1') >= ipaddress.ip_address('10.10.10.1'))

#Less than
print(ipaddress.ip_address('10.10.10.1') < ipaddress.ip_address('224.0.0.1')) # Yes
print(ipaddress.ip_address('224.0.0.1') < ipaddress.ip_address('172.16.33.33')) # No

#Less than or equal to
print(ipaddress.ip_address('10.10.10.1') <= ipaddress.ip_address('224.0.0.1'))


#Equal to
print(ipaddress.ip_address('10.10.10.1') == ipaddress.ip_address('10.10.10.1'))
print(ipaddress.ip_address('10.10.10.1') == ipaddress.ip_address('224.0.0.1'))
print(ipaddress.ip_address('192.168.1.1') == ipaddress.ip_address('192.168.1.1'))

#Not Equal to
print(ipaddress.ip_address('192.168.1.1') != ipaddress.ip_address('192.168.1.2'))
