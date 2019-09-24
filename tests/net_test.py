from easilyb.net.ip import IP, Pool


# Constructors
ip1 = IP('192.168.0.1')       # ipv4 String
ip2 = IP('2001:db8::')        # ipv6 String
ip3 = IP(3232235521)          # decimal
pool1 = Pool.from_netrange('192.168.0.0/28')  # Pool CIDR range
pool2 = Pool.from_netrange('192.168.0.1-192.168.0.255')  # Pool address range
pool3 = Pool(ip1, '192.168.0.255')  # lower and upper addresses


# Properties:
print(ip1.version)     # IP version 4 or 6
print(ip1.compressed)  # Compressed representation of the IP address
print(ip2.exploded)    # Exploded representation of the IP address
print(ip3.decimal)     # Decimal value of the IP address
print(int(ip3))        # Decimal value of the IP address
print(pool1.version)   # Pool IP version
print(pool1.count)     # Pool IP address count
print(pool1.lower)     # Pool lower ip address
print(pool1.upper)     # Pool upper ip address


# Operations
print(ip1 <= ip3)      # Comparison
print(ip1 < ip3)       # Comparison
print(ip1 > ip3)       # Comparison
print(ip1 >= ip3)      # Comparison
print(ip1 == ip3)      # Comparison
print(ip1 in pool1)    # check if address in a pool
print(ip1 + 1)         # incrementing address
print(ip2 - 1)         # decrementing address
