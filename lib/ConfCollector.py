#  GitHub: https://github.com/ibehii
#  Telegram: https://T.me/BZHNAM
#  e-mail: Behii@tutanota.com
#  ____________________________________________

# ======== # Importing Part # ======== #

import json
try:
    from requests import get
except ImportError:
    exit('Please install "requests" by using "pip3 install requests"')

def VmessCollector(amount: int) -> list[str]:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vmess"
    ConfigUrlData: list = get(_API_URL).text.split('\n')
    
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)
    
    ServersLink: list[str] = []
    
    MaxAvailableLink: int = len(ConfigUrlData)
    
    # ======== # encode the vmess link and extract its info # ======== #
    for index, Link in enumerate(ConfigUrlData):
        
        # ======== # Opening the link and change it # ======== #
        Link: str = Link.replace('vmess://', '')#type: ignore
        Link: dict = json.loads(Link) #type: ignore
        Link["ps"] = "Vmess Server/T.me/BZHNAM"
        Link: str = json.dumps(Link).replace("'", '"')
        
        # ======== # after editing the link, encode it again and return it # ======== #
        ServersLink.append('vmess://' + Link ) # type: ignore

        if(index == amount):
            return ServersLink
        elif(index == MaxAvailableLink):
            print(f'Your demand was {amount}, but we only had {MaxAvailableLink} link')
            return ServersLink
        
def VlessCollector(amount) -> list[str]:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vless"
    ConfigUrlData: list = get(_API_URL).text.split('\n')
    
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)
        
    ServersLink: list[str] = []
    
    MaxAvailableLink: int = len(ConfigUrlData)
    
    # ======== # encode the vmess link and extract its info # ======== #
    for index, Link in enumerate(ConfigUrlData):
        
        Link: list[str] = list(Link.partition('#'))
        Link[-1] = "vless Server/T.me/BZHNAM"
                
        # ======== # after editing the link, encode it again and return it # ======== #
        ServersLink.append(''.join(Link)) # type: ignore
        
        if(index == amount):
            return ServersLink
        elif(index == MaxAvailableLink):
            print(f'Your demand was {amount}, but we only had {MaxAvailableLink} link')
            return ServersLink

def TrojanCollector(amount) -> list[str]:
    _API_URL: str = "https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/trojan"
    ConfigUrlData: list = get(_API_URL).text.split('\n')
    
    # ======== # Deleting first 6 line that are not config # ======== #
    for _ in range(6):
        ConfigUrlData.pop(0)
        
    ServersLink: list[str] = []
    
    MaxAvailableLink: int = len(ConfigUrlData)
    
    # ======== # loop throw it and return # ======== #
    for index, Link in enumerate(ConfigUrlData):
        
        # ======== # Opening the link and change it # ======== #
        Link: str = Link.replace('trojan://', '')#type: ignore
        Link: dict = json.loads(Link) #type: ignore
        Link["ps"] = "Trojan Server/T.me/BZHNAM"
        Link: str = json.dumps(Link).replace("'", '"')
        
        ServersLink.append('trojan://' + Link) # type: ignore
    
        if(index == amount):
            return ServersLink
        elif(index == MaxAvailableLink):
            print(f'Your demand was {amount}, but we only had {MaxAvailableLink} link')
            return ServersLink