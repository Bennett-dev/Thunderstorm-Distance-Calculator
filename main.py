import time
def calc(T, F=60):
    K = (5/9*(F-32))+273.16
    VsoundK = 643.855*(K/273.15)**0.5
    VsoundM = 1.1507794*VsoundK
    return VsoundM * (T/3600)
x = int(input("count the seconds between the flash and the sound: "))
y = int(input("enter air temp: "))
z = str(round(calc(x, y), 4))
print("the storm is "+z+" miles away")
time.sleep(10)