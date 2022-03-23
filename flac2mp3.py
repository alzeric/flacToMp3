from re import search
import sys, os
from subprocess import call as subProCall

# Set this to your default audio download folder
audio_folder_default = "F:\\Downloads 2\\Audio"
ffmpeg_bin = "D:\VideoTools\FFMPEG\\bin\\ffmpeg.exe"

class FlacFinder:
    def __init__(self, settings):
        self.name = "FlaccFinder"
        
        '''
        self.settings = {
            "display_version": False,
            "debug": settings["debug"]
        }
        '''

        self.settings = {
            "version": "1.0.0.1",
            "ffmpeg": "ffmpeg",
            "display_version": False
        }

        for s in settings:
            self.settings[s] = settings[s]

        self.settings["ffmpeg"] = self.settings["ffmpeg_path"] if settings["ffmpeg_path"] else "ffmpeg"
        self.files = []

        if settings["version"]:
            self.settings["display_version"] = True

        if not settings["processing_path"]:
            print("Error: SearchDirectory has not been set")
            print("usage: FlacFinder('path_to_search_directory')")
            exit(0)

    def scanDirectory(self):        
        # r = Root | d = Directories | f = files
        for r, d, f in os.walk(self.settings["search_folder"]):
            for file in f:
                if '.flac' in file:
                    self.files.append(os.path.join(r, file))

    def run(self):
        print(self.settings)
        if self.settings["display_version"]:
            print(f"Library Name: {self.name} | Version: {self.settings['version']}")
            exit(0)
        print(f"Debug: {self.settings['debug']}")
        print(f"Scanning Directory: {self.settings['search_folder']}")
        print(f"Delete Mode: {self.settings['allow_delete']} | Overwrite Mode: {self.settings['allow_overwrite']} | Verbose: {self.settings['verbose']}")
        self.scanDirectory()
        for f in self.files:
            self.flacToMP3(f)

    def flacToMP3(self, file):
        cmd = f'{self.settings["ffmpeg"]} {"-y" if self.settings["allow_overwrite"] else "-n"} -i "{file}" -ab 320k -map_metadata 0 -id3v2_version 3 "{file.replace(".flac", ".mp3")}"'
        
        if self.settings["verbose"]:         
            print(cmd)
        
        if not self.settings["debug"]:
            subProCall(cmd)
        
        if self.settings["allow_delete"]:
            os.remove(file)
# END OF FlacFinder Class

processing_settings = {
    "allow_overwrite": False,
    "allow_delete": False,
    "processing_path": audio_folder_default,
    "ffmpeg_path": ffmpeg_bin if ffmpeg_bin else "ffmpeg",
    "verbose": False,
    "version": False,
    "debug": False
}

for a in sys.argv:
    if "-ao" in a:
        processing_settings["allow_overwrite"] = True
    elif "-ad" in a:
        processing_settings["allow_delete"] = True
    elif "search=" in a:
        processing_settings["processing_path"] = a.split("=")[1].replace('"', '')
    elif "ffmpeg=" in a:
        processing_settings["ffmpeg_path"] = a.split("=")[1].replace('"', '')
    elif a in ["verbose", "-v"]:
        processing_settings["verbose"] = True
    elif a in ["version", "-ver"]:
        processing_settings["version"] = True
    elif a in ["debug", "-debug"]:
        processing_settings["debug"] = True

ff = FlacFinder(settings=processing_settings)
ff.run()
