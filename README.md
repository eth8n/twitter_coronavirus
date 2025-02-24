# Coronavirus twitter analysis

This mini project applies basic analysis on a 2.7 TB dataset containing geotagged tweets, monitoring coronavirus related social media activity. Using a [MapReduce](https://en.wikipedia.org/wiki/MapReduce), procedure, the primary purpose of this project was to parallelize data extraction for efficency.

Extracting the country, language, and hashtags each tweet used, I consolidate the data into <50KB summarized JSON files, then made a series of plots from the data using `visualize.py` and `alternative_reduce.py`.

Below are the Top 10 countries and languages for `#coronavirus` and `#코로나바이러스`. As MatPlotLib does not support Korean text, the latter hashtag is not displayed in the image. Also displayed from `alternative_reduce.py`, is a time series graph showing the number of tweets tweeted for each hashtag.


## Top 10 By Country:

<img src=output_images/combined.country.json_%23coronavirus_bar.png width=100% />


<img src=output_images/combined.country.json_%23코로나바이러스_bar.png width=100% />


## Top 10 By Language:

<img src=output_images/combined.lang.json_%23coronavirus_bar.png width=100% />


<img src=output_images/combined.lang.json_%23코로나바이러스_bar.png  width=100% />


##  The Number of tweets tweeted for each hashtag
Note: #covid was excluded from the dictionary in map.py, as such it was not included in the extracted data nor the plot.


<img src=output_images/alternative_reduce_line_plot.png  width=100% />
