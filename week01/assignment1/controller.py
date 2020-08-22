import requests
from bs4 import BeautifulSoup as soup

#获得前10个电影链接列表
def get_top10_movie_urls_from(myurl):

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent':user_agent}

    response = requests.get(myurl, headers=header)

    soup_info = soup(response.text, 'html.parser')

    #获取前10个电影链接
    urls = []
    for tags in soup_info.find_all('div', attrs={'class':'movie-item film-channel'},limit=10):
        for atag in tags.find_all('a',):
            urls.append(f'https://maoyan.com' + atag.get('href'))
    return urls

#获得前10个电影详细信息
def get_top10_movie_detail_info_from(urls):

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent':user_agent}

    top10_moive_infos = []
    
    for url in urls:
        response = requests.get(url, headers=header)

        soup_info = soup(response.text, 'html.parser')

        #获取电影名称
        movie_name = soup_info.find('h1', attrs={'class':'name'}).text

        #获取电影类型
        movie_type_list = soup_info.find_all('a', attrs={'class':'text-link'})
        movie_types = ''
        for type in movie_type_list:
            movie_types += type.text.strip() + ' '

        #获取电影上映时间
        movie_release_date = soup_info.find_all('li', attrs={'class':'ellipsis'})[-1].text
        
        info_list= [movie_name, movie_types, movie_release_date]
        top10_moive_infos.append(info_list)
    return top10_moive_infos