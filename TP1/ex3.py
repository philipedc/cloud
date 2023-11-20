import matplotlib.pyplot as plot
import numpy as np

from pyspark.sql.functions import *
from pyspark.sql.window import Window

from common import createSession

def get_artist_cdf_by_playlist(tracks, playlists):
    # Data processing
    tracks_playlists = tracks.join(playlists, "pid")
    
    # Get table of top artists
    count_artists = tracks_playlists.groupBy("pid", "artist_name") \
        .agg(count("*").alias("artist_count")) \
        .orderBy("pid")
    count_window = Window.partitionBy("pid").orderBy(col("artist_count").desc())
    top_artist_by_playlist = count_artists.withColumn("rank", row_number().over(count_window)) \
        .filter(col("rank") == 1).select("pid", "artist_name", "artist_count")
        
    # Computing artist prevalence
    my_join = top_artist_by_playlist.join(playlists, "pid")
    song_prevalence = my_join.withColumn("prevalence", (my_join["artist_count"]/my_join["num_tracks"]))\
        .select("pid", "artist_name", "artist_count", "num_tracks", "prevalence")\
        .orderBy("prevalence")
    
    # Compute CDF with a little help from my friend Numpy
    data = song_prevalence.select("prevalence").rdd.flatMap(lambda x: x).collect()
    y = 1. * np.arange(len(data)) / (len(data) - 1)
    plot.plot(data, y)
    
    plot.title("Top Artist on Playlist's CDF")
    plot.xlabel('Artist (%)')
    plot.ylabel('Cummulative Distribution')
    plot.savefig("./images/ex3.png")

def main():
    spark = createSession()
    dataset = "hdfs://localhost:9000/datasets/spotify/"
    tracks = spark.read.json(dataset + 'tracks.json')
    playlists = spark.read.json(dataset + 'playlist.json')

    sc = spark.sparkContext

    get_artist_cdf_by_playlist(tracks, playlists)

    sc.stop()


if __name__ == "__main__":
    main()