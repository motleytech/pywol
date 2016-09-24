import sys
from wakeonlan import wol

if len(sys.argv) != 2:
    print "Must provide a pc name or mac address"
    exit(1)

name = sys.argv[1]

pcMacMap = {
    'pc2': '74.D4.35.E1.27.55',
    'blitz': '74.D0.2B.C6.A2.D5'
}

mac = pcMacMap.get(name, name)
print 'Waking up "%s", with mac: %s' % (name, mac)
wol.send_magic_packet(mac)
