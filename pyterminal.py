# -*- encoding: utf-8 -*-
"""
Copyright (c) 2020. 17/12/2020.

About PyTerminal(pyterm):
------------------------
PyTerminal or pyterm is a combination of windows's command and python standards libraries.
It can interact with the python interpreter, the powershell and the CMD.

Author:
------
E-mail: baabdourahmane210@gmail.com

"""


import sys
import os
import platform
import webbrowser
from colorama import Fore


# Platform info.
system = platform.system()
machine = platform.machine()
version = platform.version()
print(f"{system} version [{version}] {machine}. Copyright(c) 2020.\n")
print(Fore.BLUE + f"\t\t\tPyTerminal\n" + Fore.RESET)

# set default profile.
os.chdir(os.environ['USERPROFILE'])
print(f"\t\tProfile: [{os.environ['USERPROFILE']}]\n")

# The prompte.
prompt = Fore.BLUE + "PyTerminal" + Fore.RESET

# Username
username = Fore.YELLOW + os.environ['USERNAME'] + Fore.RESET
# Environ path content. Store them in list.
paths = os.environ['PATH']
execs_list = []
for pathexc in paths.split(";"):
    execs_list.append(pathexc)

exc_file = []
for elem in execs_list:
    try:
        for p in os.listdir(elem):
            if p.endswith(".exe"):
                exc_file.append(p.rstrip(".exe"))
    except FileNotFoundError:
        pass

# Reserved keyword
kwd = ['False', 'await', 'else', 'import', 'pass',
       'None', 'break', 'except', 'in', 'raise',
       'True', 'class', 'finally', 'is', 'return',
       'and', 'continue', 'for', 'lambda', 'try',
       'as', 'def', 'from', 'nonlocal', 'while',
       'assert', 'del', 'global', 'not', 'with',
       'async', 'elif', 'if', 'or', 'yield']


# For openning a webbrowser.
def browse(url=None):
    browser = webbrowser.open(url, 1, True)
    return browser


# ls customized command.
def ls(path=os.getcwd()):
    conten = os.listdir(path)
    dic = {}
    for i in range(len(conten)):
        dic[i] = conten[i]
    print(f"\n  {path}\n  {len(path)*'-'}")
    for n, d in dic.items():
        if n < 10:
            print(f"   {n} | {d}")
        else:
            print(f"  {n} | {d}")
    print("\n")


