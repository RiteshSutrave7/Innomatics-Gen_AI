# 6) Online Event Registration Capacity Controller

def event_registration(capacity, registrations):
    if registrations > capacity:
        confirmed = capacity
        waitlisted = registrations - capacity
        status = "Closed"
    else:
        confirmed = registrations
        waitlisted = 0
        status = "Open"
    print("Confirmed Registrations:", confirmed)
    print("Waitlisted Users:", waitlisted)
    print("Registration Status:", status)
event_registration(100, 105)
     