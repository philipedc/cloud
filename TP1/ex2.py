import matplotlib.pyplot as plot
from pyspark.sql.functions import *
from common import createSession

def load_and_preprocess_data(tracks, playlists):
    tracks_playlists = tracks.join(playlists, "pid")
    timed_tracks_playlists = tracks_playlists.withColumn("modified_at", to_timestamp("modified_at"))
    return timed_tracks_playlists

def get_top_artists_data(timed_tracks_playlists, num_artists):
    top_artists = timed_tracks_playlists.groupBy("artist_name") \
        .agg(countDistinct("pid")) \
        .orderBy("count(pid)", ascending=False) \
        .limit(num_artists)
    return top_artists

def plot_artist_data(top_artists, timed_tracks_playlists, filename):
    plot.figure(figsize=(10, 6))
    
    for artist in top_artists.collect():
        name = artist["artist_name"]
        data = timed_tracks_playlists.filter(timed_tracks_playlists["artist_name"] == name) \
            .groupBy(year("modified_at")).count().orderBy("year(modified_at)")
        data_pandas = data.toPandas()
        plot.plot(data_pandas["year(modified_at)"], data_pandas["count"], label=name)

    plot.title('Top Artists in the Last 5 Years')
    plot.xlabel('Year')
    plot.ylabel('Number of Playlists he/she appears')
    plot.legend()
    plot.savefig(filename)

def number_playlists_containing_top(sc, tracks, playlists, n=5):
    timed_tracks_playlists = load_and_preprocess_data(tracks, playlists)
    top_artists = get_top_artists_data(timed_tracks_playlists, n)
    plot_artist_data(top_artists, timed_tracks_playlists, "./images/ex2.png")

def main():

    spark = createSession()
    dataset = "hdfs://localhost:9000/datasets/spotify/"
    playlists = spark.read.json(dataset + 'playlist.json')
    tracks = spark.read.json(dataset + 'tracks.json')
    sc = spark.sparkContext

    number_playlists_containing_top(sc, tracks, playlists)
    sc.stop()


if __name__ == "__main__":
    main()