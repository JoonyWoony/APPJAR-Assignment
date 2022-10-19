from appJar import gui
count = 0

print("Hello! The password to the application is Joon for Username and password for Password :)")


def press():
    print("Username Entry:", app.entry("Username"),
          "With Password: ", app.entry("Password"))
    # By getting the entry name, get the inputted answer and search if its Joon & password
    loweruser = app.entry("Username").lower()
    if (loweruser) == 'joon' and (app.entry("Password")) == 'password':
        username = app.entry("Username")
        password = app.entry("Password")
        app.infoBox(f"Login Successful | {username}",
                    f"Welcome {username} to Travel App!")
        print(
            '[⚠ WARNING] App will load after 1-10s due to the JPG Image processing being slow :)')
        app.stop()

    else:
        app.errorBox('Woah! We hit a roadblock',
                     "Your password or username was invalid.")


def korea():  # Makes life so much easier
    loginedapp.setLabel(
        'Welcome to Travel App', f'{username}, you are currently viewing: The experience of rich and unique Asian culture, Seoul (South Korea)')
    loginedapp.setLabel("ConInfo", "Seoul is the most amazing place to visit, offering amazing food, intriguing old culture, cutting-edge modern art, fashion, and technology, as well as the nicest people who want you to fall in love with their city and nation.")
    loginedapp.setLabel(
        "Statistics", "Area: 605.2 km²\nTemperature: 22 °C, Wind 8km/h, 49% Humidity\nPopulation: 9,400,000\nPopular Places to Visit: N Seoul Tower, Myeong-Dong, Lotte World, Gyeongbokgung Palace, Lotte Tower")
    loginedapp.setImage("CountryImage", 'Deagu.jpg')
    loginedapp.reloadImage("CountryImage", 'Deagu.jpg')


def america():
    loginedapp.setLabel(
        'Welcome to Travel App', f'{username}, you are currently viewing: Stunning beauty and the city that `Never Sleeps` Washington D.C (America)'
    )
    loginedapp.setLabel("ConInfo", "Washington, DC, one of the most visited cities in the USA, provides a range of engaging activities, from discovering American history and politics to visiting several of the nation's most famous landmarks. Great cuisine, fine art, cultural activities, and much more can be found in this dynamic city.")
    loginedapp.setLabel(
        "Statistics", "Area: 177 km²\nTemperature: 9 °C, Wind N at 0 km/h, 85% Humidity\nPopulation: 701,974\nPopular Places to Visit: United States Capitol, White House, Library of Congress, Lincoln Memorial")
    loginedapp.setImage("CountryImage", 'Seoul.jpg')
    loginedapp.reloadImage("CountryImage", 'Seoul.jpg')


def bali():
    loginedapp.setLabel(
        'Welcome to Travel App', f'{username}, you are currently viewing: The city of Ubud `Isle Of Gods` Bali (Indonesia)'
    )
    loginedapp.setLabel("ConInfo", "In the highlands of Bali, Indonesia, the town of Ubud is renowned as a hub for traditional arts and dance. What makes Indonesia a beautiful place to visit is theability to stopover in a variety of locations. Natural scenery is beautiful, and its inhabitants have a variety of distinctive cultures. ")
    loginedapp.setLabel(
        "Statistics", "Area: 42.38 km²\nTemperature: 27 °C, Wind S at 13 km/h\nPopulation: 74,800\nPopular Places to Visit: Sacred Monkey Forest Sanctuary, Saraswati Temple, Campuhan Ridge Walk")
    loginedapp.setImage("CountryImage", 'Incheon.jpg')
    loginedapp.reloadImage("CountryImage", 'Incheon.jpg')


def australia():
    loginedapp.setLabel('Welcome to Travel App',
                        f'{username}, you are currently viewing: Unique natural wonders and exotic wildlife, Sydney (Australia)')
    loginedapp.setLabel("ConInfo", "Why do I love Sydney? There are a lot of items on that list, I suppose. Great food, breathtaking scenery, the beach AND the city are both within reach, and the area is home to a multicultural population from all over the world.")
    loginedapp.setLabel(
        "Statistics", "Area: 12,368 km²\nTemperature: 18 °C, Wind NE at 13 km/h, 65% Humidity\nPopulation: 5,312,000\nPopular Places to Visit: Sydney Opera House, Bondi Beach, Sydney Harbour Bridge, Taronga Zoo Sydney")
    loginedapp.setImage("CountryImage", 'Daejeon.jpg')
    loginedapp.reloadImage("CountryImage", 'Daejeon.jpg')


