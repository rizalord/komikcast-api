from bs4 import BeautifulSoup as bs
from lib.static import urlPath,errorMessage,headers
import requests


def getRootData():
    page = requests.get(urlPath, headers=headers)
    soup = bs(page.text , 'html.parser')
    if page.status_code == 200:
        # Parsing Data
        # GET HOT COMIC
        hot_comic = [] 
        project_comic = []
        for data in soup.find_all('div' , attrs={'class' : 'bs'}):
            tmp =  {
                'title' : data.find('div' , attrs={'class' : 'tt'}).get_text().strip(),
                'ch' : data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().strip().replace('Ch.' , ''),
                'rating' : data.find('div' , attrs={'class' : 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip()
            }
            hot_comic.append(tmp)
        # GET UPDATE PROJECT
        for data in soup.find('div', attrs={'class' : 'project'}).find_all('div' , attrs={'class': 'utao'}):
            tmp = {
                'title' : data.find('h3').get_text().strip(),
                'image': data.find('img').get('src').strip()
            }

            project_comic.append(tmp)

        
        return {
            # 'hot_comic' : hot_comic,
            'project_comic': project_comic
        }
        
    else:
        return errorMessage
    
