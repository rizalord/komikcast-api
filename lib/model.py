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
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().replace('Ch.' , '').strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'isCompleted': True if data.find('span' , attrs={'class' : 'Completed'}) is not None else False,
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '')[:-1] if data.find('a') is not None else None,
                'linkChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href') if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
                'linkIdChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href').replace('https://komikcast.com/chapter/' , '')[:-1] if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
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
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().replace('Ch.' , '').strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'isCompleted': True if data.find('span' , attrs={'class' : 'Completed'}) is not None else False,
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '')[:-1] if data.find('a') is not None else None,
                'linkChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href') if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
                'linkIdChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href').replace('https://komikcast.com/chapter/' , '')[:-1] if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
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
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().replace('Ch.' , '').strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': data.find('img').get('src').strip(),
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '')[:-1] if data.find('a') is not None else None,
                'linkChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href') if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
                'linkIdChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href').replace('https://komikcast.com/chapter/' , '')[:-1] if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
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

def getDataKomik():
    idKomik = req.args.get('id')
    newUrl = urlPath + 'komik/' + idKomik
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        container = {}

        # GETTING DATA
        genres = []
        list_chapter = []

        for data in soup.find('div' , {'class' : 'spe'}).find('span').find_all('a'):
            genres.append(data.get_text().strip())
        for data in soup.find('div' , {'class' : 'cl'}).find_all('li'):
            list_chapter.append({
                'chapter': data.find('span' , {'class' : 'leftoff'}).find('a').get_text().replace('Chapter' , '').strip(),
                'time_release': data.find('span' , {'class' : 'rightoff'}).get_text().strip(),
                'link': data.find('span' , {'class' : 'leftoff'}).find('a').get('href').strip(),
                'linkId': data.find('span' , {'class' : 'leftoff'}).find('a').get('href').replace('https://komikcast.com/chapter/' , '').strip(),
            })

        container = {
            'image': soup.find('div' , {'class' : 'thumb'}).find('img').get('src'),
            'title': soup.find('h1' , {'itemprop' : 'headline'}).get_text().strip(),
            'title_other': soup.find('span' , {'class' : 'alter'}).get_text().strip(),
            'rating': soup.find('div' , {'class' : 'rating'}).find('strong').get_text().replace('Rating' , '').strip(),
            'sinopsis': soup.find('div' , {'itemprop' : 'articleBody'}).find('p').get_text().strip(),
            'genres' : genres,
            'type': soup.find('div' , {'class': 'spe'}).find_all('span')[4].find('a').get_text().strip(),
            'updated_on': soup.find('div' , {'class': 'spe'}).find_all('span')[6].find('time').get_text().strip(),
            'status': soup.find('div', {'class': 'spe'}).find_all('span')[1].get_text().replace('Status:','').strip(),
            'released': soup.find('div', {'class': 'spe'}).find_all('span')[2].get_text().replace('Released:','').strip(),
            'author': soup.find('div', {'class': 'spe'}).find_all('span')[3].get_text().replace('Author:','').strip(),
            'total_chapter': soup.find('div', {'class': 'spe'}).find_all('span')[5].get_text().replace('Total Chapter:','').strip(),
            'list_chapter': list_chapter
        } 
        
        return {
            'data' : container
        }
    else:
        return errorMessage


def getChapterComic():
    idKomik = req.args.get('id')
    newUrl = urlPath + 'chapter/' + idKomik
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        select_chapter = []
        images = []

        for data in soup.find('select').find_all('option'):
            if data.get_text() != 'Select Chapter Manga':
                select_chapter.append({
                    'text': data.get_text().strip(),
                    'link': data.get('value').strip(),
                    'linkId': data.get('value').replace('https://komikcast.com/chapter/' , '').strip(),
                })
        
        for data in soup.find('div' , {'id' : 'readerarea'}).find_all('img'):
            if data.get('src').strip() != '':
                images.append({
                    'link': data.get('src').strip(),
                    'width': data.get('width').strip() if data.get('width') is not None else None,
                    'height': data.get('height').strip() if data.get('height') is not None else None,
                })

        container = {
            'title': soup.find('h1' , {'itemprop' : 'name'}).get_text().strip(),
            'chapter': soup.find('h1' , {'itemprop' : 'name'}).get_text().split('Chapter')[1].replace('Bahasa Indonesia' , '').strip(),
            'comic_title': soup.find('div' , {'class': 'allc'}).find('a').get_text().strip(),
            'comic_link': soup.find('div' , {'class': 'allc'}).find('a').get('href').strip(),
            'comic_link_id': soup.find('div' , {'class': 'allc'}).find('a').get('href').replace('https://komikcast.com/komik/' , '').strip(),
            'select_chapter': select_chapter,
            'prev_link': soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'prev'}).get('href').strip() if soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'prev'}) is not None else None,
            'prev_link_id': soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'prev'}).get('href').replace('https://komikcast.com/chapter/' , '').strip() if soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'prev'}) is not None else None,
            'next_link': soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'next'}).get('href').strip() if soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'next'}) is not None else None,
            'next_link_id': soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'next'}).get('href').replace('https://komikcast.com/chapter/' , '').strip() if soup.find('div' , {'class': 'nextprev'}).find('a' , {'rel' : 'next'}) is not None else None,
            'images': images
        }
        
        return {
            'data' : container
        }
    else:
        return errorMessage

def getSpecificComic():
    keyword = req.args.get('keyword')
    newUrl = urlPath + '?s=' + keyword if req.args.get('page') is None else urlPath + 'page/' + req.args.get('page') + '/?s=' + keyword
    pagination_page = int(req.args.get('page')) if req.args.get('page') is not None else 1
    page = requests.get(newUrl , headers=headers)
    soup = bs(page.text , 'html.parser')

    if page.status_code == 200:
        # Parsing Data
        # Initialization Container

        daftar_komik = []

        for data in soup.find_all('div' , attrs={'class' : 'bs'}):
            image = None
            try:
                image = data.find('img') .get('src').strip()
            except:
                pass

            daftar_komik.append({
                'title' : data.find('div' , attrs={'class': 'tt'}).get_text().strip(),
                'chapter': data.find('div' , attrs={'class' : 'epxs'}).find('a').get_text().replace('Ch.' , '').strip(),
                'rating' : data.find('div' , attrs={'class': 'rating'}).find('i').get_text().strip(),
                'image': image,
                'type': data.find('span' , attrs={'class' : 'type'}).get_text().strip(),
                'isCompleted': True if data.find('span' , attrs={'class' : 'Completed'}) is not None else False,
                'link': data.find('a').get('href') if data.find('a') is not None else None,
                'linkId': data.find('a').get('href').replace('https://komikcast.com/komik/' , '')[:-1] if data.find('a') is not None else None,
                'linkChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href') if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
                'linkIdChapter': data.find('div' , attrs={'class' : 'bigor'}).find('a').get('href').replace('https://komikcast.com/chapter/' , '')[:-1] if data.find('div' , attrs={'class' : 'bigor'}).find('a') is not None else None,
            })
        
        return {
            'results' : daftar_komik,
            'page': pagination_page
        }

    else:
        return errorMessage
