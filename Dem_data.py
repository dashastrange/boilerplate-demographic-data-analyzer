import pandas as pd

adult_pop_df = pd.read_csv('adult.data.csv')

adult_pop_df.head()

# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
adult_pop_df['race'].value_counts()

# What is the average age of men?
male_age_series = adult_pop_df.loc[adult_pop_df['sex'] == 'Male', ['age']]
male_age_series.mean()

# What is the percentage of people who have a Bachelor's degree?
bach_degree_count = adult_pop_df.loc[adult_pop_df['education'] == 'Bachelors', 'education'].count()
edu_count = adult_pop_df['education'].count()
percent_degree = (bach_degree_count / edu_count) * 100

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) makes more than 50K?
advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
advanced_edu_df = adult_pop_df[adult_pop_df['education'].isin(advanced_edu)]
high_earners = advanced_edu_df[advanced_edu_df['salary'] == '>50K']
percentage = (len(high_earners) / len(advanced_edu_df)) * 100

# What percentage of people without advanced education makes more than 50K?
non_advanced_edu = ['HS-grad', '11th', '9th']
non_adv_edu_df = adult_pop_df[adult_pop_df['education'].isin(non_advanced_edu)]
another_high_earners = non_adv_edu_df[non_adv_edu_df['salary'] == '>50K']
percentage_non_edu = (len(another_high_earners) / len(non_adv_edu_df)) * 100

# What is the minimum number of hours a person works per week?
min_hrs = min(adult_pop_df['hours-per-week'])
min_hrs_work_df = adult_pop_df[adult_pop_df['hours-per-week'] == min_hrs]
min(adult_pop_df['hours-per-week'])

# What percentage of the people who work the minimum number of hours per week has a salary of more than 50K?
min_for_50k = min_hrs_work_df[min_hrs_work_df['salary'] == '>50K']
percentage_50k_min_hrs = (len(min_hrs_work_df) / len(high_earners)) * 100

# What country has the highest percentage of people that earn >50K and what is that percentage?
all_high_earners = adult_pop_df.loc[adult_pop_df['salary'] == '>50K', ['native-country', 'salary']]
all_high_earners_count = all_high_earners['native-country'].count()
countries_high_earning_df = all_high_earners[['native-country', 'salary']]
high_earn_count = all_high_earners['salary'].value_counts()
for country in countries_high_earning_df['native-country']:
    country_high_earners_count = countries_high_earning_df['native-country'].value_counts()

country_high_earners_count.sort_values(ascending=False)
top_country = country_high_earners_count.sort_values(ascending=False).head(1)
percentage_50K_top_country = (top_country / all_high_earners_count) * 100

# Identify the most popular occupation for those who earn >50K in India.
India_50k_occupation = adult_pop_df.loc[adult_pop_df['native-country'] == 'India', ['salary', 'occupation', ]]
high_earners_India = India_50k_occupation.loc[India_50k_occupation['salary'] == '>50K']
for occupation in high_earners_India:
    high_earners_occupations_count = high_earners_India['occupation'].value_counts()
top_occupation = high_earners_occupations_count.sort_values(ascending=False).head(1)
