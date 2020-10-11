import requests
import time


def login(url):
    print('Trying to log in')
    postdata = {
        'cmd': 'login',
        'url': 'URL',
        'ip': '*********', # Write your ip
        'name': '*********', # Your username
        'password': '*********', # Your password
        'set': 'go'
    }
    requests.post(url, data=postdata)

# The method of judging whether the url can can connect is little silly, you can change to yours.
def is_connect(url, key='style'):
    try:
        message = requests.get(url, timeout=1).text
    except:
        return False    
    return False if message.rfind(key) == -1 else True
     
if __name__ == '__main__':
    login_url = 'http://wlt.ustc.edu.cn/cgi-bin/ip'
    test_url = 'http://www.baidu.com'
    
    for i in range(5):
        # Campus network conncetion check
        if not is_connect(login_url):
            continue
        
        # Web visit check
        if is_connect(test_url):
            print('\n','*'*10, 'Network connected', '*'*10)
            break
        else:
            login(login_url)
            time.sleep(1)

    if not is_connect(login_url):
        print('No campus network')
    elif not is_connect(test_url):
        print('Failed to login')
