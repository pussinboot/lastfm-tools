import win32gui
import time, datetime
from mylast import *

class ScrobbleDaemon:
	def __init__(self):
		self.last_name = None

	def get_hwnd(self):
		return win32gui.FindWindow('Winamp v1.x', None)

	def get_np(self):
		hwnd = self.get_hwnd()
		if hwnd == 0: return
		wintitle = win32gui.GetWindowText(hwnd)
		if wintitle[-9:] == '[Stopped]' or wintitle[-8:] == '[Paused]':
			#print(wintitle[-9:])
			return
		wintitle = wintitle[:-9]
		# r/a/dio hacks :^)
		if wintitle[-9:] == '(R/a/dio)':
			wintitle = wintitle[:-10]
		return wintitle

	def scrobble_track(self,timestamp=None):
		if timestamp is None:
			timestamp = int(time.mktime(datetime.datetime.now().timetuple()))
		np = self.get_np()
		if np is None or np == self.last_name: return
		(artist, track) = split_artist_track(np)
		lastfm_network.scrobble(artist=artist, title=track, timestamp=timestamp)
		print(time.strftime("%H:%M"),"\t",np)
		self.last_name = np

	def run(self):
		try:
			while True:
				time.sleep(5)
				self.scrobble_track()
		except KeyboardInterrupt:
			pass
		finally:
			print('shutting down')

if __name__ == '__main__':
	daemon = ScrobbleDaemon()
	daemon.run()