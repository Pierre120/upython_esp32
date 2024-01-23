# ESP32WROOM32 ESP-Now [RX]Receiver
import network, espnow
from utime import sleep_ms

print("+=> [RX]Receiver Node <=+")

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF) # Or network.AP_IF
print("Activating WLAN...")
sta.active(True)
print("WLAN Activated")

# Initialize ESP-Now protocol
enow = espnow.ESPNow()
print("Activating ESP-Now...")
enow.active(True)
print("ESP-Now Activated")

# Buffer for messages
# Buffer = [ESP-Now headers, 250-byte payload, RSSI, timestamp]
buf = [bytearray(6), bytearray(250), 0, 0]

# Callback function to handle received message
def recv_cb(e):
    enow.recvinto(buf, 0) # return immediately if no data available
    print(buf)

# interrupt when a message is received
enow.irq(recv_cb)

# wait for messages for 60s
print("Listening...")
for i in range(60):
    print(i)
    sleep_ms(1000)
print("End")

# Close WLAN interface and protocol
enow.active(False)
sta.active(False)
