S = 5
alpha = 0.7
currentTemperature = 37
eps = 2
cBoar = 3100
mBoar = 70


def get_d_temperature(current_temperature, dt):
    return (alpha * S * (current_temperature - environmentTemperature) * dt) / (cBoar * mBoar)


environmentTemperature = int(input("Enter environment temperature "))
endTemperature = int(input("Enter boar temperature after detection "))
waitingTime = int(input("Enter waiting time "))

if environmentTemperature > endTemperature:
    print("Temperature of boar is less than environment temperature")

dt = 0.1
smT = 0

while smT < waitingTime:
    currentTemperature -= get_d_temperature(currentTemperature, dt)
    smT += dt

if abs(currentTemperature - endTemperature) < eps:
    print("Yes")
else:
    print("No")