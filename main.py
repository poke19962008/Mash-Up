import librosa
import pickle, json, os

class mash:

    def __init__(self, json_, cached=False):
        self.sr = 22050  # new Sampling Rate for the audio files

        self.songs = json_
        self.Yin = []
        self.Yout = []

        self._setup()
        # self._load(cached=cached)

    def _setup(self):
        if not os.path.exists('cache'):
            os.makedirs('cache')

    def _load(self, cached=True):
        for song in self.songs:
            if os.path.exists("cache/%s.pkl"%song['name']):
                print "\nLoading", song['name'], "from cache"
                with open("cache/%s.pkl"%song['name'], 'rb') as f:
                    if song['mixin']:
                        self.Yin = pickle.load(f)
                    else:
                        self.Yout.append(pickle.load(f))
                continue

            print "\nLoading", song['name']
            y, sr = librosa.load(song['path'], sr=self.sr)
            if song['mixin']:
                self.Yin = y
            else:
                self.Yout.append(y)
            print "[SUCCESS] Loaded", song['name']

            if cached:
                try:
                    with open('cache/%s.pkl'%song['name'], 'wb') as f:
                        pickle.dump(y, f)
                        print "[SUCCESS] Cached", song['name']
                except Exception as e:
                    print "[FAILED] Caching", song['name']
                    print e



if __name__ == '__main__':
    with open('songs.json', 'r') as f:
        j = json.loads(f.read())
        obj = mash(j, cached=True)
