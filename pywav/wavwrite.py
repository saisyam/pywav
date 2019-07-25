import struct

class WavWrite:
    def __init__(self, f, channels, samplerate, bitspersample, audioformat):
        self._file = open(f, "wb")
        self._numofchannels = channels
        self._samplerate = samplerate
        self._bitspersample = bitspersample
        if (audioformat != 1 and audioformat != 6 and audioformat != 7):
            raise Exception("Unsupported audio format")
        self._audioformat = audioformat
    
    def write(self, rawdata):
        self._file.write(b'RIFF')
        datalength = len(rawdata)
        if self._audioformat == 1:
            self._file.write(struct.pack('<L4s4sLHHLLHH4s',
            36 + datalength, b'WAVE', b'fmt ', 16,
            self._audioformat, self._numofchannels, self._samplerate,
            int(self._numofchannels * self._samplerate * (self._bitspersample/8)),
            int(self._numofchannels*(self._bitspersample/8)), self._bitspersample, b'data'))
        elif self._audioformat == 6 or self._audioformat == 7:
            self._file.write(struct.pack('<L4s4sLHHLLHHH4sLL4s',
            50 + datalength, b'WAVE', b'fmt ', 18,
            self._audioformat, self._numofchannels, self._samplerate,
            int(self._numofchannels * self._samplerate * (self._bitspersample/8)),
            int(self._numofchannels*(self._bitspersample/8)), self._bitspersample, 0, b'fact', 4, 
            datalength, b'data'))

        self._file.write(struct.pack('<L', datalength))
        self._file.write(rawdata)
    
    def close(self):
        self._file.close()

        
    
