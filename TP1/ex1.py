import matplotlib.pyplot as plot
import numpy as np

from pyspark.sql.functions import *
from pyspark.sql.window import Window

from common import createSession

COLUMN = "duration_ms"
ROWS = ["Minimum", "Mean", "Maximum"]

def get_outlier_data(tracks):
    # Treat data
    first_q, third_q = tracks.approxQuantile(COLUMN, [0.25, 0.75], 0)
    iqr = third_q - first_q
    
    bottom_range = first_q - (1.5*iqr)
    top_range = third_q + (1.5*iqr)
    
    filtered_tracks = tracks.filter((tracks[COLUMN] > bottom_range) & (tracks[COLUMN] < top_range))
    
    # Get data
    og_data = get_min_max_mean(tracks)
    filtered_data = get_min_max_mean(filtered_tracks)
    
    # Generate tables
    generate_table(og_data, "original")
    generate_table(filtered_data, "filtered")


def get_min_max_mean(df):
    my_max = df.agg({COLUMN: "max"}).collect()[0][0]
    my_min = df.agg({COLUMN: "min"}).collect()[0][0]
    my_mean = df.select(mean('duration_ms')).collect()[0][0]
    return [my_min, my_mean, my_max]
    
    
def generate_table(data, kind):
    fig, ax = plot.subplots()
    ax.axis('off')
        
    table_data = []
    for i in range(3):
        table_data.append([ROWS[i], data[i]])

    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.5, 1.5)
    plot.show()
    plot.savefig(f'./images/ex1_{kind}.png')

def main():
    spark = createSession()
    dataset = "hdfs://localhost:9000/datasets/spotify/"
    tracks = spark.read.json(dataset + 'tracks.json')
    sc = spark.sparkContext

    get_outlier_data(tracks)

    sc.stop()


if __name__ == "__main__":
    main()