from bs4 import BeautifulSoup
import requests
import argparse
import wget
from colorama import Fore, Back, Style

argparser = argparse.ArgumentParser()
argparser.add_argument("--download", action='store_true', help="Descargar archivos JS.")
argrequired = argparser.add_argument_group("requireds arguments")
argrequired.add_argument("--url", "-u", help="Especificar URL.", required=True)
args = argparser.parse_args()
url = args.url
download = args.download

def logo():
    logo = Fore.LIGHTRED_EX +"""
     _ ____    _____ ___ _   _ ____  _____ ____  
    | / ___|  |  ___|_ _| \ | |  _ \| ____|  _ \ 
 _  | \___ \  | |_   | ||  \| | | | |  _| | |_) |
| |_| |___) | |  _|  | || |\  | |_| | |___|  _ < 
 \___/|____/  |_|   |___|_| \_|____/|_____|_| \_\.""" + Fore.WHITE + Back.RED + "Cyber Phantom" + Fore.RESET + Back.RESET
                                                 

    return logo
def main(url):
        try:
            print(logo())
            web_page = requests.get(url)
            soup = BeautifulSoup(web_page.content, "html.parser")
            script_js = soup.find_all("script")

            for js in script_js:
                if js.get('src') == None:
                    print(Back.YELLOW + Fore.WHITE + "\nCodigo incluido - No externo:" + Back.RESET + Fore.RESET)
                    print(Back.BLACK+ Fore.WHITE + f"{js.prettify()}" + Back.RESET + Fore.RESET)
                else:
                    if js.get('src').startswith("http://") or js.get('src').startswith("https://"):
                        url_js = f"{js.get('src')}"
                    if js.get('src').endswith("/"):
                        url_js =f"servidor.objetivo.com{js.get('src')}\n" 
                    else:
                        url_js = f"servidor.objetivo.com/{js.get('src')}\n" 
                    print(Back.GREEN + Fore.WHITE + f"\nCodigo externo [{js.get('src')}]:" + Back.RESET + Fore.RESET)
                    print(Back.BLACK+ Fore.WHITE + f"{url_js}" + Back.RESET + Fore.RESET)
                    if download == True:
                        url_download = f"{url}"+js.get("src")
                        wget.download(url_download, "")
        except requests.exceptions.ConnectionError:
            print(Back.RED + Fore.WHITE + "Servicio desconocido" + Back.RESET + Fore.RESET)

                

if __name__ == "__main__":
    main(url)