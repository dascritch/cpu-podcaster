### CPU podcaster

This piece of s...oftware is dedicated to take a full radio show in ready-to-broadcast wav format to :

- full ogg vorbis broadcastable file
- full mp3 file for old podcast devices
- html excerpt with reference to segments

### Entry files :

- .wav ready-to-broadcast named in a special fashion for getting metadata from file name.
- timeline export of audacity, to catch chapters time cues and names

### Exports constraints :

- launching cpu_podcaster should ask a minimum interaction, but verify information before being really run
- cuted chapters audio files need at least 1/75th second precision on start and end (Audio CD frame precision)
- mp3 files should be in a sub-directory `./podcast/` of each ogg file
- some sections must go in different sub-dir structure (mainly interviewes)
- mp3 and ogg should have meta tags information (id3)
- mp3 should embed "cover" image
- mp3 and ogg should support chaptering when available
- a chapters.html should be exported, for being inserted in blog post. Chapters needs only precision to the second and indicate the start point, but specific link annotation according to [ondemiroir-audio-tag format](https://github.com/dascritch/ondemiroir-audio-tag)

### Example of html segment

Based on [release Ex0007 of the CPU radio show](http://cpu.dascritch.net/post/2015/10/29/Ex0007-Noms-de-domaines)

```html
<p>Chapitres </p>
<ol>
<li><a href="/post/2015/11/02/Bonjour-%C3%A0-toi%2C-enfant-du-futur-imm%C3%A9diat-%3A-j-ai-lou%C3%A9-cpu.pm">Bonjour à toi, enfant du futur immédiat : J'ai loué cpu.pm</a> — <a href="#&amp;t=1m18s">(1:18)</a></li>
<li>♪  The Who - <em>Who are you</em> — <a href="#&amp;t=15m10s">(15:10)</a></li>
<li>How to : Le système DNS — <a href="#&amp;t=18m2s">(18:02)</a></li>
<li>♪  Miss Kittin &amp; The Hacker- <em>I come .com</em> — <a href="#&amp;t=24m9s">(24:09)</a></li>
<li>Interview : Anthony Eden, fondateur et de DNSimple — <a href="#&amp;t=29m22s">(29:22)</a></li>
<li>♪  Étienne De Crecy - <em>Noname</em> — <a href="#&amp;t=47m10s">(47:10)</a></li>
<li>Plantage : Sex.com — <a href="#&amp;t=48m24s">(48:24)</a></li>
<li>♪  Bang Gang - <em>Stop in the name of love</em> — <a href="#&amp;t=54m26s">(54:26)</a></li>
<li><a href="/post/2015/10/31/M%C3%A9t%C3%A9o-%3A-en-vers-et-en-noms-de-domaine">Météo : en vers des domaines</a> — <a href="#&amp;t=56m44s">(56:44)</a></li>
</ol>
```