import pandas as pd
import controller as helper

myurl = 'https://maoyan.com/films'

urls = helper.get_top10_movie_urls_from(myurl)

lists = helper.get_top10_movie_detail_info_from(urls)

top_10_moive_infos = pd.DataFrame(data=lists)

top_10_moive_infos.to_csv('./top10_movie_infos_01.csv', encoding='utf_8_sig', index=False, header=False)