# Main method.
def main():

    # Usage guide.
    usage = """
    Usage:
    
        commands:
        ? | /? | -help                          - Show this message help and exit.
        cd            [-path]                   - Change the directory. Use <..> to go back in directory.
        copy path1\\file2 | path1\\file2          - Copy a file or folder.
        del path\\file                           - Delete a file.
        echo                                    - Display in the standard output (console) what you type after.
        go            [-url]                    - Open web browser for internet.
        ls | lsd | ls [-path]                   - Show the content of current directory or given directory.
        mkdir  [-path] [dest\\name]              - Create a directory.
        open [-path]                            - Open a file or folder.
        q | quit | exit                         - Quit the console.
        read [-path] file                       - Read a file in the console. 
        ren [src\\file1|fd] [dest\\file2|fd]      - Rename a file or a directory.
        rmdir [-path] [src\\name]                - Remove a directory.
                                                  For read media file use <open vlc "path\\mediafile">
    """

    # Main loop.
    while True:

        try:

            # Prompte loop.
            loop = True

            while loop:
                name = input(f"{username}@{prompt}> ")
                args = f"{name}".split(" ")  # Make a list for args entered.

                msg = Fore.RED + "Error: Invalid cmd.  use ? for help" + Fore.RESET  # Error message.
                err_syntax = Fore.RED + "Syntax Error: separate the two files or folder by " + Fore.RESET + "'!'"
                err_expres = Fore.RED + "Error: check the expression." + Fore.RESET
                # Deal with entered args greater than two.
                if len(args) >= 2:

                    # ls cmd with -path and without it.
                    if args[0] == 'ls' and args[1] == '-path':
                        ls(path=' '.join(args[2:]))

                    elif args[0] == 'ls' and args[1] != '-path':
                        ls(path=' '.join(args[1:]))

                    # cd cmd with -path and without it.
                    elif args[0] == 'cd' and args[1] == '-path':
                        os.chdir(' '.join(args[2:]))
                        print(f"Current dir.: {os.getcwd()}\n")

                    elif args[0] == 'cd' and args[1] != '-path':
                        os.chdir(' '.join(args[1:]))
                        print(f"Current dir.: {os.getcwd()}\n")

                    # mkdir cmd with -path and without it.
                    elif args[0] == 'mkdir' and args[1] != '-path':
                        os.mkdir(' '.join(args[1:]))
                        print(f"[+] Done.")

                    elif args[0] == 'mkdir' and args[1] == '-path':
                        os.mkdir(' '.join(args[2:]))
                        print(f"[+] Done.")

                    # rmdir cmd with -path and without it.
                    elif args[0] == 'rmdir' and args[1] != '-path':
                        os.rmdir(' '.join(args[1:]))
                        print(f"[-] Removed.")

                    elif args[0] == 'rmdir' and args[1] == '-path':
                        os.rmdir(' '.join(args[2:]))
                        print(f"[-] Removed.")

                    # ren cmd with -path and without it.
                    elif args[0] == 'ren' and args[1] != '-path':
                        if '!' in args:
                            os.renames(' '.join(args[1:args.index('!')]), ' '.join(args[args.index('!')+1:]))
                        else:
                            print(err_syntax)

                    elif args[0] == 'ren' and args[1] == '-path':
                        if '!' in args:
                            os.renames(' '.join(args[2:args.index('!')]), ' '.join(args[args.index('!')+1:]))
                        else:
                            print(err_syntax)

                    # read cmd with -path and without it.
                    elif args[0] == 'read' and args[1] != '-path':
                        with open(' '.join(args[1:]), mode='r', encoding='utf-8') as file:
                            content = file.readlines()
                            for line in content:
                                print(f"{line.rstrip()}")
                        print("\n[Done.]")

                    elif args[0] == 'read' and args[1] == '-path':
                        with open(' '.join(args[2:]), mode='r', encoding='utf-8') as file:
                            data = file.readlines()
                            for line in data:
                                print(f"{line.strip()}")
                        print("\n[Done.]")

                    # open cmd with -path and without it.
                    elif args[0] == 'open' and args[1] != '-path':
                        os.system("start " + ' '.join(args[1:]))

                    elif args[0] == 'open' and args[1] == '-path':
                        os.system("start " + ' '.join(args[2:]))

                    # open cmd with vlc and -path and without -path.
                    elif args[0] == "open" and args[1] == 'vlc' and args[2] != "-path":

                        if platform.system() != 'Windows':
                            print("[/i\\] Start is only available on Windows platform.")
                        else:
                            if "VideoLAN\\VLC\\" in os.listdir("C:\\Program Files\\"):
                                last_dir = os.getcwd()
                                os.chdir("C:\\Program Files\\VideoLAN\\VLC\\")
                                os.system("vlc.exe" + str(' '.join(args[2:])))
                                os.chdir(last_dir)
                            else:
                                print("Install vlc.")

                    elif args[0] == "open" and args[1] == 'vlc' and args[2] == "-path":

                        if platform.system() != 'Windows':
                            print("[/i\\] Start is only available on Windows platform.")
                        else:
                            if "VideoLAN\\VLC\\" in os.listdir("C:\\Program Files\\"):
                                last_dir = os.getcwd()
                                os.chdir("C:\\Program Files\\VideoLAN\\VLC\\")
                                os.system("vlc.exe" + str(' '.join(args[3:])))
                                os.chdir(last_dir)
                            else:
                                print("Install vlc.")

                    # tree cmd with -path and without it.
                    elif args[0] == 'tree' and args[1] != '-path':
                        try:
                            os.system("tree " + " ".join(args[1:]))
                        except KeyboardInterrupt:
                            loop = False

                    elif args[0] == 'tree' and args[1] == '-path':
                        try:
                            os.system("tree " + " ".join(args[2:]))
                        except KeyboardInterrupt:
                            loop = False

                    # go cmd with -url and without it.
                    elif args[0] == 'go' and args[1] != '-url':
                        try:
                            browse(' '.join(args[1:]))
                        except TypeError:
                            print("Type a valid url.")

                    elif args[0] == 'go' and args[1] == '-url':
                        try:
                            browse(url=' '.join(args[2:]))
                        except TypeError:
                            print("Type a valid url.")

                    # copy cmd without -path.
                    elif args[0] == "copy" and args[1] != "-path":
                        if '!' in args:
                            os.system("copy " + " ".join(args[1:args.index("!")]) + " " +
                                      " ".join(args[args.index("!")+1:]))

                    # del cmd with -path and without it.
                    elif args[0] == "del" and args[1] != "-path":
                        os.system("del " + " ".join(args[1:]))

                    elif args[0] == "del" and args[1] == "-path":
                        os.system("del " + " ".join(args[2:]))

                    # echo cmd redirected in file in write mode by cleaning the existing content.
                    elif args[0] == "echo" and (">" in args):
                        with open(" ".join(args[args.index('>')+1:]), mode="w", encoding="utf-8") as file:
                            file.write(" ".join(args[1:args.index('>')]))

                    # echo cmd redirected in file in write mode by adding data to the existing content.
                    elif args[0] == "echo" and (">>" in args):
                        with open(" ".join(args[args.index('>>')+1:]), mode="a", encoding="utf-8") as file:
                            file.write(f"\n{' '.join(args[1:args.index('>>')])}")

                    # Return data after echo cmd
                    elif args[0] == "echo":
                        print(" ".join(args[1:]))

                    # Executes all executable file or cmd provides from the system path.
                    elif args[0] in exc_file:
                        os.system(str(name))

                    # Evaluate mathematical expressions or operations
                    elif args[0].isdigit():
                        try:
                            from math import cos, sin, tan, exp, e, pi, sqrt
                            print(f"[Output]: {eval(''.join(args))}")
                        except (SyntaxError, NameError):
                            print(err_expres)
                        except ZeroDivisionError:
                            print("Error: zero division!")

                    elif "".join(args).isdigit():
                        print(f"[Output]: {name.strip()}")

                    elif "".join(args).isascii() and "".join(args).isascii() not in kwd:
                        try:
                            from math import cos, sin, tan, exp, e, pi, sqrt
                            print(f"[Output]: {eval(''.join(args))}")
                        except (SyntaxError, NameError):
                            print(err_expres)
                        except ZeroDivisionError:
                            print(err_expres)

                # Deal with single argument.
                elif name == 'ls':
                    ls(path=os.getcwd())

                elif name == 'lsd':
                    os.system("dir")

                elif name == 'ren':
                    old = str(input(" Old : "))
                    new = str(input(" New : "))
                    os.renames(old, new)
                    print(f"[v] Renamed.")

                elif name == 'exit' or name == 'q' or name == 'quit':
                    sys.exit()

                elif name == '?' or name == '-help' or name == '/?':
                    print(usage)

                elif name == 'py':
                    os.system("py")

                elif name == 'cmd':
                    os.system("cmd")

                elif name == 'cls':
                    os.system("cls")

                elif name == 'tree':
                    try:
                        os.system("tree " + os.getcwd())
                    except KeyboardInterrupt:
                        loop = False

                elif name == '':
                    pass

                elif name in exc_file:
                    os.system(str(name))
                    raise FileNotFoundError("Not recognized as executable.")

                elif name.isdigit() or name.isascii() and name.isidentifier() is False:
                    try:
                        from math import cos, sin, tan, exp, e, pi, sqrt
                        print(f"[Output]: {eval(name)}")
                    except NameError:
                        print(err_expres)
                    except ZeroDivisionError:
                        print("Error: zero division!")

                elif name.isascii() and name.isidentifier() is False:
                    try:
                        print(f"[Output]: {eval(name)}")
                    except (SyntaxError):
                        print(err_expres)
                    except ZeroDivisionError:
                        print("Error: zero division!")

                else:
                    print(msg)

        except (TypeError, IOError, SyntaxError):
            pass
        except KeyboardInterrupt:
            print("\n")
            # print(" [/i\\] Invalid syntax: wrong cmd or missing given directori(es) or file(s).")


if __name__ == '__main__':
    if system != 'Windows':
        print("It is not yet tested on other platform than Windows.\n")
    else:
        main()
