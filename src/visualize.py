#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt 

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

top10_desc = sorted(counts[args.key].items(), key=lambda item: item[1], reverse=True)[:10]
# Then sort these top 10 in ascending order (low to high)
top10_sorted = sorted(top10_desc, key=lambda item: item[1])

# Extract keys and values for plotting
keys = [k for k, v in top10_sorted]
values = [v for k, v in top10_sorted]

# Create a bar graph
plt.figure(figsize=(10,6))
plt.bar(keys, values, color='skyblue')
plt.xlabel("Keys")
plt.ylabel("Counts")
plt.title("Top 10 keys for " + args.key)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the bar graph as a PNG file. The filename is based on the input file and key.
output_png = args.input_path + "_" + args.key + "_bar.png"
plt.savefig(output_png)
plt.close()

print("Bar graph saved as", output_png)
