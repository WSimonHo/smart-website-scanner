import csv
import random

# Read the contents of the first CSV file
# file1 = './csv/train/normal_content_without_url_3.csv'
file1 = '/Users/simhoz/Desktop/ai-modal/rnn/website_url_5_b.csv'
data1 = []
with open(file1, 'r') as csv_file1:
    reader1 = csv.reader(csv_file1)
    next(reader1)  # Skip the header row
    data1 = list(reader1)

# Read the contents of the second CSV file
# file2 = './csv/train/website_content_without_url_3.csv'
file2 = '/Users/simhoz/Desktop/ai-modal/rnn/website_url_5_p.csv'
data2 = []
with open(file2, 'r') as csv_file2:
    reader2 = csv.reader(csv_file2)
    next(reader2)  # Skip the header row
    data2 = list(reader2)

# Combine the data from both files into a single list
merged_data = data1 + data2

# Disorganize the data by shuffling the list
random.shuffle(merged_data)

# Write the merged and disorganized data to a new CSV file
output_file = './csv/train/train_dataset_6.csv'
with open(output_file, 'w', newline='') as csv_output:
    writer = csv.writer(csv_output)
    writer.writerow(['url','result'])  # Adjust the column headers as needed

    for row in merged_data:
        writer.writerow(row)