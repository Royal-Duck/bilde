import pickle, os, sys

########## CONFIG ##########
src_dir : str = "src/"
lib_dir : str = "lib/"
bin_dir : str = "bin/"
intermediate_dir : str = "intermediate/"

main_file : str = "main.cpp"
executable_file : str = "main"

tracking_file : str = "tracking_builds.bin"
############################

arguments : list[str] = sys.argv

class File:
    def __init__(self, name : str = "", extension : str = "cpp"):
        self.last_time_edit : int = 0
        self.name : str = name
        self.extension : str = extension
    def check_compile(self, libs) -> bool:
        current_time_edit : int = os.path.getmtime(src_dir + self.name + "." + self.extension)
        if self.last_time_edit != current_time_edit or not os.path.exists(intermediate_dir+self.name+".o"):
            self.last_time_edit = current_time_edit
            os.system(f"g++ {src_dir + self.name}.{self.extension} -o {intermediate_dir + self.name}.o -c {libs} -I{lib_dir}")
            return True
        return False
    def exists(self) -> bool:
        if os.path.exists(src_dir + self.name + "." + self.extension):
            return True
        return False

libs : str = ""
files : list[File] = []

def load_tracking_file() -> None:
    global libs, files
    file = open(tracking_file, "rb")
    libs, files = pickle.load(file)
    file.close()

def save_tracking_file() -> None:
    file = open(tracking_file, "wb")
    obj = [libs, files]
    pickle.dump(obj, file)
    file.close()

def link() -> None:
    files_string : str = ""
    for file in files:
        files_string += intermediate_dir + file.name + ".o "
    os.system(f"g++ {files_string}-o {bin_dir}{executable_file} {libs} -I{lib_dir}")

def append_lib(lib : str) -> None:
    global libs
    if not (f"-l{lib}" in libs.split(" ")):
        libs += f"-l{lib} "
        return
    print(f"failed to append the library {lib}, already keeping track of it")

def remove_lib(lib : str) -> None:
    global libs
    if not f"-l{lib} " in libs:
        print(f"not keeping track of any lib called '{lib}'.")
        return
    libs = libs.replace(f"-l{lib} ", "")

def clear_unexistant_files() -> None:
    for i, file in enumerate(files):
        if not file.exists():
            del files[i]

def append_file(file : str) -> None:
    global files
    name, extension = file.split(".")
    for c_file in files:
        if name == c_file.name and extension == c_file.extension:
            print(f"failed to append the file {file}, already keeping track of it.")
            return
    files.append(File(name, extension))

def remove_file(file : str) -> None:
    name, extension = file.split(".")
    for i, c_file in enumerate(files):
        if c_file.name == name and c_file.extension == extension:
            del files[i]
            return
    print(f"not keeping track of any file called {file}.")

if not os.path.exists(tracking_file):
    temp_file = open(tracking_file, "x")
    temp_file.close()

with open(tracking_file, "rb") as f:
    if f.readlines() != []:
        load_tracking_file()

clear_unexistant_files()

if files == []:
    append_file(main_file)

match arguments[1]:
    case "run":
        anything_compiled = False
        for file in files:
            if file.check_compile(libs):
                anything_compiled = True
        if anything_compiled or (not(os.path.exists(bin_dir+executable_file))):
            link()
        os.system(bin_dir + executable_file)
    case "append":
        append_file(arguments[2])
    case "remove":
        remove_file(arguments[2])
    case "lib":
        if arguments[2] != "-r":
            append_lib(arguments[2])
        else :
            remove_lib(arguments[3])
    case "comp":
        for file in files:
            file.check_compile(libs)
        link()

save_tracking_file()
