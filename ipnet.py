import ipaddress

#Create an IP network object
ipobj = ipaddress.IPv4Network('10.10.10.0/24') #Create an IP network object in CIDR notation
ipobj2 = ipaddress.IPv4Network('10.10.10.0/255.255.255.0') #Create an IP network object using subnet mask
print(ipobj)
print(type(ipobj2))

#Show the network with subnet mask
print(ipobj.with_netmask)

#Show the network with prefix length
print(ipobj.with_prefixlen)

#Show the network with host mask
print(ipobj.with_hostmask)

#Show only subnet mask
print(ipobj.netmask)

#Show only host mask
print(ipobj.hostmask)

#Show only prefix length
print(ipobj.prefixlen)

#Show only network address
print(ipobj.network_address)

#Show total number of addresses in the network
print(ipobj.num_addresses)

#Show all the hosts within the subnet
print(ipobj.hosts())
print([ip for ip in ipobj.hosts()])
print([str(ip) for ip in ipobj.hosts()])

#Check if an IP address falls within a subnet
print(ipaddress.ip_address('192.168.1.1') in ipaddress.IPv4Network('10.10.10.0/24'))
print(ipaddress.ip_address('192.168.1.1') in ipaddress.IPv4Network('192.168.1.0/24'))

#Check if two networks overlaps

n1 = ipaddress.ip_network('192.0.2.0/24')
n2 = ipaddress.ip_network('192.0.3.0/28')
print(n1.overlaps(n2))

# Check the supernet
print(ipaddress.ip_network('192.168.77.0/26').supernet(new_prefix=23))
print(ipaddress.ip_network('192.168.77.0/26').supernet(prefixlen_diff=2))

#Subnet of

n1 = ipaddress.ip_network('192.0.2.0/24')
n2 = ipaddress.ip_network('192.0.2.0/28')
print(n1.subnet_of(n2))


#Supernet of
n1 = ipaddress.ip_network('192.0.2.0/24')
n2 = ipaddress.ip_network('192.0.2.0/28')
print(n1.supernet_of(n2))


#List all the subnets of a CIDR
n1 = ipaddress.ip_network('10.10.10.0/24')
print(n1.subnets())
print([ n for n in n1.subnets()])
print([ str(n) for n in n1.subnets()])
print([ str(n) for n in n1.subnets(prefixlen_diff=2)])
print([ str(n) for n in n1.subnets(new_prefix=30)])

#When a IP network has to be contructed with host bit set.
#E.g., 192.168.1.1/24 is specified whereas 192.168.1.0/24 is expected.

print(ipaddress.ip_network('192.168.0.1/28'))

#Pass an additional argument "strict=False"
print(ipaddress.ip_network('192.168.0.1/28',strict=False))


