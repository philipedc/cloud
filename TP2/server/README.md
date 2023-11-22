# python-docker

A simple Python app for [Docker's Python Language Guide](https://docs.docker.com/language/python).

# Request Recommendations
Recommendations can be requested via curl, using command:
    curl localhost:32211/api/recommend -d '{"songs": [<song_list>]}' -H 'Content-Type: application/json'
