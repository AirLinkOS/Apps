import sys,time
from icmplib import ping

IPADDR = "192.168.1.1"
STIME = 5

def logMessage(message="", trace=False):
   print("%s: %s" % (time.asctime(), message))
   
def sendPing(ipAddr) :
   status = False
   try :
       host = ping(ipAddr, count=1)
       if host.packets_received > 0:
           status = True
   except Exception as e:
       logMessage("Exception: " +  str(e))
   return status

def main(argv):
   global STIME
   LOOPCOUNT = 0
   while True:
       LOOPCOUNT += 1
       status = sendPing(IPADDR)
       if status == True :
          logMessage("ping " + str(LOOPCOUNT) + " " + IPADDR)          
       else: 
          logMessage("ping failure " + str(LOOPCOUNT) + " " + IPADDR)
       time.sleep(STIME)

if __name__ == '__main__':
   main(sys.argv[1:])
