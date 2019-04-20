from cx_Freeze import setup, Executable

base = None    

executables = [Executable("PCS.py", base=base)]

packages = ["idna","urllib","requests","argparse"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "PCS",
    options = options,
    version = "1.0",
    description = '<Simple DynDNS Update Script>',
    executables = executables
)
