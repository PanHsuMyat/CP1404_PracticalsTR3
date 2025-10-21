"""
CP1404 Practical 5
Hexadecimal colour lookup program
"""

COLOUR_CODES = {"aliceblue": "#f0f8ff",
                "byzantium": "#702963",
                "cadetgrey": 	"#91a3b0",
                "cadmiumgreen": "#006b3c",
                "cadmiumorange": "#ed872d",
                "candyapplered": "#ff0800",
                "electricblue": "#7df9ff",
                "mindaro": "#e3f988"}


colour_name = input("Enter a colour name: ").lower()

while colour_name != "":
    hex_code = COLOUR_CODES.get(colour_name)
    if hex_code:
        print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    print("Invalid colour, please try again.")
    colour_name = input("Enter a colour name: ").lower()

print("Goodbye!")