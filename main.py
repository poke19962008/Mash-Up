import librosa
import numpy as np
import pickle, json, os

class mash:

    def __init__(self, json_, cached=False):
        self.sr = 22050  # new Sampling Rate for the audio files

        self.songs = json_
        self.Yin = []
        self.Yout = []
        self.beats = {'in': [], 'out': []}
        self.tempo = {'in': 0, 'out': 0}

        self._setup()
        self._load(cached=cached)
        self._extract()

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

    def _extract(self):
        # TODO: Add cosine distance similarity to choose the best mixout
        self.Yout = self.Yout[0] # NOTE: considering 1mixin & 1mixout

        self.tempo['in'], self.beats['in'] = librosa.beat.beat_track(y=self.Yin, sr=self.sr)
        self.tempo['out'], self.beats['out'] = librosa.beat.beat_track(y=self.Yout, sr=self.sr)

        self.OTAC()

    def OTAC(self): # Optimal Tempo Adjustment Coefficient Computation
        C = [-2, -1, 0, 1, 2]

        Tin_ = [(2**c)*self.tempo['in'] for c in C]
        TinIndex_ = np.argmin(np.absolute(Tin_, self.tempo['out']))
        Copt = Ta_[TinIndex_]

        Bopt = (2**Copt)*self.tempo['in']
        Tlow, Thigh = np.min(Bopt, self.tempo['out']), np.max(Bopt, self.tempo['out'])

        a, b = 2, 1
        Ttgt = (a-b)*Tlow + np.sqrt( ((a-b)**2)*(Tlow**2) + 4*a*b*Thigh*Tlow )
        Ttgt = Ttgt/(2*a)

        self.tempo['tgt'] = Ttgt



if __name__ == '__main__':
    with open('songs.json', 'r') as f:
        j = json.loads(f.read())
        obj = mash(j, cached=True)