def japan():
    loginedapp.setLabel('Welcome to Travel App',
                        f'{username}, you are currently viewing: Tradition overalapped with cutting edge technology, Tokyo (Japan)')
    loginedapp.setLabel(
        "Statistics", "Area: 2,194 km²\nTemperature: 23 °C, Wind E at 6 km/h, 73% Humidity\nPopulation: 13,960,000\nPopular Places to Visit: Tokyo Skytree, Meiji Jingu, Senso-Ji, Tokyo DisneyLand")
    loginedapp.setLabel("ConInfo", "Staying in Tokyo may provide you with a wealth of cultural experiences and a plethora of fresh memories. Keeping an open mind while you navigate the city might help you discover unique stores, eateries, and even just scenery. You might partake in a customary cultural event or try something new.")
    loginedapp.setImage("CountryImage", 'Ulsan.jpg')
    loginedapp.reloadImage("CountryImage", 'Ulsan.jpg')


def images():
    global count
    count += 1
    if count == 1:
        japan()
    elif count == 2:
        australia()
    elif count == 3:
        america()
    elif count == 4:
        korea()
    elif count == 5:
        bali()
    else:
        loginedapp.errorBox("ERROR | FINISHED_COUNTRY_CYCLE",
                            "You have already finished cycling through all countries that are available.")


def search():
    entryinput = loginedapp.entry("Search Country").lower()
    print(f"Searching Country with Input: {entryinput}")
    username = app.entry("Username").lower()
    if entryinput == 'japan':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        japan()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'australia':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        australia()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'korea':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        korea()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'america':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        america()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'bali':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        bali()
        loginedapp.setSize("fullscreen")
    else:
        loginedapp.clearAllEntries()
        print('[ERROR] Callback -> Entered Country Not Found')
        loginedapp.errorBox("Could Not Find Country! | ERROR",
                            "We were unable to find the country entered. Countries Available are: america, korea, australia, japan, bali")


with gui("Login Window", "400x200", bg='orange', font={'size': 16}) as app:
    app.label("Welcome to Travel App", bg='blue', fg='orange')
    app.entry("Username", label=True, focus=True)
    app.entry("Password", label=True, secret=True)
    app.addButtons(["Submit", "Cancel"], [press, app.stop])

with gui("Travel App", "1920x1080", bg='yellow', font={'size': 16}) as loginedapp:
    username = app.entry("Username")
    loginedapp.label('Welcome to Travel App',
                     f"{username}, you are currently viewing: The city of Ubud `Isle Of Gods` Bali (Indonesia)", bg='green')
    loginedapp.addLabel("ConInfo", "In the highlands of Bali, Indonesia, the town of Ubud is renowned as a hub for traditional arts and dance. What makes Indonesia a beautiful place to visit is theability to stopover in a variety of locations.")
    loginedapp.setLabelFont(size=10)
    loginedapp.addLabel(
        "Statistics", "Area: 42.38 km²\nTemperature: 27 °C, Wind S at 13 km/h\nPopulation: 74,800\nPopular Places to Visit: Sacred Monkey Forest Sanctuary, Saraswati Temple, Campuhan Ridge Walk")
    loginedapp.image("CountryImage", 'Ulsan.jpg')
    loginedapp.entry("Search Country", label=True, focus=True)
    loginedapp.addButtons(["Change Country", "Search", "Close Application"], [
        images, search, loginedapp.stop])
    loginedapp.startLabelFrame("SimpleFrame", 0, 1, 1)
    loginedapp.setLabelFrameTitle(
        "SimpleFrame", "Recommended Place to Visit: Museum Puri Lukisan")
    loginedapp.addImage("Simple", 'Attraction1.png')
    loginedapp.stopLabelFrame()
    loginedapp.setSize("fullscreen")
