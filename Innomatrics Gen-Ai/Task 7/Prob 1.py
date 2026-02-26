# 1) Smart Light Controller
# create class Smart_light
class Smart_Light:
    def __init__(self, light_name):
        self.light_name = light_name
        self.status = "OFF" # it is a default status.
    def turn_on(self):
        self.status = "ON"
    def turn_off(self):
        self.status = "OFF"
    def show_status(self):
        print(self.light_name + " is " + self.status)

Light_name = input("Enter Light Name: ")
action = input("Enter Action (ON/OFF): ")

light = Smart_Light(Light_name)

if action == "ON":
    light.turn_on()
elif action == "OFF":
    light.turn_off()

light.show_status()