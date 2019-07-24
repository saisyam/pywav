# Why pywav?
I am building a tool to test SIP applications. I am trying to convert RTP payload which was sent as PCMA/PCMU (mu-law or A-law compression) format. I tried [Python Wave](https://docs.python.org/3/library/wave.html) module but didn't work as expected because it will not consider any compression. So I digged a little bit and came up with my own way of creating and reading WAV files.

