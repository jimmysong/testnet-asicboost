import json

from binascii import hexlify


def hex_field(binary):
    return hexlify(binary[::-1])


def int_field(binary):
    return int("0x{}".format(hex_field(binary)), 16)


with open('testnet_headers') as f:
    header = f.read(80)
    version_distribution = {}
    height = 1
    while header != "":
        version = int_field(header[0:4])
        if not version_distribution.get(version):
            version_distribution[version] = {'count': 0, 'first_instance': height}
        version_distribution[version]['count'] += 1
        header = f.read(80)
        height += 1

for version in sorted(version_distribution.keys()):
    data = version_distribution[version]
    if data['count'] < 5:
        print("{}:{}".format(version, data))

