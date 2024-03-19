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

df = pd.read_csv("data/rainfall_names.csv")

# Group by the first and second columns and sum up the rest of the columns
df_grouped = df.groupby(['subdivision', 'YEAR']).sum().reset_index().round(2)


# Save the modified DataFrame back to a CSV file
df_grouped.to_csv("combined_regions.csv", index=False)


