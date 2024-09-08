import requests
from pyfiglet import Figlet

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[TimeZone]': response.get('timezone'),
            '[ZIP]': response.get('zip'),
            '[Latitude]': response.get('lat'),
            '[Longtude]': response.get('lon'),
            '[Map]': f'https://www.google.it/maps/place/{response.get('lat')},{response.get('lon')}'
        }
        
        for key, value in data.items():
            print(f'{key}: {value}')

    except requests.exceptions.ConnectionError:
        print('[!] Please check you connection!')

def main():
    preview_text = Figlet(font='standard')
    print(preview_text.renderText('IP Info'))

    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()