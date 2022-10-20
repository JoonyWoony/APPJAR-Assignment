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


def seoul():  # Makes life so much easier
    loginedapp.setLabel(
        'Welcome to Travel App', f'{username}, you are currently viewing: The experience of rich and unique Asian culture, Seoul (South Korea)')
    loginedapp.setLabel("ConInfo", "Seoul is the most amazing place to visit, offering amazing food, intriguing old culture, cutting-edge modern art,\n fashion, and technology, as well as the nicest people who want you to fall in love with their city and nation.")
    loginedapp.setLabel(
        "Statistics", "Area: 605.2 km²\nTemperature: 22 °C, Wind 8km/h, 49% Humidity\nPopulation: 9,400,000\nPopular Places to Visit: N Seoul Tower, Myeong-Dong, Lotte World, Gyeongbokgung Palace, Lotte Tower")
    loginedapp.setImage("CountryImage", 'Seoul.jpg')
    loginedapp.reloadImage("CountryImage", 'Seoul.jpg')


def incheon():
    loginedapp.setLabel(
        'Welcome to Travel App', f'{username}, you are currently viewing: The origin of Incheon International Airport, Incheon (South Korea)'
    )
    loginedapp.setLabel("ConInfo", "Tourists can find historical sites and significant locations all across the city.\nVisit Jayu Park, Chinatown, and the locations of the battles in Ganghwa-do to hear their untold tales.\nAnother reason travelers adore Incheon is the stunning backdrop the West Sea and its numerous islands provide.")
    loginedapp.setLabel(
        "Statistics", "Area: 1,066 km²\nTemperature: 11°C, Wind E at 5 km/h, 77% Humidity\nPopulation: 2,923,000]\nPopular Places to Visit: Songdo Central Park, Wolmido, Chinatown Incheon, Muuido, Incheon Bridge")
    loginedapp.setImage("CountryImage", 'Incheon.jpg')
    loginedapp.reloadImage("CountryImage", 'Incheon.jpg')


def daegu():
    loginedapp.setLabel(
        'Welcome to Travel App', f'{username}, you are currently viewing: Ancient culture and numerous scenic attractions, Daegu (South Korea)'
    )
    loginedapp.setLabel("ConInfo", "Daegu is one of the biggest cities in South Korea, and in addition to its numerous visual features and stunning mountains, it also boasts a rich and historical culture.\nExperience historical landmarks from the Silla and Joseon dynasties, as well as beautiful vistas of the Palgongsan and Apsan mountains.")
    loginedapp.setLabel(
        "Statistics", "Area: 886.6 km²\nTemperature: 8°C, Wind SE at 5 km/h, 69% Humidity\nPopulation: 2,465,000\nPopular Places to Visit: Seomun Market, Daegu 83 Tower, Apsan Park, Palgongsan, Daegu Art Museum")
    loginedapp.setImage("CountryImage", 'Deagu.jpg')
    loginedapp.reloadImage("CountryImage", 'Deagu.jpg')


def daejeon():
    loginedapp.setLabel('Welcome to Travel App',
                        f'{username}, you are currently viewing: The city of Science, Daejeon (South Korea)')
    loginedapp.setLabel("ConInfo", "Daejeon is known for being a transportation center and a city of science in South Korea, therefore there are many of things to do there.\nYou can take advantage of a wide range of sights and experiences in the city that is home to the KAIST national research university and Daedeok Science Town.")
    loginedapp.setLabel(
        "Statistics", "Area: 539.8 km²\nTemperature: 8°C, Wind NW at 2 km/h, 78% Humidity\nPopulation: 1,531,000\nPopular Places to Visit: Daejeon World, National Science Museum, Cheongnamdae")
    loginedapp.setImage("CountryImage", 'Daejeon.jpg')
    loginedapp.reloadImage("CountryImage", 'Daejeon.jpg')


