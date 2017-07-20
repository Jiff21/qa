import requests

file = requests.get(
    'http://clients2.google.com/service/update2/crx?response=redirect&x=id%3D<EXTENSION_ID_HERE>%26uc%26lang%3Den-US&prod=chrome')
