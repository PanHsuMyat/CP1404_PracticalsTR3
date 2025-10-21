"""
CP1404/CP5632 Practical 5
State names in a dictionary
File has been reformatted and state inputs can be any case.
"""

CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania",
                "SA": "South Australia"}

for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

state = input("Enter short state: ").upper()
while state != "":
    if state in CODE_TO_NAME:
        print(f"{state:3} is {CODE_TO_NAME[state]}")
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()