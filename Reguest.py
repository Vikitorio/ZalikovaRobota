import requests
import csv
validCode = [ '05', '07', 12, 14, 18, 21, 23, 26, 32, 35, 44,46, 48, 51, 53, 56, 59, 61, 63,
             65, 68, 71, 73, 74, 80, 85]
directorPostType = ['Ректор', 'В.о.ректора',  'Начальник', 'Директор']
userNum = input('Введіть код ')
if validCode.count(int(userNum)) == 0 and validCode.count(userNum) == 0:
    print("Помилка: Код не валідний спробуйте знову")
    print("Список доступних кодів: ", validCode)
    exit(0)
for i in range(len(directorPostType)):
    print('Введіть додатковий фільтр (З посадою керівника): \n', i, '-', directorPostType[i])
directorFilter = int(input())
directorFilter = str(directorPostType[directorFilter])

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + userNum + '&exp=json')
r.json()
universities: list = r.json()

filtered_data_id = [{k: row[k] for k in ['university_id', 'post_index']} for row in universities]
filtered_data_names_website = [{k: row[k] for k in ['university_name', 'university_site', 'university_director_post']}
                               for director in ['university_director_post'] for row in universities
                               if row[director] == directorFilter]

fileCsvName = 'universities'
with open(fileCsvName + "_" + userNum + '.csv', mode='w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data_id[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data_id)
with open(fileCsvName + "_" + userNum + "_website" + '.csv', mode='w', encoding='CP1251') as f_websites:
    writer = csv.DictWriter(f_websites, fieldnames=filtered_data_names_website[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data_names_website)
print('Файли готові!!!!')
input('')

