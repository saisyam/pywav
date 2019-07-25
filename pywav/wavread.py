import struct

class WavRead:
    def __init__(self, f):
        self._file = open(f, "rb")
        self._numchannels = 0
        self._samplerate = 0
        self._byterate = 0
        self._bytespersample = 0
        self._bitspersample = 0
        self._samplelength = 0
        self._data = None
        self._audioformat = 0
        self._extraparams = -1
        self.__read()
        self._file.close()

    def getnumofchannels(self):
        return self._numchannels
    
    def getsamplerate(self):
        return self._samplerate
    
    def getbyterate(self):
        return self._byterate
    
    def getbytespersample(self):
        return self._bytespersample
    
    def getbitspersample(self):
        return self._bitspersample
    
    def getsamplelength(self):
        return self._samplelength
    
    def getdata(self):
        return self._data

    def getaudioformat(self):
        return self._audioformat
    
    def getparams(self):
        params = {}
        params['numchannels'] = self._numchannels
        params['samplerate'] = self._samplerate
        params['byterate'] = self._byterate
        params['bytespersample'] = self._bytespersample
        params['bitspersample'] = self._bitspersample
        params['samplelength'] = self._samplelength
        params['audioformat'] = self._audioformat

        return params

    def __read(self):
        #RIFF header
        riff_chunk_id = self._file.read(4)
        if riff_chunk_id != b'RIFF':
            raise Exception("No RIFF header found")
        riff_chunk_size = struct.unpack('<I', self._file.read(4))[0]
                
        wave_format = self._file.read(4)
        if wave_format != b"WAVE":
            raise Exception("Not a WAVE file")
    
        # read fmt chunk
        fmt_chunk_id = self._file.read(4)
        if fmt_chunk_id != b'fmt ':
            raise Exception("fmt chunk missing")
        
        fmt_chunk_size = struct.unpack('<I', self._file.read(4))[0]
        self._audioformat = struct.unpack('<H', self._file.read(2))[0]
        self._numchannels = struct.unpack('<H', self._file.read(2))[0]
        self._samplerate = struct.unpack('<I', self._file.read(4))[0]
        self._byterate = struct.unpack('<I', self._file.read(4))[0]
        self._bytespersample = struct.unpack('<H', self._file.read(2))[0]
        self._bitspersample = struct.unpack('<H', self._file.read(2))[0]
        if fmt_chunk_size == 18:
            self._extraparams = struct.unpack('<H', self._file.read(2))[0]
            fact_chunk_id = self._file.read(4)
            if fact_chunk_id != b'fact':
                raise Exception("fact chunk missing")
            
            fact_chunk_size = struct.unpack('<I', self._file.read(4))[0]
            self._samplelength = struct.unpack('<I', self._file.read(4))[0]
        data_chunk_id = self._file.read(4)
        if data_chunk_id != b'data':
                raise Exception("data chunk missing")
        data_chunk_size = struct.unpack('<I', self._file.read(4))[0]
        if self._samplelength == 0: #no fact chunk
            self._samplelength = data_chunk_size
        self._data = self._file.read(data_chunk_size)