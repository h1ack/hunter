import subprocess
import argparse
import asyncio
import time
from urllib.parse import urlparse, parse_qs
import os
from colorama import Style, Fore

# Colors
Green = Fore.GREEN
Blue = Fore.BLUE
Red = Fore.RED
reset = Style.RESET_ALL

# Banner
BNR = rf"""{Blue}
   __  _______ ____ ___  ___      
  /  |/  /_  /|_  // _ \/ _ \__ __
 / /|_/ //_ <_/_ </ // / // /\ \ / 
/_/  /_/____/____/____/\___//_\_\{Green}
                                  Meed - Tools ©
                             github : github.com/Mede1x{reset}
"""

async def run(command):
    """Execute a shell command asynchronously."""
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        print(f"{Red}Error while running: {command}{reset}")
        print(stderr.decode())
    else:
        print(stdout.decode())

async def fetch_parameters(input_file, output_file):
    """Fetch URLs from a file and write them to another file."""
    if not os.path.exists(input_file):
        print(f"{Red}Input file '{input_file}' does not exist.{reset}")
        return

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            url = line.strip()
            if url:
                outfile.write(f"{url}\n")

    print(f"{Green}[+] URLs extracted to '{output_file}'.{reset}")


def is_tool_installed(tool):
    """Check if a tool is installed."""
    return subprocess.call(['which', tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

async def main():
    print(BNR)

    parser = argparse.ArgumentParser(description="Subdomain enumeration tool v1.0 M33D")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    args = parser.parse_args()
    domain = args.domain

    print(f'[+] M33D0x | {time.ctime()} | ASYNC FOR {Green}{domain}{reset}\n')

    # Check tool installation
    for tool in ["subfinder", "httpx", "katana"]:
        if not is_tool_installed(tool):
            print(f"{Red}Error: {tool} is not installed!{reset}")
            return

    hunt_dir = f"{domain}.hunt"
    if not os.path.exists(hunt_dir):
        os.makedirs(hunt_dir)

    # Execute the tools
    start_time = time.time()
    await run(f"subfinder -d {domain} -o {hunt_dir}/{domain}.subdomain.txt")
    print(f"[+] Subfinder completed in {time.time() - start_time:.2f} seconds\n")

    start_time = time.time()
    await run(f"httpx -l {hunt_dir}/{domain}.subdomain.txt -o {hunt_dir}/{domain}.alive.txt")
    print(f"[+] HTTPX completed in {time.time() - start_time:.2f} seconds\n")

    start_time = time.time()
    await run(f"katana -u {hunt_dir}/{domain}.alive.txt -o {hunt_dir}/{domain}.endpoints.txt")
    print(f"[+] Katana completed in {time.time() - start_time:.2f} seconds\n")

    # Fetch parameters from endpoints
    input_file = f'{hunt_dir}/{domain}.endpoints.txt'
    output_file = f'{hunt_dir}/{domain}.parameters.txt'
    await fetch_parameters(input_file, output_file)


# Entry point
if __name__ == "__main__":
    asyncio.run(main())
