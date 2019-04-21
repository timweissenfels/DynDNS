from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Updater.py", base=base)]

packages = ["idna","urllib","requests","argparse"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Updater-linux",
    options = options,
    version = "1.0",
    description = '<Simple DynDNS Update Script>',
    executables = executables
)
