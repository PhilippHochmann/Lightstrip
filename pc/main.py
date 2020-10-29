from flask import Flask, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

from Lightstrip import LightstripState
from MusicVisualizationState import MusicVisualizationState
from Patterns import sectionCallback, barCallback, beatCallback, tatumCallback, segmentCallback, genericCallback

sp  = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state", redirect_uri='http://127.0.0.1:5001'))
vs  = LightstripState("/dev/ttyUSB0", 180)
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1><a href=/start>Fetch song</a></h1>"

@app.route('/start')
def start():
    global vs

    track = sp.current_playback()
    if track is None:
        return "No track playing right now"
    analysis = sp.audio_analysis(track["item"]["id"])
    start = time.time()
    track = sp.current_playback()
    time_offset = track["progress_ms"] / 1000 + (time.time() - start) / 2

    vs.endVisualization()
    ms = MusicVisualizationState(analysis, time_offset, sectionCallback, barCallback, beatCallback, tatumCallback, segmentCallback, genericCallback)
    vs.startVisualization(ms.update)

    return redirect("/")
