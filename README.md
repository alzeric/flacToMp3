# flacToMp3

## Join us on Discord for (almost) instant support/help/interaction
[https://discord.gg/N6ecRsmE](https://discord.gg/N6ecRsmE)

## What does this do? ##
Recursively finds and converts .flac files into .mp3 files 

## PreReqs ##
| ITEM          | Notes                                                             |
| ------------- | ----------------------------------------------------------------- |
| Python 3.9.10 | could work with other versions, just not tested/supported |
| FFMPEG | Recommended GPL build [Download](https://github.com/BtbN/FFmpeg-Builds/releases) |

## Usage ## 
  *Python flacToMp3.py*
  
   **CLI Options**
   |       flag      |                              description                              |
   | --------------- | --------------------------------------------------------------------- |
   | -ao | *allow overwrite (overwrite existing files without confirmation* |
   | -ad | *allow delete (deletes .flac files after conversion)* |
   | search="{PATH}" | *sets folder for processing (eg. search="C:\ToBeConvertedFolder")* |
   | ffmpeg="{PATH}" | *sets path to ffmpeg binary (eg. ffmpeg="C:\FFMPEG\bin\ffmpeg.exe")* |
   | verbose or -v | *enables verbose mode* |
   | version or -ver | *outputs version of flac2mp3 class* |
   | debug or -debug | *runs through all aspects of the script without processing or deleting* |

## Output ##
  
  **Out of the box what is the FFMPEG commang being used?**
  
  `ffmpeg (-y/-n) -i "{file}" -ab 320k -map_metadata 0 -id3v2_version 3 "{file.mp3}"`
  
  (-y/-n) is the overwrite file flag (y for yes | n for no) this is currently controlled via the -ao script flag see my code for an example.
  
  If you need assist feel free to pop in to discord and hit me up.

 **Can this be changed?**
 
 Yes quite easily, first line in the flacToMp3 def contains the current ffmpeg settings

## Hey you! Yeh You! ##
You're awesome for checking out this project I hope you enjoy this and any other apps/tools/scripts I create or help create.  

If you're having overwhelming thoughts of gratitude and want to shower me with gifts.... 

[$5 me love you long time or maybe toss me a ☕ that would actualy be pretty awesome of you!](https://www.buymeacoffee.com/Alzeric) 

or perhaps you wanna stuff me like a piggybank and throw coins at me... in that case BTC can be donated here: 

BTC Address: 3Kq2EmoxHqhRjPkmdbe2tK5qjvkoC1etiV

Hey and you keep being awesome, May the guitar/bass Rock Gods shine down on you and bathe you in Musical Glory!
