#!/usr/bin/env python3

import json

filename = 'json_sample.json'

with open(filename) as j:
    j = json.load(j)

ip4 = []
ip6 = []

for a, b in j.items():
    for c, d in b.items():
        for e, f in d.items():
            g = f['prefix_length']
            if c == 'ipv4':
                ip4.append('{}/{}'.format(e, g))
            elif c == 'ipv6':
                ip6.append('{}/{}'.format(e, g))

for m in ip4:
    print('IPv4 address in this data: ' + m)
for n in ip6:
    print(n)

#print('\nIPv4 addresses: {}\n'.format(ip4))
#print('\nIPv6 addresses: {}\n'.format(ip6))



