import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from a file
    adult_pop_df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = adult_pop_df['race'].value_counts()

    # What is the average age of men?
    male_age_series = adult_pop_df.loc[adult_pop_df['sex'] == 'Male', ['age']]
    average_age_men = round(male_age_series['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bach_degree_count = adult_pop_df.loc[adult_pop_df['education'] == 'Bachelors', 'education'].count()
    edu_count = adult_pop_df['education'].count()
    percentage_bachelors = round((bach_degree_count / edu_count) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu_df = adult_pop_df[adult_pop_df['education'].isin(advanced_edu)]
    high_earners = advanced_edu_df[advanced_edu_df['salary'] == '>50K']
    percentage = round((len(high_earners) / len(advanced_edu_df)) * 100, 1)

    # What percentage of people without advanced education makes more than 50K?
    non_adv_edu_df = adult_pop_df[~adult_pop_df['education'].isin(advanced_edu)]
    another_high_earners = non_adv_edu_df[non_adv_edu_df['salary'] == '>50K']
    percentage_non_edu = round((len(another_high_earners) / len(non_adv_edu_df)) * 100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = percentage
    lower_education = percentage_non_edu

    # percentage with salary >50K
    non_advanced_edu = ['HS-grad', '11th', '9th']
    non_adv_edu_df = adult_pop_df[adult_pop_df['education'].isin(non_advanced_edu)]
    another_high_earners = non_adv_edu_df[non_adv_edu_df['salary'] == '>50K']
    lower_education_rich = (len(another_high_earners) / len(non_adv_edu_df)) * 100
    higher_education_rich = percentage

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_hrs = min(adult_pop_df['hours-per-week'])
    min_hrs_work_df = adult_pop_df[adult_pop_df['hours-per-week'] == min_hrs]
    min_work_hours = min(adult_pop_df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_for_50k = min_hrs_work_df[min_hrs_work_df['salary'] == '>50K']
    percentage_50k_min_hrs = (len(min_for_50k) / len(min_hrs_work_df)) * 100
    rich_percentage = percentage_50k_min_hrs

    # What country has the highest percentage of people that earn >50K?
    all_high_earners = adult_pop_df.loc[adult_pop_df['salary'] == '>50K', ['native-country', 'salary']]
    all_high_earners_count = all_high_earners['native-country'].count()
    countries_high_earning_df = all_high_earners[['native-country', 'salary']]
    high_earn_count = all_high_earners['salary'].value_counts()

    for country in countries_high_earning_df['native-country']:
        country_high_earners_count = countries_high_earning_df['native-country'].value_counts()

    country_all_people_count = adult_pop_df['native-country'].value_counts()
    percentage_50K_top_country = round((country_high_earners_count / country_all_people_count) * 100, 1)
    percentage_50K_top_country.sort_values(ascending=False)
    highest_earning_country_percentage = round(percentage_50K_top_country.sort_values(ascending=False).head(1).iloc[0], 1)
    highest_earning_country = percentage_50K_top_country.sort_values(ascending=False).index[0]

    # Identify the most popular occupation for those who earn >50K in India.
    India_50k_occupation = adult_pop_df.loc[adult_pop_df['native-country'] == 'India', ['salary', 'occupation', ]]
    high_earners_India = India_50k_occupation.loc[India_50k_occupation['salary'] == '>50K']
    for occupation in high_earners_India:
        high_earners_occupations_count = high_earners_India['occupation'].value_counts()
    top_IN_occupation = high_earners_occupations_count.sort_values(ascending=False).head(1).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
