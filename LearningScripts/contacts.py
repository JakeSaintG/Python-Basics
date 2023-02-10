contacts = {
    "number":"4",
    "students": [
        {"name":"Sarah H.", "email":"s@test.com"},
        {"name":"Fox M.", "email":"f@test.com"},
        {"name":"Samus A.", "email":"m@test.com"},
        {"name":"Donkey K.", "email":"d@test.com"},
        {"name":"Gary O.", "email":"p@test.com"},
    ]
}

for s in contacts["students"]:
    print(s["email"])