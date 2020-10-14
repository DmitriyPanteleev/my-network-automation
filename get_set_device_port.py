#!/usr/bin/python3

from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902
 
def GetPortStatus(ip,comm,oid):
 rez=None      
 try:
    errorIndication, errorStatus, errorIndex, varBinds = next(
       getCmd(SnmpEngine(),
          CommunityData(comm),
          UdpTransportTarget((ip, 161), timeout=2.0, retries=0),
          ContextData(),
          ObjectType(ObjectIdentity(oid)))
    )
 
    if errorIndication:
       print(errorIndication)
       return rez
    elif errorStatus:
       print('%s at %s' % (errorStatus.prettyPrint(),
               errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
       return rez           
    else:
       for varBind in varBinds:      
     if str(varBind).find("up")>0: rez=1;
     if str(varBind).find("down")>0: rez=2;
     if rez==None:
       zx=str(varBind).split("=");
       rez=zx[1].replace(" ","");      
 except:           
     rez=None  
 return rez
 
def SetPortStatus(ip,comm,oid,status):
 rez=None            
 try:
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.setCmd(
       cmdgen.CommunityData(comm,mpModel=1),
       cmdgen.UdpTransportTarget((ip, 161)),
    (oid, rfc1902.Integer(status)),    
    )
    # Check for errors and print out results
    if errorIndication:
       print(errorIndication)
    else:
       if errorStatus:
       print('%s at %s' % (
           errorStatus.prettyPrint(),
           errorIndex and varBinds[int(errorIndex)-1] or '?'
           )
       )
       rez=None
       else:
       for name, val in varBinds:
           print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))    
           rez=True
 except:           
     rez=None
 return rez

if __name__ == '__main__':
# Example how to use

# Get port status
# oid=1.3.6.1.2.1.2.2.1.8.x
# x - port number
# D-Link
rz=GetPortStatus('12.1.14.6','XFiles','1.3.6.1.2.1.2.2.1.8.9')  
print "Dlink: ",rz
 
# Set port status
# up=1,down=2
# oid=1.3.6.1.2.1.2.2.1.7.9.x
# x - port number
# D-Link
rz=SetPortStatus('72.8.114.4','X-Files','1.3.6.1.2.1.2.2.1.7.9',1)
print rz;
