# Mash Up

Mash Up is a small Python package that can mix 2 songs in the most desirable way. It has been made by following **FULL-AUTOMATIC DJ MIXING SYSTEM WITH OPTIMAL TEMPO ADJUSTMENT BASED ON MEASUREMENT FUNCTION OF USER DISCOMFORT** Research Paper published at 10th International Society for Music Information Retrieval Conference (ISMIR 2009).

For the demonstration purpose I have mashed [Fragmented](http://www.nihilus.net/soundtracks/Fragmented.mp3) and [Red E](http://www.nihilus.net/soundtracks/Red-e.mp3), each having tempo of 143 BPM and 123 BPM. Check out the **[Mashed Song](https://soundcloud.com/sayan-das-869256052/mash-up)**. Fade in starts at 5min 19seconds.

## DJ Mixing Technique

### Optimal Tempo Adjustment Coefficient Computation (OTAC)

In order to automatically generate a smooth Song to Song (StS) transition, a unique tempo adjustment technique is applied. It computes the optimal tempo adjustment coeffecients, here after described as OTAC, which express the factors of tempo adjustment for the songs to be consecutively played, thus it is capable of automatically generating smooth StS transition for any given combination of song. Diagram below shows the tempi of the target songs in StS transition. Here `Ta` & `Tb` are the tempo of song A & B.

![image](https://raw.githubusercontent.com/poke19962008/Mash-Up/master/res/sc1.png)

### Beat Adjustment and Crossfading

Here the two songs cross fades with each other. When songs with strong beats is adjusted to weaker beat of the other song, this cause discomfortness to hear.
So to eliminate the above problem it computed the `cross-correlation of the beats of the target songs withn the range of the cross fade`. For this it computes the power of located near the beat. The power of spectograme are computed by the `Fast Fourier Transformation` of the song sampled at `22,500Hz`.

## Song Selection

>This part is under construction!!
 
It will use aural similarity to determine the mashability of two song. Songs which have the highest similarity will be chosen.

For this it samples the audio at 22,500Hz converting it into raw power signal. Then Step Wise Fast Fourier Transformation (FFT) can be used to bin the power into 12 semi tones. Thus for each song we get 12*(number of sample points) matrix, called chroma.

![image](https://raw.githubusercontent.com/poke19962008/Mash-Up/master/res/sc2.png)

It will then compute the cosine distance between corresponding chroma vectors of the two songs to come up with an array of cosine distance. From their mean can be calculated. A smaller cosine distance means the songs have close semitone composition and thus well sound well together.

> Blog Comming Soon!!

## Dependencies
- Librosa
- PyDub
- Numpy

## To Do

- [ ] Complete Song Selection
- [ ] Reduce Dependencies

## References
- Ishizaki, H.; Hoashi, K. & Takishima, Y. (2009), Full-Automatic DJ Mixing System with Optimal Tempo Adjustment based on Measurement Function of User Discomfort., in Keiji Hirata; George Tzanetakis & Kazuyoshi Yoshii, ed., 'ISMIR' , International Society for Music Information Retrieval, , pp. 135-140 .


## Licence
The MIT License (MIT)
=====================

Copyright © `2016` `SAYAN DAS`

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
