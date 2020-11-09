import argparse
import requests
from bs4 import BeautifulSoup
import urllib.request

# argparse settings
parser = argparse.ArgumentParser(description='Lineage OS Downloader')
parser.add_argument('codename', action="store", help="Codename of your device")
args = parser.parse_args()
# Get link
downloadlink = "http://download.lineageos.org/" + args.codename
# Download html
r = requests.get(downloadlink)
# Get download link
soup = BeautifulSoup(r.text, 'lxml')
link = soup.find('div', class_= 'scrollable-table').find_all("a")[0]
link = link.get("href")
# Download file
print('Beginning file download... ')
filename = "lineageos_" + args.codename + ".zip"
urllib.request.urlretrieve(link, filename)
print('File successfully downloaded and saved to', filename)
