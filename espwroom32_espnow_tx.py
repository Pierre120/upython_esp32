# ESPWROOM32 ESP-Now [TX]Transmitter/Sender
import network, espnow
from utime import sleep_ms
from uos import urandom

print("<=+ [TX] Transmitter/Sender Node +=>")

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF) # Or network.AP_IF
sta.active(False)
print("Activating WLAN...")
sta.active(True) # Problem/Errors arises on this line
print("WLAN Activated")

# Initialize ESP-Now protocol
enow = espnow.ESPNow()
print("Activating ESP-Now...")
enow.active(True)
print("ESP-Now Activated")

# NOTE: peer MAC address value can be changed
peer = b'\xb0\xa72*>d' # MAC address of ESP32WROOM32 chip (receiver)
print("Adding peer [ESP32WROOM32]...")
enow.add_peer(peer) # Must add_peer() before send()
print("Peer added")

print("Sending...")
for i in range(15): # characterize network for 30s
    # 3 set of dummy 6-byte accelerometer data
    msg1 = urandom(6)
    msg2 = urandom(6)
    msg3 = urandom(6)
    print(i*2)
    sleep_ms(950) # approx 1s interval before message burst
    print("Message success:", enow.send(peer, msg1, True))
    sleep_ms(500)
    print("Message success:", enow.send(peer, msg2, True))
    sleep_ms(500)
    print("Message success:", enow.send(peer, msg3, True))
print("End")

# Close WLAN interface and protocol
enow.active(False)
sta.active(False)
