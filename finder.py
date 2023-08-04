import pandas as pd 
import matplotlib.pyplot as plt 
import geopandas as gpd 

""" Begining of reading the csv file """
state_choice_query = ""

user_state=""
csv_reader = ""

def reader():
    
    df = pd.read_csv('iou_zipcodes_2020 (1).csv')
    query = df.query(f'state == "{user_state}"')
    state=query[['zip', 'utility_name', 'state', 'service_type']]
    global state_choice_query
    state_choice_query = state
    

def get_player_state():
    options = {
        "alabama": "AL",
        "alaska": "AK",
        "arizona": "AZ",
        "arkansas": "AR",
        "california": "CA",
        "colorado": "CO",
        "connecticut": "CT",
        "delaware": "DE",
        "Florida": "FL",
        "Ggeorgia": "GA",
        "hawaii": "HI",
        "idaho": "ID",
        "illinois": "IL",
        "indiana": "IN",
        "iowa": "IA",
        "kansas": "KS",
        "kentucky": "KY",
        "louisiana": "LA",
        "maine": "ME",
        "maryland": "MD",
        "massachusetts": "MA",
        "michigan": "MI",
        "minnesota": "MN",
        "mississippi": "MS",
        "missouri": "MO",
        "montana": "MT",
        "nebraska": "NE",
        "nevada": "NV",
        "new hampshire": "NH",
        "new jersey": "NJ",
        "new mexico": "NM",
        "new york": "NY",
        "north carolina": "NC",
        "north dakota": "ND",
        "ohio": "OH",
        "oklahoma": "OK",
        "oregon": "OR",
        "pennsylvania": "PA",
        "rhode island": "RI",
        "south carolina": "SC",
        "south dakota": "SD",
        "tennessee": "TN",
        "texas": "TX",
        "utah": "UT",
        "vermont": "VT",
        "virginia": "VA",
        "washington": "WA",
        "west virginia": "WV",
        "wisconsin": "WI",
        "wyoming": "WY",
        "district of columbia": "DC",
        "american Samoa": "AS",
        "guam": "GU",
        "northern mariana islands": "MP",
        "puerto rico": "PR",
        "united states minor outlying islands": "UM",
        "u.s. virgin islands": "VI",
    }
    while True: 
        print("Choose a state: ")
        for key, value in options.items():
            print(f"{key}: {value}") 
        user_input = input("Type type your state now: ").lower()
        if user_input in options: 
            return options[user_input]
        else:
            print("Ooooops Try again.")
        
strip_user_state = get_player_state()
user_state = strip_user_state.strip()           
csv_reader = reader()
print(user_state)
print(state_choice_query)

""" At this point we have chosen the state for the user, 
seperated that data from the csv file,
have selected specific columns to show,
and saved that to a variable caled state_choice_query"""



    
def get_user_zip():
    while True:
        try: 
            global user_zip
            user_zip_input = int(input("What is your zipcode? "))
        except ValueError:
            print("try numerical values")
        else: 
            break
        
    user_zip = user_zip_input
    if len(str(user_zip)) != 5:
        print("Please enter a 5 number zipcode ")
        get_user_zip()
    
    return user_zip


def zip_query():
    
    zip_file = state_choice_query.query(f'zip == {user_zip_choice}')
    return zip_file
    




user_zip_choice = (get_user_zip())
print(user_zip)
    
        
    

zip_choice_query = zip_query()

is_empty = zip_choice_query
print(is_empty)
def is_empty_function():
    while is_empty.empty == True:
        print("No zipcode found try again")
        global zip_choice_query
        zip_choice_query = get_user_zip()
        
    else:
        return

    


print(zip_choice_query)








            
