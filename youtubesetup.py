from cx_Freeze import *

includefiles =  ['Graphics-Vibe-Shield-Badge-Social-Youtube.ico']
base =  None
if sys.platform == "win32":
    base = "win32GUI"


shortcut_table = [
    ("DesktopShortcut", #shortcut
     "DesktopFolder", #Directory
     "youtube_downloader", #Name
     "TARGETDIR", #component
     "[TARGETDIR]\main.exe",  #Target
     None,   #Arguments
     None,   #description
     None,   #hotkey
     None,    #item
     None,    #iconindex
     None,    #showcmd
     "TARGETDIR",  #wkdir
    )
]
msi_data = {"Shortcut":shortcut_table}

bdist_msi_options= {'data':msi_data}
setup(
    version="1.0",
    description="youtube downloader",
    author="rajat kesharwani",
    name="Rajat youtube",
    options={'build_exe':{'include_files':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='Graphics-Vibe-Shield-Badge-Social-Youtube.ico',
        )
    ]
)