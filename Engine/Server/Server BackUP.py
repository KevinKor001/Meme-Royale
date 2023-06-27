import sys
import subprocess
import time
import os
os.system('py -m pip install cloudlink websockets')


from cloudlink import cloudlink
cl = cloudlink()
cls = cl.server(logs=True)
print("Enter Custom IO (Type # for default --Localhost)")
cIp = input("Enter Custom IP : ")
cPort = input("Enter Custom Port : ")
defValue = "#"
forLoop = 10
cls.set_motd("CL4 Optimized! Gotta Go Fast!", True)
print("Setting values")

if cIp == defValue :
    cIp = "127.0.0.1"

if cPort == defValue :
    cPort = "3000"

cHost = cIp + ":" + cPort
cls.reject_clients = True
print("Server Is Initializing")
print("Ip Set to : " + cIp)
time.sleep(0.1)
print("Port Set To: " + cPort)
time.sleep(0)
print("CUSTOM IP IS BROKEN PLEASE DONT USE IT!!!")

time.sleep(0)
print("Server Started On @LocalHost : Room - ws://127.0.0.1:3000/")
time.sleep(0)
print("Server Ready : Players May Now Connect")

Logs = input("Want to display the servers logs in the console Y/N: ")

cls.reject_clients = False
cls.run()



#cls.run( ip : port ) -- Custom address setup


#"127.0.0.1"
#"3000"
