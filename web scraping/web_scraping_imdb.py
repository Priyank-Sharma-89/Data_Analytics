import requests, openpyxl
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://www.imdb.com/chart/top/"

excel = Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Name','Year of Release','Rating'])

try:
    reqResponse = requests.get(url)
    reqResponse.raise_for_status()

    soup = BeautifulSoup(reqResponse.text,'html.parser')
    
    moviesList = soup.find('tbody',class_='lister-list').find_all('tr')
    
    for movie in moviesList:
        movieName = movie.find('td',class_='titleColumn').a.text

        movieYear = movie.find('td',class_='titleColumn').span.text.strip('()')

        movieRating = movie.find('td',class_='ratingColumn imdbRating').strong.text

        print(movieName,movieYear,movieRating)

        sheet.append([movieName,movieYear,movieRating])

except Exception as e:
    print(e)


excel.save('IMDB Top Movies.xlsx')