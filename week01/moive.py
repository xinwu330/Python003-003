import pandas as pd
import controller as helper

myurl = 'https://maoyan.com/films?showType=3'

urls = helper.get_top10_movie_urls_from(myurl)

print(urls)

lists = helper.get_top10_movie_detail_info_from(urls)

print(lists)

movie1 = pd.DataFrame(data = lists)

movie1.to_csv('./week01/top10_movie_infos.csv', encoding='utf_8_sig', index=False, header=False)