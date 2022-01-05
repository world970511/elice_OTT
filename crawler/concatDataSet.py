import os
import pandas as pd

all_data = pd.DataFrame(columns=['img_url','title', 'year', 'kind', 'KMRB', 'genre', 'country',
                                 'cast', 'director', 'runtime(min)', 'provider'])
#파일 모음집 호출
os.chdir('../dataset/img')
file_list= os.listdir()

for i in range(len(file_list)):
    if 'csv' in file_list[i]:
        data = pd.read_table(file_list[i])
        print('파일명:',file_list[i])
        print('초반 데이터 확인 :', len(data))
        data.drop_duplicates(['title'])# 타이틀열을 기준으로 중복되는 데이터 제거
        print('중복 제거 확인 :',len(data),'\n')
        all_data = pd.concat([all_data, data], ignore_index=True, axis=0)

print('=================')
print('최종 데이터 확인 :', len(all_data))
all_data.drop_duplicates(['title'])# 타이틀열을 기준으로 중복되는 데이터 제거
print('중복 제거후 데이터 :')
all_data.info()
all_data.to_csv('../kinolight_img_data.csv',mode='w', index=False)



