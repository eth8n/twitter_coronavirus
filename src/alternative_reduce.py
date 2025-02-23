#!/usr/bin/env python3
import argparse
import os
import json
import glob
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# Command line arguments: list of hashtags to plot and optionally the input folder
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True, help='List of hashtags to plot')
parser.add_argument('--input_folder', default='output', help='Folder containing mapping output files (e.g., *.lang files)')
args = parser.parse_args()

# Data structure: for each hashtag, a dictionary mapping day_of_year -> tweet count
hashtag_daily_counts = {hashtag: {} for hashtag in args.hashtags}

# Find all .lang files in the input folder. We assume mapping step produced files named like "geoTwitter20-01-01.zip.lang"
files = glob.glob(os.path.join(args.input_folder, '*.lang'))

# Process each file
for file_path in files:
    base_name = os.path.basename(file_path)
    # Expecting a pattern like: geoTwitter20-01-01.zip.lang
    if base_name.startswith("geoTwitter") and base_name.endswith(".zip.lang"):
        # Remove prefix and suffix to isolate the date string.
        # For example, "geoTwitter20-01-01.zip.lang" -> "20-01-01"
        date_str = base_name[len("geoTwitter"):-len(".zip.lang")]
        # Convert to full date; dataset is for 2020, so "20-01-01" becomes "2020-01-01"
        full_date_str = "2020" + date_str[2:]
        try:
            day_date = datetime.datetime.strptime(full_date_str, "%Y-%m-%d").date()
            day_of_year = day_date.timetuple().tm_yday
        except Exception as e:
            # If date parsing fails, skip this file.
            continue
    else:
        continue

    # Open the JSON file and load counts.
    with open(file_path) as f:
        counts = json.load(f)
    
    # For each hashtag, sum over all language counts if the hashtag is present.
    for hashtag in args.hashtags:
        if hashtag in counts:
            # Sum counts over all languages for this hashtag.
            total_count = sum(counts[hashtag].values())
        else:
            total_count = 0
        hashtag_daily_counts[hashtag][day_of_year] = total_count

# Plotting: For each hashtag, create a line (x-axis: day of the year; y-axis: tweet count)
plt.figure(figsize=(12, 8))
for hashtag, day_counts in hashtag_daily_counts.items():
    if day_counts:
        # Ensure we cover the full range of days present for this hashtag.
        min_day = min(day_counts.keys())
        max_day = max(day_counts.keys())
        days = list(range(min_day, max_day + 1))
        # For days with no data, default to 0.
        counts_per_day = [day_counts.get(day, 0) for day in days]
        plt.plot(days, counts_per_day, label=hashtag)
    else:
        # If no data, plot an empty line (or skip plotting)
        plt.plot([], [], label=hashtag)

plt.xlabel("Day of the Year")
plt.ylabel("Number of Tweets")
plt.title("Tweet Counts per Hashtag Throughout 2020")
plt.legend()
plt.tight_layout()

# Save the line plot as a PNG file
output_file = "alternative_reduce_line_plot.png"
plt.savefig(output_file)
print("Line plot saved as", output_file)
