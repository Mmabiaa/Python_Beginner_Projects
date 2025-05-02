import urllib.request
import urllib.error


def URL_CHECK(url):
    print('Checking connectivity...')
    
    try:
        response = urllib.request.urlopen(url)
        print('Connected to ' + url + ' successfully')
        print(f'Response code: {response.getcode()}')
    except urllib.error.URLError as e:
        print(f'Failed to connect to {url}. Reason: {e.reason}')

def main():
    user_url = input('Enter a URL (include http:// or https://): ')
    
    # Check if the URL starts with http:// or https://
    if not user_url.startswith(('http://', 'https://')):
        print("Invalid URL. Please ensure it starts with 'http://' or 'https://'.")
        return
    
    URL_CHECK(user_url)

if __name__ == '__main__':
    main()
