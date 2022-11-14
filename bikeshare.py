import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please Select The City Name (chicago, new york city, washington) : \n").lower()
    while city not in CITY_DATA.keys():
        print("Please Make Sure That You Selected The Right City Name")
        city = input("Please Select The City Name (chicago, new york city, washington) : \n").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january","february","march","april","may","june","all"]
    while True:
        month = input("Please Select The Month :(january,february,march,april,may,june,all) : \n").lower()
        if month in months:
            break
        else:    
            print("Wrong Input")
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["sunday","monday","tuesday","wednesday","thursday","friday","all"]
    while True:
        day = input("Please Select The Day :(sunday,monday,tuesday,wednesday,thursday,friday,all) : \n").lower()
        if day in days :
            break
        else :
            print("Wrong Input")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df["Start Time"] = pd.to_datetime(df["Start Time"]) 
    
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["start_hour"] = df["Start Time"].dt.hour
    
    if month != "all":
        months = ["january","february","march","april","may","june"]
        month = months.index(month) +1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The Most Comman Month is : {}".format(df["month"].mode()[0]))

    # TO DO: display the most common day of week
    print("The Most Comman Day Of Week is : {}".format(df["day_of_week"].mode()[0]))

    # TO DO: display the most common start hour
    print("The Most Comman Start Hour is : {}".format(df["start_hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The Most Comman Start Station is : {}".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("The Most Comman End Station is : {}".format(df["End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df["trip_route"]=df["Start Station"]+","+df["End Station"]

    print("The Most Comman Trip Route is : {}".format(df["trip_route"].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The Total Travel Time is :",(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("The Average Travel Time is :",(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The Count Of Users is :",df["User Type"].value_counts().to_frame())

    # TO DO: Display counts of gender
    if city != "washington":      
        print("The Count Of Genders is :",df["Gender"].value_counts().to_frame())      
    # TO DO: Display earliest, most recent, and most common year of birth
        print("The Eaeliest Year Of Birth is :",int(df["Birth Year"].min()))
        print("The Recent Year Of Birth is :",int(df["Birth Year"].max()))
        print("The Most Comman Year Of Birth is :",int(df["Birth Year"].mode()[0]))     
    else:
          print("This City Has NO Data About Gender Counts.")
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

          
          
def display_data(df):
          print("Here Is a Sample of Row Data If you Want To Check \n")
          index=0
          i=input("If You Want To Check 5 Rows From The Data, Please Type Yes or No...\n").lower()
          if i not in ["yes" , "no"]:
              print("OOPs! Wrong Input, Please Make Sure You Type Yes or No \n")
              i=input("If You Want To Check 5 Rows From The Data, Please Type Yes or No...\n").lower()
          elif i != "yes":
              print("\n << Thank You For Your Time >> \n") 
          else:
              while index+5 < df.shape[0]:
                print(df.iloc[index:index+5])
                index += 5
                i=input("Would You Like To Check Another 5 Rows From The Data, Please Type Yes or No...\n").lower()
                if i != "yes":
                    print("\n << Thank You For Your Time >> \n")
                    break
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)  

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
