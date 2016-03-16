lastfm-tools
============

Some Python CLI tools for talking to the Last.fm API.

Uses [pylast](https://github.com/pylast/pylast):

```
pip install pylast
```

puss's script - scrobble_fix.py
-------------------------------
run with pythonw in order to scrobble whatever is playing in winamp : )

np.py
-----
Show my now playing song, or that of a given username.


lastplayed.py
-------------

Shows the last 20 tracks you scrobbled (or of a given username).

Or shows all the last scrobbled tracks by an artist (or just of a given track).

loveit.py
---------

Loves whatever track is now playing on Last.fm, then prints confirmation of last loved track.

loved.py
--------

Shows your last 20 (or a given number of) loved tracks.

nowplaying.py
-------------

Command-line loopy thing to show what a Last.fm user is now playing. Based on [bbcscrobbler](https://github.com/hugovk/bbcscrobbler).

scrobble.py
-----------

Takes a track and scrobbles it
 * Mandatory parameter 1: "artist - track"
 * Optional parameter 2: UNIX timestamp. Default: now

unscrobble.py
-------------

After prompting, removes your last scrobbled track from your library. Use `--number` to unscrobble lots at a time.

mylast.py
---------

Config and common things. You need your own Last.fm API key and secret, get them from http://www.last.fm/api/account and put them here. Also put your username and either password or password hash.


