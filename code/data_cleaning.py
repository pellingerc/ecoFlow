import numpy
import csv
import pandas as pd


floods = "data/India_Floods_Inventory.csv"
population = "data/population.csv"
rainfall = "data/rainfall_in_india1901-2015.csv"

def get_first_column(csv_file):
    """
    Function to extract the first column of a CSV file.
    
    Args:
    csv_file (str): Path to the CSV file.
    
    Returns:
    list: The values in the first column.
    """
    first_column = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:  # Check if row is not empty
                first_column.append(row[1])
    return first_column

#states = get_first_column(population)[1:]
#remove last item
#states = states[:-1]


def shorten_text(text, words_to_match):
    text = text.lower()
    for word in words_to_match:
        if word in text:
            return word
    return text


def shorten_region(input_file_path, output_file_path, words_to_match):
    # Read input CSV and write to output CSV
    with open(input_file_path, 'r', newline='') as input_file, \
            open(output_file_path, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        for row in reader:
            # Shorten text in the first column
            shortened_text = shorten_text(row[0], words_to_match)
            row[0] = shortened_text
            writer.writerow(row)


# states = [word.lower() for word in states]
# shorten_region(rainfall, "data/rainfall_names.csv", states)

def remove_first_col(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            row = row[1:]
            row[0] = row[0].lower()
            writer.writerow(row) 

#remove_first_col(population, "data/population_rank.csv")

rainfall_pd = pd.read_csv("data/rainfall_names.csv")
population_pd = pd.read_csv("data/population_rank.csv")

# Group by the first and second columns and sum up the rest of the columns
rainfall_grouped = rainfall_pd.groupby(['subdivision', 'YEAR']).sum().reset_index().round(2)

# Rainfall post 1950
rainfall_post_1951 = rainfall_grouped[rainfall_grouped['YEAR'] > 1950]

# Rainfall pre 2012 and post 1950
rainfall_years = rainfall_post_1951[rainfall_post_1951['YEAR'] < 2012]

rainfall_years.to_csv("data/rainfall_years.csv", index=False)

# Filter for same regions
rainfall_regions = rainfall_years[rainfall_years['subdivision'].isin(population_pd['state or union territory'])]
rainfall_regions.to_csv("data/rainfall_regions.csv", index=False)

#rename pop columns to just year
population_pd = population_pd.rename(columns={'Population 1951' : '1951', 'Population 1961' : '1961', 'Population 1971' : '1971', 'Population 1981' : '1981', 'Population 1991' : '1991', 'Population 2001' : '2001', 'Population 2011' : '2011'})

population_pd.to_csv("data/population_years.csv", index=False)

#add population data to rainfall matching decade
populations = []
for index, row in rainfall_regions.iterrows():
    state = row['subdivision']
    year = row['YEAR']
    #pair year to 1951, 1961, 1971, 1981, 1991, 2001, 2011
    if year < 1961:
        year = 1
    elif year < 1971:
        year = 2
    elif year < 1981:
        year = 3
    elif year < 1991:
        year = 4
    elif year < 2001:
        year = 5
    elif year < 2011:
        year = 6
    else:
        year = 7
    population_row = population_pd[population_pd['state or union territory'] == state]
    population = population_row.iloc[0, year]
    populations.append(population)

rainfall_regions['Decade Population'] = populations

rainfall_regions.to_csv("data/rainfall_population.csv", index=False)




    

    


# # Now, merged_df contains the population data from the second dataframe added to the first dataframe
# merged_df.to_csv("data/merged_data.csv", index=False)


