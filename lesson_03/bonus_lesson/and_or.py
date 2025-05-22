age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the event")
else:
    print("Access denied")

# ----------------------------

is_vip = False
has_invite = True

if is_vip or has_invite:
    print("Welcome to the VIP section")
else:
    print("Access denied")

# ------------------------------

age = 20
has_ticket = False
is_vip = True

if (age >= 18 and has_ticket) or is_vip:
    print("You can enter")
else:
    print("Access denied")