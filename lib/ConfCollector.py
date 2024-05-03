#  GitHub: https://github.com/ibehii
#  Telegram: https://T.me/BZHNAM
#  e-mail: Behii@tutanota.com
#  ____________________________________________

# ======== # Importing Part # ======== #

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
    for index, Link in enumerate(ConfigUrlData):
        
        # ======== # Opening the link and change it # ======== #
        Link: str = Link.replace('vmess://', '')#type: ignore
        Link: dict = json.loads(Link) #type: ignore
        Link["ps"] = "Vmess Server/T.me/BZHNAM"
        Link: str = json.dumps(Link).replace("'", '"')
        
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
    for index, Link in enumerate(ConfigUrlData):
        
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
    for index, Link in enumerate(ConfigUrlData):
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