from appJar import gui
count = 0 

def press():
    print("Username Entry:", app.entry("Username"),
          "With Password: ", app.entry("Password"))
    if (app.entry("Username")) == 'Joon' and (app.entry("Password")) == 'password':
        username = app.entry("Username")
        password = app.entry("Password")
        app.infoBox(f"Login Successful | {username}",
                    f"Welcome {username} to Travel App!")
        app.stop()
        
        def images(): 
            global count
            count += 1
            loginedapp.label("Country", "Australia")
            loginedapp.label("information", "Woah W CRASH SYDNEY NO WAY??? OPERA HOUSE YOO CLAM LOOKING HOUSE SO FAMOUS MAN.")
            if count == 1:
                loginedapp.setLabel("Country", "Indonesia")
                loginedapp.setImage("Image", "japan.png")
                loginedapp.reloadImage("Image", "japan.png")
                loginedapp.setLabel("information", "omg I love indonesia w country so much baboons yay.")
            elif count == 2:
                loginedapp.setLabel("Country", "China")
                loginedapp.setLabel("information", "good country I love china")
                loginedapp.setImage("Image", "china.jpg")
                loginedapp.reloadImage("Image", "china.jpg")
            elif count == 3:
                loginedapp.setLabel("Country", "Japan")
                loginedapp.setLabel("information", "watashiwa arigato desu")
                loginedapp.setImage("Image", "operahouse.png")
                loginedapp.reloadImage("Image", "operahouse.png")
            elif count == 4: 
                loginedapp.setLabel("Country", "Yugoslavia")
                loginedapp.setLabel("information", "W cunttry Idk the name but ok")
                loginedapp.setImage("Image", "Yugoslavia.png")
                loginedapp.reloadImage("Image", "Yugoslavia.png")


        with gui("Travel App", "1000x200", bg='yellow', font={'size': 18}) as loginedapp:
            loginedapp.label("Welcome to Travel App", bg='blue', fg='orange')
            loginedapp.label(
                f"You are currently logged in as {username}!", bg='green')
            loginedapp.addImage("Image", "Australia.png")
            loginedapp.addButtons(
                ["Log out", "Show Images"], [loginedapp.stop, images])

with gui("Login Window", "400x200", bg='orange', font={'size': 18}) as app:
    app.label("Welcome to Travel App", bg='blue', fg='orange')
    app.entry("Username", label=True, focus=True)
    app.entry("Password", label=True, secret=True)
    app.addButtons(["Submit", "Cancel"], [press, app.stop])