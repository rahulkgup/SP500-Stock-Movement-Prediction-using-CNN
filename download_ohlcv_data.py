import urllib.request
import csv
import time

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
username = '65a3c11ec7fd8d4f89ae253ba9bf2571'
password = '434b2fe1b7de73a43dc74e7439b19519'



#https://api.intrinio.com/historical_data.csv?identifier=AAPL&item=marketcap
#https://api.intrinio.com/historical_data.csv?identifier=AAPL&item=volume
#https://api.intrinio.com/historical_data.csv?identifier=AAPL&item=netincome
#https://api.intrinio.com/historical_data.csv?identifier=AAPL&item=beta

def start_intrinio(username, password):
    def intrinio(url, file):

        # If we knew the realm, we could use it instead of None.
        top_level_url = "https://api.intrinio.com"
        
        #password_mgr.add_password(None, top_level_url, username, password)
        
        #handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        
        # create "opener" (OpenerDirector instance)
        #opener = urllib.request.build_opener(handler)
        
        #hdr = {'User-Agent':'Responsivity-Check Bot/1.0'}
        #request = urllib.request(top_level_url, headers=hdr)

        #Now all calls to urllib.request.urlretrieve
        urllib.request.urlretrieve(top_level_url + url, file)

        return
    return intrinio

url = None
file = None

reader = csv.reader(open('US_Large_Cap.csv'), delimiter=',')
for row in reader:
    ticker =  row[0]  
    ticker = ticker.encode('ascii', 'ignore').decode('ascii') 
    url = '/prices.csv?ticker=' + ticker
    
    #file = ''.join(e for e in url if e.isalnum()) + '.csv'
    file = ticker + '.csv'
    print(url, file)       
    intrinio = start_intrinio(username, password)
    intrinio(url, file)
    time.sleep(3) 
    
