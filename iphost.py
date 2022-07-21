import ipaddress

#Create an IP interface object
iho1 = ipaddress.IPv4Interface('10.10.10.1/24') 
iho2 = ipaddress.IPv4Interface('192.168.1.1/255.255.255.0') 

#Print IP without Subnet information
print(iho1.ip)

#Print the network/subnet the IP belongs to
print(iho2.network)

#Print the IP with prefixlen(CIDR)
print(iho2.with_prefixlen)

#Print the IP with netmask
print(iho1.with_netmask)

#Print the IP with hostmask
print(iho1.with_hostmask)

#Show only subnet mask
print(iho1.netmask)

#Show only host mask
print(iho1.hostmask)
