# Why pywav?
I am building a tool to test SIP applications. I am trying to convert RTP payload which was sent as PCMA/PCMU (mu-law or A-law compression) format. I tried [Python Wave](https://docs.python.org/3/library/wave.html) module but didn't work as expected because it will not consider any compression. So I digged a little bit and came up with my own way of creating and reading WAV files by looking at their formats [here](http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html).

# WavRead and WavWrite
There are two classes WavRead and WavWrite which will perform reading and writing of wave files respectively. Currenlty PCM, PCMU and PCMA formats are supported. You will get the raw data from the RTP stream which you can write into the wave file by providing information about the audio format, number of channels, sample rate etc.

# Reading example
```python
wave_read = pywav.WavRead("<filename to read>")
# print parameters like number of channels, sample rate, bits per sample, audio format etc
# Audio format 1 = PCM (without compression)
# Audio format 6 = PCMA (with A-law compression)
# Audio format 7 = PCMU (with mu-law compression)
print(wave_read.getparams())
```
# Writing example
```Python
# first parameter is the file name to write the wave data
# second parameter is the number of channels, the value can be 1 (mono) or 2 (stereo)
# third parameter is the sample rate, 8000 samples per second
# fourth paramaer is the bits per sample, here it is 8 bits per sample
# fifth parameter is the audio format, here it is 1 meand PCM with no compression.
wave_write = pywav.WavWrite("<filename to write>", 1, 8000, 8, 1)
# raw_data is the byte array. Write can be done only once for now. 
# Incremental write will be implemented later
wave_write.write(<raw data>)
# close the file stream and save the file
wave_write.close()
```