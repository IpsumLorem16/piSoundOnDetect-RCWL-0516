# piSoundOnDetect-RCWL-0516
Raspberry pi project, play sound when movement detected with the RCWL-0516

Made to play 'monster' sounds via blutooth speaker for Halloween.

Plays sound once, and lights LED while movement detected. Sleeps for 5 seconds after playing sound.

Will only trigger sound once if continously moving. LED being off means it is ready to detect again.

Uses pyGame to play sounds. I got the sounds for free from: https://pixabay.com/sound-effects/ (I did not upload what I used here). And used FFmpeg to convert to .wav files, as well as trim the length.
