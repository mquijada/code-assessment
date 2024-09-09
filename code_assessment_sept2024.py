import schedule, time 
import pandas as pd
import matplotlib.pyplot as plt

#Setup Kaggle authentication
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

#Download the music data file from Kaggle + Create PD DataFrame 
api.dataset_download_files('thebumpkin/10400-classic-hits-10-genres-1923-to-2023', path='./data', unzip=True)
data = pd.read_csv('./data/ClassicHit.csv')

#Data Exploration 
data.head()
data.describe()
print(data.dtypes)

#Save data to csv
data.to_csv('orig_music_data.csv', index=False)
#Save original DataFrame to Github

# Top 10 most dance-worthy songs 
trackGroup = data[["Track", "Artist", "Danceability", "Year"]]
top10track = trackGroup.sort_values('Danceability', ascending = False).head(10)
print(top10track)
#Save top10track DF to Github


#What is the correlation between liveness & dancability?
compDanceLive = data[["Danceability", "Liveness"]]
compDanceLive.plot()
compDanceLive.plot.scatter(x="Danceability", y= "Liveness", alpha=0.5)
plt.show()

#Scheduled refresh every week 
schedule.every().monday.do(lambda x: api.dataset_download_files('thebumpkin/10400-classic-hits-10-genres-1923-to-2023', path='./data', unzip=True))

print("hello world")