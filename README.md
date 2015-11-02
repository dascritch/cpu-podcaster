### CPU podcaster

This piece of s...oftware is dedicated to take a full radio show in ready-to-broadcast wav format to

- full ogg vorbis broadcastable file
- full mp3 file for old podcast devices
- 

Entry files :
- .wav ready-to-broadcast named in a special fashion for getting metadata from file name.
- timeline export of audacity, to catch chapters time cues and names

Exports constraints :

- launching cpu_podcaster should ask a minimum interaction, but verify information before being really run
- mp3 files should be in a sub-directory `./podcast/` of each ogg file
- some sections must go in different sub-dir structure (mainly interviewes)
- mp3 and ogg should have meta tags information (id3)
- mp3 should embed "cover" image
- mp3 and ogg should support chaptering when available
- a chapters.html should be exported, for being inserted in blog post