#  GitHub: https://github.com/ibehii
#  Telegram: https://T.me/BZHNAM
#  e-mail: Behii@tutanota.com
#  ____________________________________________

# ======== # Importing part # ======== #
try:
    from colorama import Fore
    from Rcolor import standard_rainbow_fg
    from pyperclip import copy
    from sys import path as sys_path
    from urllib.request import urlretrieve
    from urllib.error import URLError
    from sys import path as sys_path
    from os import name, path, system
    from shutil import move
    sys_path.append(path.join(sys_path[0], 'lib'))
    from lib import ConfCollector
    import pyfiglet

except ImportError:
    exit('Please install the requirement by "pip3 install -r requirement.txt"')

# ======== # Download required font for figlet # ======== #
pyfiglet_path: str = pyfiglet.__file__.replace('__init__.py', 'fonts')
CurrentFolder: str = sys_path[0]
   
if (not path.exists(path.join(pyfiglet_path, 'ANSI Shadow.flf'))):
        try:
            move(path.join(CurrentFolder, 'ANSI Shadow.flf'), path.join(pyfiglet_path, 'ANSI Shadow.flf'))
        except FileNotFoundError:
            print(Fore.RED + path.join(CurrentFolder, 'ANSI Shadow.flf') + ' Was Not Found!\n' + Fore.RESET)
            print(Fore.YELLOW + 'Downloading the required font!' + Fore.RESET)
            try:
                urlretrieve(
                "https://github.com/xero/figlet-fonts/raw/master/ANSI%20Shadow.flf", 'ANSI Shadow.flf')
                move('ANSI Shadow.flf', path.join(pyfiglet_path + 'ANSI Shadow.flf'))
            except URLError:
                exit(Fore.RED + "Couldn't connect to server.\nCheck your internet connection and try again" + Fore.RESET)


def _clear_screen() -> None:
    if (name == 'nt'):
        system('cls')
    else:
        system('clear')

# ======== # Main Menu # ======== #    
print(standard_rainbow_fg(pyfiglet.figlet_format('Config', font='ANSI Shadow')))
print(Fore.YELLOW +  '''[1] - Get Vmess configs
[2] - Get Vless configs
[3] - Get Trojan configs
[4] - Get some random configs\n''' + Fore.RESET)

UserChoice: int = int(input(Fore.GREEN + 'Pick a number -> ' + Fore.RESET))

match UserChoice:

    # ======== # Vmess # ======== #
    case 1: 
        _clear_screen()
        print(standard_rainbow_fg(pyfiglet.figlet_format('Vmess', font='ANSI Shadow')), end='\n\n')
        AmountConfig: int = int(input(Fore.YELLOW + 'How many config do you need? max(40) -> ' + Fore.RESET))
        
        if (AmountConfig > 40):
            exit(Fore.RED + "The maximum capability is 40 config per requests" + Fore.RESET)
        
        VmessConfig: str = '\n'.join(ConfCollector.VmessCollector(AmountConfig))
        copy(VmessConfig)
        print('The configs were copied to your clipboard.')

    # ======== # vless # ======== #
    case 2: 
        _clear_screen()
        print(standard_rainbow_fg(pyfiglet.figlet_format('Vless', font='ANSI Shadow')), end='\n\n')
        AmountConfig: int = int(input(Fore.YELLOW + 'How many config do you need? max(40) -> ' + Fore.RESET))
        
        if (AmountConfig > 40):
            exit(Fore.RED + "The maximum capability is 40 config per requests" + Fore.RESET)
        
        VlessConfig: str = '\n'.join(ConfCollector.VlessCollector(AmountConfig))
        copy(VlessConfig)
        print('The configs were copied to your clipboard.')

    # ======== # trojan # ======== #
    case 3: 
        _clear_screen()
        print(standard_rainbow_fg(pyfiglet.figlet_format('Trojan', font='ANSI Shadow')), end='\n\n')
        AmountConfig: int = int(input(Fore.YELLOW + 'How many config do you need? max(15) -> ' + Fore.RESET))
        
        if (AmountConfig > 15):
            exit(Fore.RED + "The maximum capability is 15 config per requests" + Fore.RESET)
        
        TrojanConfig: str = '\n'.join(ConfCollector.TrojanCollector(AmountConfig))
        copy(TrojanConfig)
        print('The configs were copied to your clipboard.')
        
    case 4:
        _clear_screen()
        print(standard_rainbow_fg(pyfiglet.figlet_format('Mixed', font='ANSI Shadow')), end='\n\n')

        if ConfCollector.MixedConfig():
            print(f'Links saved on {path.join(sys_path[0], 'XrayMixedConfigs.txt')} file')