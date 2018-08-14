#!/usr/bin/python

import subprocess
import sys
import os

if len(sys.argv) != 2:
    print "Usage: alive_targets <ip address/range>"
    print "Range for last octect like 192.168.1.1-255"
    sys.exit(0)

target_hosts = sys.argv[1]

def alive_hosts(target_hosts):
    print "INFO: Performing ping sweep over %s" % (target_hosts)
    output_file = "/root/scripts/recon_enum/results/exam/targets.txt"
    f = open(output_file, 'w')
    if not os.path.isdir('/root/scripts/recon_enum/results/exam/nmap'):
        os.makedirs('/root/scripts/recon_enum/results/exam/nmap')
    lines = subprocess.check_output(['nmap','-n','-sn',target_hosts,'-oA','/root/scripts/recon_enum/results/exam/nmap/%s_HOST_DISCOVERY' % target_hosts]).split("\n")
    live_hosts = 0
    for line in lines:
        line = line.strip()
        line = line.rstrip()
        if ("Nmap scan report for" in line):
            ip_address = line.split(" ")[4]
            if (live_hosts > 0):
                f.write('\n')
            f.write("%s" % (ip_address))
            live_hosts += 1
    print "INFO: Host scanning complete. Targets acquired."
    f.close()

if __name__=='__main__':
    alive_hosts(target_hosts)
