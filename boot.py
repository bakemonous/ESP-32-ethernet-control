import network
"""try:
    sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
    sta_if.scan()                             # Scan for available access points
    sta_if.connect("underbast", "12345678") # Connect to an AP
    sta_if.isconnected()
except OSError:
    print('НЕ палучилась')
else:
    print ("success")"""
ssidAP         = 'WiFiName1' #Enter the router name
passwordAP     = '12345678'  #Enter the router password

local_IP       = '192.168.1.1'
gateway        = '192.168.1.1'
subnet         = '255.255.255.0'
dns            = '8.8.8.8'

ap_if = network.WLAN(network.AP_IF)

def AP_Setup(ssidAP,passwordAP):
    ap_if.ifconfig([local_IP,gateway,subnet,dns])
    print("Setting soft-AP  ... ")
    ap_if.config(essid=ssidAP,authmode=network.AUTH_WPA_WPA2_PSK, password=passwordAP)
    ap_if.active(True)
    print('Success, IP address:', ap_if.ifconfig())
    print("Setup End\n")

try:
    AP_Setup(ssidAP,passwordAP)
except:
    print("Failed, please disconnect the power and restart the operation.")
    ap_if.disconnect()