def ulsan():
    loginedapp.setLabel('Welcome to Travel App',
                        f'{username}, you are currently viewing: rocky cliffs and sandy beaches, Ulsan (South Korea)')
    loginedapp.setLabel(
        "Statistics", "Area: 1,057 km²\nTemperature: 14°C, Wind N at 5 km/h, 43% Humidity\nPopulation: 1,166,000\nPopular Places to Visit: Daewangam Park, Taehwagang National Garden, Llsan Beach")
    loginedapp.setLabel("ConInfo", "the south-easternmost point of the Korean peninsula, known for its striking craggy cliffs and extensive swaths of sandy beaches.\nIt is famous for whaling, whale viewing, and having the biggest automobile manufacturing plant in the world.")
    loginedapp.setImage("CountryImage", 'Ulsan.jpg')
    loginedapp.reloadImage("CountryImage", 'Ulsan.jpg')


def images():
    global count
    count += 1
    if count == 1:
        seoul()
    elif count == 2:
        daegu()
    elif count == 3:
        daejeon()
    elif count == 4:
        ulsan()
    elif count == 5:
        incheon()
    else:
        count -= 5
        loginedapp.infoBox("CYCLE_FINISHED", "Hey! You finished cycling through all the cities that are available. Your cycle has been resetted")
        print(f'[RESET NOTIFICATION] Counter has been resetted. Incrementing from {count} now.')


def search():
    entryinput = loginedapp.entry("Search City").lower()
    print(f"Searching Country with Input: {entryinput}")
    username = app.entry("Username").lower()
    if entryinput == 'daegu':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        daegu()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'incheon':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        incheon()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'seoul':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        seoul()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'ulsan':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        ulsan()
        loginedapp.setSize("fullscreen")
    elif entryinput == 'daejeon':
        loginedapp.infoBox(
            f"Search Successful| {entryinput}", f"Hey {username}, you searched for {entryinput}.\nThe following country is being processed.")
        print("Loading Country Map... may take around 10 seconds :)")
        loginedapp.clearAllEntries()
        daejeon()
        loginedapp.setSize("fullscreen")
    else:
        loginedapp.clearAllEntries()
        print('[ERROR] Callback -> Entered City Not Found')
        loginedapp.errorBox("Could Not Find City! | ERROR",
                            "We were unable to find the city entered. Countries Available are: incheon, daejeon, daegu, ulsan, seoul")


with gui("Login Window", "400x200", bg='orange', font={'size': 16}) as app:
    app.label("Welcome to Travel App", bg='blue', fg='orange')
    app.entry("Username", label=True, focus=True)
    app.entry("Password", label=True, secret=True)
    app.addButtons(["Submit", "Cancel"], [press, app.stop])

with gui("Travel App", "1920x1080", bg='yellow', font={'size': 16}) as loginedapp:
    username = app.entry("Username")
    loginedapp.label('Welcome to Travel App',
                     f"{username}, you are currently viewing: The origin of Incheon International Airport, Incheon (South Korea)", bg='green')
    loginedapp.addLabel("ConInfo", "Tourists can find historical sites and significant locations all across the city.\nVisit Jayu Park, Chinatown, and the locations of the battles in Ganghwa-do to hear their untold tales.\nAnother reason travelers adore Incheon is the stunning backdrop the West Sea and its numerous islands provide.")
    loginedapp.setLabelFont(size=10)
    loginedapp.addLabel(
        "Statistics", "Area: 42.38 km²\nTemperature: 27 °C, Wind S at 13 km/h\nPopulation: 74,800\nPopular Places to Visit: Sacred Monkey Forest Sanctuary, Saraswati Temple, Campuhan Ridge Walk")
    loginedapp.image("CountryImage", 'Incheon.jpg')
    loginedapp.entry("Search City", label=True, focus=True)
    loginedapp.addButtons(["Change Country", "Search", "Close Application"], [
        images, search, loginedapp.stop])
    loginedapp.startLabelFrame("SimpleFrame", 0, 1, 1)
    loginedapp.setLabelFrameTitle(
        "SimpleFrame", "Recommended Place to Visit: Museum Puri Lukisan")
    loginedapp.addImage("Simple", 'Attraction1.png')
    loginedapp.stopLabelFrame()
    loginedapp.setSize("fullscreen")
