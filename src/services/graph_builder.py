
import os
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

def build_graph_percentage_delayed_flights_per_airline():
    """ Histogram """
    movies = read_json()
    movies_rating_list = [infos["rate"] for movie, infos in movies.items()]

    plt.figure(figsize=(10, 6))
    plt.hist(movies_rating_list, bins=20, edgecolor='black', alpha=0.75, color='royalblue')

    mean_rating = float(np.mean(movies_rating_list))
    plt.axvline(mean_rating, color='red', linestyle='dashed', linewidth=2,
                label=f'Average Rating: {mean_rating:.2f} IMDb')

    plt.title('Distribution of Ratings', fontsize=14)
    plt.xlabel('Rating (IMDb)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend()

    plt.savefig("rating_histogram.png")

def build_graph_percentage_delayed_flights_per_our_of_day():
    pass