from bs4 import BeautifulSoup as bs
from lib.static import urlPath,errorMessage,headers
import requests
from flask import request as req

def getRootData():
    newUrl = urlPath if req.args.get('page') is None else urlPath + 'page/' + req.args.get('page') + '/'
    page = requests.get(newUrl, headers=headers)
    soup = bs(page.text , 'html.parser')
    if page.status_code == 200:

        # Parsing Data
        # Initialization Container
        hot_comic = [] 
        project_comic = []
        latest_chapter = []

        # GET HOT COMIC
        for data in soup.find_all('div' , attrs={'class' : 'bs'}):
            tmp =  {
                'title' : data.find('div' , attrs={'class' : 'tt'}).get_text().strip(),
                'ch' : data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().strip().replace('Ch.' , ''),
                'rating' : data.find('div' , attrs={'class' : 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '') if data.find('a') is not None else None,
            }
            hot_comic.append(tmp)
        # GET UPDATE PROJECT
        for data in soup.find('div', attrs={'class' : 'listupd project'}).find_all('div' , attrs={'class': 'utao'}):
            chapters = []
            for cp in data.find_all('li'):
                chapters.append({
                    'title': cp.find('a').get_text().strip() if cp.find('a') is not None else None ,
                    'time_uploaded': cp.find('i').get_text().strip() if cp.find('i') is not None else None ,
                    'link' : cp.find('a').get('href').strip() if cp.find('a') is not None else None ,
                    'linkId' : cp.find('a').get('href').strip().replace('https://komikcast.com/chapter/' , '') if cp.find('a') is not None else None ,
                })

            tmp = {
                'title' : data.find('h3').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'isHot': True if data.find('span' , attrs={'class' : 'hot'}) is not None else False,
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '') if data.find('a') is not None else None,
                'chapters': chapters
            }

            project_comic.append(tmp)
        # GET LATEST COMIC
        for data in soup.find_all('div', attrs={'class' : 'listupd'})[2].find_all('div' , attrs={'class': 'utao'}):
            chapters = []
            for cp in data.find_all('li'):
                chapters.append({
                    'title': cp.find('a').get_text().strip() if cp.find('a') is not None else None ,
                    'time_uploaded': cp.find('i').get_text().strip() if cp.find('i') is not None else None ,
                    'link' : cp.find('a').get('href').strip() if cp.find('a') is not None else None ,
                    'linkId' : cp.find('a').get('href').strip().replace('https://komikcast.com/chapter/' , '') if cp.find('a') is not None else None ,
                })

            tmp = {
                'title' : data.find('h3').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'isHot': True if data.find('span' , attrs={'class' : 'hot'}) is not None else False,
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '') if data.find('a') is not None else None,
                'chapters': chapters
            }

            latest_chapter.append(tmp)
        
        return {
            'hot_comic' : hot_comic,
            'project_comic': project_comic ,
            'latest_chapter': latest_chapter
        }
        
    else:
        return errorMessage
    
def getDaftarKomik():

    newUrl = urlPath + 'daftar-komik/' if req.args.get('page') is None else urlPath + 'daftar-komik/page/' + req.args.get('page') + '/'
    pagination_page = int(req.args.get('page')) if req.args.get('page') is not None else 1
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        daftar_komik = []

        for data in soup.find_all('div' , attrs={'class' : 'bs'}):
            daftar_komik.append({
                'title' : data.find('div' , attrs={'class': 'tt'}).get_text().strip(),
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'isCompleted': True if data.find('span' , attrs={'class' : 'Completed'}) is not None else False
            })
        
        return {
            'daftar_komik' : daftar_komik,
            'page': pagination_page
        }

    else:
        return errorMessage

def getProjectList():

    newUrl = urlPath + 'project-list/' if req.args.get('page') is None else urlPath + 'project-list/page/' + req.args.get('page') + '/'
    pagination_page = int(req.args.get('page')) if req.args.get('page') is not None else 1
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        daftar_komik = []

        for data in soup.find_all('div' , attrs={'class' : 'bs'}):
            daftar_komik.append({
                'title' : data.find('div' , attrs={'class': 'tt'}).get_text().strip(),
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
            })
        
        return {
            'daftar_komik' : daftar_komik,
            'page': pagination_page
        }

    else:
        return errorMessage

def getKomikTamat():

    newUrl = urlPath + 'komik-tamat/' if req.args.get('page') is None else urlPath + 'komik-tamat/page/' + req.args.get('page') + '/'
    pagination_page = int(req.args.get('page')) if req.args.get('page') is not None else 1
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        daftar_komik = []

        for data in soup.find_all('div' , attrs={'class' : 'bs'}):
            daftar_komik.append({
                'title' : data.find('div' , attrs={'class': 'tt'}).get_text().strip(),
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'isCompleted': True if data.find('span' , attrs={'class' : 'Completed'}) is not None else False
            })
        
        return {
            'daftar_komik' : daftar_komik,
            'page': pagination_page
        }

    else:
        return errorMessage

def getJadwalUpdate():
    newUrl = urlPath + 'jadwal-update-project-harian-komikcast/'
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        container = []

        # GETTING DATA
        for data in soup.find('div' , attrs={'class' , 'text_exposed_show'}).find_all('p'):
            
            if '&nbsp;' not in data.get_text():
                container.append({
                    'time' :  str(data.get_text()).split('=')[0].replace('–' , '').strip(),
                    'project': str(data.get_text()).split('=')[-1].strip(),
                })
        
        # Remove last element, cause it's useless empty string
        container.pop()
        
        return {
            'data' : container
        }
    else:
        return errorMessage

