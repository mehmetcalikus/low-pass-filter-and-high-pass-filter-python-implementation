# low-pass-filter-and-high-pass-filter-python-implementation

This code performs the (asymptotical) low pass filter (LPF) functions given
below (Figure 1 for 0 gain and Figure 2 for 5dB gain)

The desired filters are also added to the repo as figure.png

Also this code perform this LPF for fc=2000Hz and write out the output data into a file for both
audio samples I used a sample sound file named Africa.wav here and saved the outputs in the sound 
files named Africa5dBGainLPF.wav and Africa0dBGainLPF.wav etc, but you can make minor changes to 
the code to suit your own sound files.

Important Note: Please be careful about dtype(int16 or int8) and sample frequency of your sound file.

At last this code subtract the Low pass filtered audio signal from the original audio signal and 
get 2000Hz High Pass Filter applied (equivalent) audio stream.


You can access the audio(wav) files created as output of this code from this link:
https://drive.google.com/drive/folders/1_pHyhP4guFWKEa3k2B2jNW6t6SoNI-dg?usp=sharing


