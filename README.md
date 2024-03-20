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