#playing with conditionals
temp: int = 75
weather: str = "rain"
other_hazards = ["bugs", "sun burn", "don't feel like it"]

naught = "test";
if not naught == "tes":
    print("Should see this twice")

if naught != "tes":
    print("Should see this twice \n\n")


if temp > 80:
    print("Gross. Too hot.")
elif temp < 30:
    print("Too cold")
else:
    print("Not too hot but like...Why go outside when Minecraft is inside.")


if ("rain" in weather) or ("hail" in weather):
    print("Stay inside")
else:
    print("You could go outside but like...inside is where the couch is.")


if ("bugs" in other_hazards) and ("sun burn" in other_hazards):
    print("Deffo stay inside")
elif "don't feel like it" in other_hazards:
    print("Should probably stay inside")
else:
    print("Uuuuuugggggghhhhhh...fine")