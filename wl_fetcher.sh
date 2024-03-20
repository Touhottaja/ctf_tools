#!/bin/bash

# Author: touhottaja
# Name: wl_fetcher.sh
# Description: Single script to fetch wordlists from multiple sources

# List of git repos containing the wordlists
WORDLIST_GIT_URLS=("https://github.com/00xBAD/kali-wordlists.git" 
                   "https://github.com/danielmiessler/SecLists.git")

# Functions
display_header() {
    echo "__          ___          ______   _       _               "
    echo "\ \        / / |        |  ____| | |     | |              "
    echo " \ \  /\  / /| |  ______| |__ ___| |_ ___| |__   ___ _ __ "
    echo "  \ \/  \/ / | | |______|  __/ _ \ __/ __| '_ \ / _ \ '__|"
    echo "   \  /\  /  | |____    | | |  __/ || (__| | | |  __/ |   "
    echo "    \/  \/   |______|   |_|  \___|\__\___|_| |_|\___|_|   "
    echo
}

display_help() {
    echo "Usage: $0 [OPTION] [DIRECTORY]"
    echo "Fetches wordlists into the provided directory."
    echo
    echo "Options:"
    echo "-h, --help             Display this help message"
    echo "-d, --directory        Specify the directory to fetch wordlists into"
    echo "-l, --list             Lists repos from which wordlists are fetched"
    echo "-u, --update           Fetches updates for wordlists (if available)"
}

fetch_wordlists() {
    local directory=$1
    echo "Fetching wordlists into: $directory"

    # cd into the directory
    cd "$directory" || exit 1

    # Clone the wordlists from git using git clone
    for url in "${WORDLIST_GIT_URLS[@]}"; do
        echo "Fetching $url"
        git clone "$url"
        if [ $? -ne 0 ]; then
            echo "Error cloning $url"
        else
            echo "Successfully cloned $url"
        fi
    done
}

update_wordlists() {
    local directory=$1
    echo "Updating wordlists in: $directory"

    # cd into the directory
    cd "$directory" || exit 1

    # Get list of folders in the directory
    local folders=($(ls -d */))

    # Update the wordlists using git fetch and git rebase
    for folder in "${folders[@]}"; do
        echo "Updating $folder"
        cd $folder
        git fetch
        git rebase
        if [ $? -ne 0 ]; then
            echo "Error updating $folder"
        else
            echo "Successfully updated $folder"
        fi
        cd ..
    done
}

# Main
main() {
    display_header

    if [[ $1 == "-h" || $1 == "--help" ]]; then
        display_help
        exit 0
    elif [[ $1 == "-d" || $1 == "--directory" ]]; then
        directory="$2"
        if [ ! -d "$directory" ]; then
            echo "Directory does not exist"
            exit 1
        fi
        fetch_wordlists "$directory"
    elif [[ $1 == "-l" || $1 == "--list" ]]; then
        echo "The following repositories will be fetched:"
        for url in "${WORDLIST_GIT_URLS[@]}"; do
            echo "$url"
        done
        echo "Done!"
        exit 0
    elif [[ $1 == "-u" || $1 == "--update" ]]; then
        directory="$2"
        if [ ! -d "$directory" ]; then
            echo "Directory does not exist"
            exit 1
        fi
        update_wordlists "$directory"
        exit 0
    else
        echo "Invalid option: $1" 1>&2
        display_help
        exit 1
    fi
}

# Call the main function
main "$@"
