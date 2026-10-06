from machine import Pin, ADC, PWM
import time
import network
import urequests

WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

SERVER_URL = "http://host.wokwi.internal:5000/api/data"

pH = ADC(Pin(34))
DO = ADC(Pin(35))
H2S = ADC(Pin(32))
NH3 = ADC(Pin(33))

red = Pin(2, Pin.OUT)
blue = Pin(16, Pin.OUT)
green = Pin(15, Pin.OUT)


class Alert_system:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def update(self, status):
        if status == "Normal":
            self.green.off()
            self.red.on()
            self.blue.on()

        elif status == "Warning":
            self.green.off()
            self.red.off()
            self.blue.on()

        elif status == "Danger":
            self.green.on()
            self.blue.on()
            self.red.off()
            time.sleep(0.5)
            self.green.on()
            self.blue.on()
            self.red.on()
            time.sleep(0.5)


class Rangefinder:
    def __init__(self, name, normal_low, normal_high, danger_low=None, danger_high=None):
        self.name = name
        self.normal_low = normal_low
        self.normal_high = normal_high
        self.danger_low = danger_low
        self.danger_high = danger_high

    def compare(self, value):
        if self.danger_low is not None and value < self.danger_low:
            return "Danger"

        elif self.danger_high is not None and value > self.danger_high:
            return "Danger"

        elif self.normal_low <= value <= self.normal_high:
            return "Normal"

        else:
            return "Warning"


alert_system = Alert_system(red, green, blue)

ph1 = Rangefinder("pH", 6.5, 7.75, 5.5, 9.0)
do2 = Rangefinder("DO", 5, 20, 2, None)
h2s3 = Rangefinder("H2S", 0, 1, None, 5)
nh34 = Rangefinder("NH3", 0, 1, None, 5)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        while not wlan.isconnected():
            time.sleep(0.5)

    print("Wi-Fi connected!")
    print("ESP32 IP:", wlan.ifconfig()[0])

connect_wifi()

while True:
    pH_Val = 6.5 + (pH.read() / 4095) * 3.5
    DO_Val = (DO.read() / 4095) * 12
    H2S_Val = (H2S.read() / 4095) * 20
    NH3_Val = (NH3.read() / 4095) * 20

    ph = ph1.compare(pH_Val)
    do = do2.compare(DO_Val)
    h2s = h2s3.compare(H2S_Val)
    nh3 = nh34.compare(NH3_Val)

    danger_count = 0

    if ph == "Danger":
        danger_count += 1

    if do == "Danger":
        danger_count += 1

    if h2s == "Danger":
        danger_count += 1

    if nh3 == "Danger":
        danger_count += 1

    if danger_count == 4:
        overall_status = "Danger"
    elif danger_count >= 2:
        overall_status = "Warning"
    else:
        overall_status = "Normal"

    print("pH:", pH_Val, ph)
    print("DO:", DO_Val, do)
    print("H2S:", H2S_Val, h2s)
    print("NH3:", NH3_Val, nh3)
    print("Danger count:", danger_count)
    print("Overall Status:", overall_status)
    
    alert_system.update(overall_status)


    data = {
    "ph": pH_Val,
    "do": DO_Val,
    "h2s": H2S_Val,
    "nh3": NH3_Val,
    "ph_status": ph,
    "do_status": do,
    "h2s_status": h2s,
    "nh3_status": nh3,
    "overall_status": overall_status
    }

    try:
        response = urequests.post(
            SERVER_URL,
            json=data
        )

        print("Data sent to server")
        response.close()

    except Exception as e:
        print("Failed to send data:", e)
    
    time.sleep(1)