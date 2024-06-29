#  GitHub: https://github.com/ibehii
#  Telegram: https://T.me/BZHNAM
#  e-mail: Behii@tutanota.com
#  ____________________________________________

# ======== # Importing Part # ======== #
from sys import path as sys_path
import base64
import json
try:
    from requests import get, exceptions
except ImportError:
    exit('Please install "requests" by using "pip3 install requests"')

def VmessCollector(amount: int) -> list[str]:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vmess"
    try:
        ConfigUrlData: list = get(_API_URL).text.split('\n')
    except exceptions.ConnectionError:
        exit('Couldn\'t connect to github.com . Please check your connection.')
    except exceptions.Timeout:
        exit('Couldn\'t connect to github.com . TimeOut has reached.') 
        
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)
    
    ServersLink: list[str] = []
    
    MaxAvailableLink: int = len(ConfigUrlData)
    
    # ======== # encode the vmess link and extract its info # ======== #
    for Link in (ConfigUrlData):
        # ======== # Opening the link and change it # ======== #
        
        # ==== # Decode base64 # ==== #
        Link: str = Link.replace('vmess://', '')#type: ignore
        bytesLink: bytes = Link.encode('utf-8')
        decodedLink: str = base64.b64decode(bytesLink).decode()
        
        # ==== # Changing the description # ==== #
        Link: dict = json.loads(decodedLink) #type: ignore
        Link["ps"] = "Vmess Server/T.me/BZHNAM"
        Link: str = json.dumps(Link).replace("'", '"')
        bytesLink = Link.encode('utf-8')
        Link: str = base64.b64encode(bytesLink).decode()
        
        # ======== # after editing the link, encode it again and return it # ======== #
        ServersLink.append('vmess://' + Link ) # type: ignore

    else:
        if(MaxAvailableLink >= amount):
            return ServersLink[0:amount]
        else:
            print(f'Your demand was {amount}, but we only had {MaxAvailableLink} link')
            return ServersLink
        
def VlessCollector(amount: int) -> list[str]:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vless"
    try:
        ConfigUrlData: list = get(_API_URL).text.split('\n')
    except exceptions.ConnectionError:
        exit('Couldn\'t connect to github.com . Please check your connection.')
    except exceptions.Timeout:
        exit('Couldn\'t connect to github.com . TimeOut has reached.') 
    
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)
        
    ServersLink: list[str] = []
    
    MaxAvailableLink: int = len(ConfigUrlData)
    
    # ======== # encode the vmess link and extract its info # ======== #
    for Link in (ConfigUrlData):
        
        Link: list[str] = list(Link.partition('#'))
        Link[-1] = "vless Server/T.me/BZHNAM"
        Link: str = ''.join(Link)
                
        # ======== # after editing the link, encode it again and return it # ======== #
        ServersLink.append(''.join(Link)) # type: ignore
        
    else:
        if(MaxAvailableLink >= amount):
            return ServersLink[0:amount]
        else:
            print(f'Your demand was {amount}, but we only had {MaxAvailableLink} link')
            return ServersLink

def TrojanCollector(amount: int) -> list[str]:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/trojan"
    try:
        ConfigUrlData: list = get(_API_URL).text.split('\n')
    except exceptions.ConnectionError:
        exit('Couldn\'t connect to github.com . Please check your connection.')
    except exceptions.Timeout:
        exit('Couldn\'t connect to github.com . TimeOut has reached.') 
    
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)
        
    ServersLink: list[str] = []
    
    MaxAvailableLink: int = len(ConfigUrlData)
    
    # ======== # loop throw it and return # ======== #
    for Link in (ConfigUrlData):
        # ======== #change the link # ======== #
        Link: list[str] = list(Link.partition('#'))
        Link[-1] = "vless Server/T.me/BZHNAM"
        Link: str = ''.join(Link)

        ServersLink.append(Link) # type: ignore
        
    else:
        if(MaxAvailableLink >= amount):
            return ServersLink[0:amount]
        else:
            print(f'Your demand was {amount}, but we only had {MaxAvailableLink} link')
            return ServersLink
        
def MixedConfig() -> bool:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/mix"
    try:
        ConfigUrlData: list = get(_API_URL).text.split('\n')
    except exceptions.ConnectionError:
        exit('Couldn\'t connect to github.com . Please check your connection.')
    except exceptions.Timeout:
        exit('Couldn\'t connect to github.com . TimeOut has reached.') 
        
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)

    filePath: str = sys_path[0] + 'XrayMixedConfigs.txt'
    try:
        with open(filePath, 'w', encoding='utf-8') as confFile:
            confFile.write('\n'.join(ConfigUrlData))
    except:
        return False
    else:
        return True