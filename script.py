# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def damages_cleaned(records):
    conversion = {"M": 1000000,
              "B": 1000000000}
    damages = []
    for record in records:
        if 'M' in record:
            new_record = record.replace('M', '')
            new_record = float(new_record) * conversion['M']
        elif 'B' in record:
            new_record = record.replace('B', '')
            new_record = float(new_record) * conversion['B']
        else:
            new_record = 'Damages not recorded'
        damages.append(new_record)    
    return(damages)
# test function by updating damages
Damages = damages_cleaned(damages) 

# 2 
# Create a Table
def hurricane_dict(Names, Months, Years, Max_winds, Affected_Areas, Damages, Deaths):
    sub = []
    for i in range(len(Names)):
        sub.append(dict(Name= Names[i], Month= Months[i], Year= Years[i], Maximum_Sustained_Wind= Max_winds[i], Areas_Affected = Affected_Areas[i], Damage = Damages[i], Deaths=Deaths[i]))
    main_dict = dict(zip(names,sub))
    return main_dict
# Create and view the hurricanes dictionary
Hurricane = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, Damages, deaths)
print(Hurricane)
# 3
# Organizing by Year
def hurricane_year_info(data):
    current_year =[]
    current_cane = []
    if type(data) == dict:
        for key in data.keys():
            current_year.append(data[key]['Year'])
        for value in data.values():
            new_value = [value]
            current_cane.append(new_value)
    return dict(zip(current_year, current_cane))
# create a new dictionary of hurricanes with year and key
hurricane_year = print(hurricane_year_info(Hurricane))

# 4
# Counting Damaged Areas
def count_damaged_areas(hurricane_data):
  Area = []
  Area_count = []
  for key, value in hurricane_data.items():
    for area in hurricane_data[key]['Areas_Affected']:
        Area.append(area)
        Area_count.append(Area.count(area))
  return(dict(zip(Area, Area_count)))

# create dictionary of areas to store the number of hurricanes involved in
Number_of_times_area_affected = count_damaged_areas(Hurricane)
print('\n', Number_of_times_area_affected)

# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(hurricane_data):
  v = hurricane_data.values()
  max_area_count = max(v)
  for k,v in hurricane_data.items():
    max_area = max(hurricane_data, key = hurricane_data.get)
  return (max_area, max_area_count)
# find most frequently affected area and the number of hurricanes involved in
area_most_affected = most_affected_area(Number_of_times_area_affected)
print('\nThe most area affected and the number of times is {}'.format(area_most_affected))

# 6
# Calculating the Deadliest Hurricane
def most_deaths(hurricane_info):
    highest_death = ''
    highest_death_count = 0
    for hurricane in hurricane_info:
        if hurricane_info[hurricane]['Deaths'] > highest_death_count:
            highest_death = hurricane
            highest_death_count = hurricane_info[hurricane]['Deaths']
    return highest_death, highest_death_count  
# find highest mortality hurricane and the number of deaths
highest_mortality = most_deaths(Hurricane)
print(highest_mortality)
# 7
# Rating Hurricanes by Mortality
def find_hurricane_mortality_rating(hurricane_info):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  hurricane_mortality_rating = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricane_info:
    if hurricane_info[hurricane]['Deaths'] == mortality_scale[0]:
        hurricane_mortality_rating[0].append(hurricane)
    elif mortality_scale[0] < hurricane_info[hurricane]['Deaths'] <= mortality_scale[1]:
        hurricane_mortality_rating[1].append(hurricane)
    elif mortality_scale[1] < hurricane_info[hurricane]['Deaths'] <= mortality_scale[2]:
        hurricane_mortality_rating[2].append(hurricane)
    elif mortality_scale[2] < hurricane_info[hurricane]['Deaths'] <= mortality_scale[3]:
        hurricane_mortality_rating[3].append(hurricane)
    elif mortality_scale[3] < hurricane_info[hurricane]['Deaths'] <= mortality_scale[4]:
        hurricane_mortality_rating[4].append(hurricane)
    else:
        hurricane_mortality_rating[5].append(hurricane)
  return hurricane_mortality_rating

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_mortality_grade = find_hurricane_mortality_rating(Hurricane)
print(hurricane_mortality_grade)

# 8 Calculating Hurricane Maximum Damage
def most_damage(hurricane_info):
    highest_damage = ''
    highest_cost = 0
    for hurricane in hurricane_info:
        if hurricane_info[hurricane]['Damage'] == 'Damages not recorded':
            hurricane_info[hurricane]['Damage'] = 0
        if hurricane_info[hurricane]['Damage'] > highest_cost:
            highest_damage = hurricane
            highest_cost = hurricane_info[hurricane]['Damage']
    return highest_damage, highest_cost
# find highest damage inducing hurricane and its total cost
hurricane_highest_damage = most_damage(Hurricane)
print(hurricane_highest_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def rate_hurricane_damage(hurricane_info):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    hurricane_damage_scale = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for hurricane in hurricane_info: 
        if hurricane_info[hurricane]['Damage'] == damage_scale[0]:
            hurricane_damage_scale[0].append(hurricane)
        elif damage_scale[0] < hurricane_info[hurricane]['Damage'] <= damage_scale[1]:
            hurricane_damage_scale[1].append(hurricane)
        elif damage_scale[1] < hurricane_info[hurricane]['Damage'] <= damage_scale[2]:
            hurricane_damage_scale[2].append(hurricane)
        elif damage_scale[2] < hurricane_info[hurricane]['Damage'] <= damage_scale[3]:
            hurricane_damage_scale[3].append(hurricane)
        elif damage_scale[3] < hurricane_info[hurricane]['Damage'] <= damage_scale[4]:
            hurricane_damage_scale[4].append(hurricane)
        else:
            hurricane_damage_scale[5].append(hurricane)
    return hurricane_damage_scale
# categorize hurricanes in new dictionary with damage severity as key
hurricane_damage_grade = rate_hurricane_damage(Hurricane)
print(hurricane_damage_grade)