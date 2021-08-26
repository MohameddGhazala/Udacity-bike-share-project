import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all' ,'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ["all", "monday", "tuesday", "wednesday", "thursday","friday","saturday", "sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("\n Let's make this a more comfortable experience, please follow my instructions \n")

    while True:
            city = str(input("\nPlease type city name you want data from! ex: 'chicago, new york city or washington' \n ").lower())
            if city not in CITY_DATA:
                print("Pleaase type city name correctly")
            else:
                print("Good! So you want to show data from Chicago!\n")
                break
            


    while True:
        month = str(input("Enter a month name in the first 6 months, if you'd like to apply no filter type all \n")).lower()
        if month not in MONTHS:        
                print("Oops! Please make sure you entered a valid month\n.")
        elif month == "all":
            print("Well then, it seems you don't want to filter by month.\n")
            break
        else:
            print("results will be shown for {}\n".format(month))
            break
       
    while True:
        day = str(input("please enter a day name, if you want to show all week's results type all.\n")).lower()
        
        if day not in DAYS:
            print("Oops! Please enter a valid day.")
        elif day == "all":
            print("Well then, No day filter will be applied.\n")
            break
        else: 
            print("results will be shown for {}\n".format(day))
            break

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
    #loading data from file
    df = pd.read_csv(CITY_DATA[city])
    
    #edit date format in 'Start date'
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    #extracting month 
    df['month'] = df['Start Time'].dt.month
    
    #extractind day
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour
    
    
    #checking whether to apply filter on month or not
    if month != 'all':
        month = MONTHS.index(month)
        df = df[df['month'] == month ]
    
    #checking whether to apply filter on day or not
    if day != 'all':
        
       df = df[df['day_of_week'] == day.title()]
    
    
      
    return df
def raw_data(df):
    """This function takes df as input and return 5 raws each iteration """
    
    start = 0
    while True:
        answer = input("Would you like to show first 5 raws of the data?[y / n]\n").lower()
        if answer== "y":
            pd.set_option('display.max_columns',200)
            print(df.iloc[start: start +5])
            start += 5
        else:
            break

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    print("Let's have some fun!\n")
   
    start_time = time.time()
    
    if month == 'all':
        while True:
            
            answer = input("Would you like to know the most common month, day & hour?[y/n]\n ").lower()
            if answer == "y":
                print('\nCalculating The Most Frequent Times of Travel...\n')
                popular_month = df['month'].mode()[0]
                print("{} is the most popular month\n".format(MONTHS[popular_month].title()))
                
                popular_day = df['day_of_week'].mode()[0]
                print("{} is the most popular day of the week\n".format(popular_day.title()))

                popular_hour = df['hour'].mode()[0]
                print('\nMost Frequent Start Hour:', popular_hour)
                break
            elif answer == "n":
                break
            else:
                print("please type y or n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    while True:
        answer = input("Would you like to show station stats? [y/n] \n").lower()
        if answer == "y":    
    
            popular_start_st = df['Start Station'].mode()[0]
            print('The most popular start station is: {}\n'.format(popular_start_st))

            popular_end_st = df['End Station'].mode()[0]
            print('\nThe most popular end station is: {}\n'.format(popular_end_st))

    #first creating new column for comination
            df['Combination']= df['Start Station'] + " ==> " + df["End Station"]
    #Then find the mode i.e most repeated combination
    
            comb = df["Combination"].mode()[0]
    
            print("\nAnd finally! The most frequent combination is from {}\n".format(comb))
            break
        else:
            break
        
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    while True:
        answer = input("Would you like to show trip duration stats? [y/n] \n").lower()
        if answer == "y":
                total_duration = df['Trip Duration'].sum()
                print("\nTotal Trip duration is {} hours \n".format(round((total_duration / 3600), 3)))
                 #  display mean travel time
                mean_duration = df['Trip Duration'].mean()
                print("\nThe mean trip duration is {} seconds. \n".format(round(mean_duration),2))
                break
        else:
                break
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    start_time = time.time()
    while True:
        answer = input("Would you like to show user stats? [y/n] \n").lower()
        if answer == "y":
            print('\nCalculating User Stats...\n')
            
    
            print("\nHere are some cool data about users!\n")
            #  Display counts of user types
            user_count = df['User Type'].value_counts()
            print(user_count)
        else:
            break
            

   
            if city != 'washington':

                gender_count = df['Gender'].value_counts()
                print(gender_count)
        

                most_recent = df['Birth Year'].max()
                print("\n\nMost recent year is {}\n".format(int(most_recent)))
        
                earliest_year = df['Birth Year'].min()
                print("\nThe earliest year of birth is {}\n".format(int(earliest_year)))
        
                common_year = df['Birth Year'].mode()[0]
                print("The most common year of birth is {}".format(int(common_year)))
                break
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

        
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

