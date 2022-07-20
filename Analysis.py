import pandas as pd
from matplotlib import pyplot as plt

# Handeling of the databases
movies=pd.read_csv('movies.csv',low_memory=False)
links=pd.read_csv('links_small.csv')
ratings=pd.read_csv('ratings_small.csv')
oscars = pd.read_csv('oscars.csv')
movies['popularity'] = pd.to_numeric(movies['popularity'], errors='coerce')
movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')
movies['id'] = pd.to_numeric(movies['id'], errors='coerce')
links = links.merge(ratings)
links=links.rename(columns={'imdbId': 'id'})
movies = pd.merge(movies,links)

# Connection between the rating of a movies and it's chances to win an oscar
ratingsVsNomi = oscars.groupby('rate')['Oscar_nominated'].mean().reset_index()
plt.plot(ratingsVsNomi.rate,ratingsVsNomi.Oscar_nominated, color = 'Orange')
plt.xlabel("Rate of Movie")
plt.ylabel("Oscar Nominations")
plt.title("Connection Between The Rating of a Movie & It's Oscar Nominations")
plt.show()

# The movie genre that got nominated the most times
oscars['genre'] = oscars.genre.apply(lambda x: x.split('|')[0])
genreVsNomi = oscars.groupby('genre')['Oscar_nominated'].mean().reset_index()
x = genreVsNomi['genre']
y = list(genreVsNomi['Oscar_nominated'])
plt.bar(x,y,color = 'PaleTurquoise')
plt.xlabel('Genres of Movies')
plt.ylabel('Oscar Nomination')
plt.title("Which Genres Get Nominated The Most Times?")
plt.show()

# Connection between the movie duration and it's nominations
bins = ["short","short-medium","medium","medium-long","long"]
oscars = oscars.sort_values(by = 'duration')
TimeVsNomi = oscars.groupby(pd.cut(oscars['duration'],len(bins),labels = bins))['Oscar_nominated'].mean()
TimeVsNomi.plot(kind='bar',color = 'PaleGreen')
plt.xlabel("Movie Duration")
plt.ylabel("Oscar Nominations")
plt.title("Connection Between a Movie Duration & it's Oscar Nominations")
plt.show()

# Connection between popularity of a movie and it's nominations
bins = [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]
oscars = oscars.sort_values(by = 'popularity')
TimeVsNomi = oscars.groupby(pd.cut(oscars['popularity'],len(bins)))['Oscar_nominated'].mean()
TimeVsNomi.plot(kind='line',color = 'DeepSkyBlue')
axs = plt.subplot()
axs.set_xticks(range(len(bins)))
axs.set_xticklabels(bins)
plt.xlabel("Popularity")
plt.ylabel("Oscar Nominations")
plt.title("Connection Between Popularity of a Movie & it's Oscar Nominations")
plt.show()

# Connection between the Budget of a Movie & it's ratings
bins = [50000000, 100000000, 150000000, 200000000, 250000000]
movies = movies.sort_values(by = 'budget')
BudgetVsNomi = movies.groupby(pd.cut(movies['budget'],len(bins)))['rating'].mean()
BudgetVsNomi.plot(kind='line',color = 'Violet')
axs = plt.subplot()
axs.set_xticks(range(len(bins)))
axs.set_xticklabels(bins)
plt.xlabel("Budget of Movie ($)")
plt.ylabel("Rating")
plt.title("Connection Between of a Movie's Budget & it's Rating")
plt.show()

# Connection between a movie's gross & it's nominations
bins = [0, 200000000, 400000000, 600000000, 800000000, 1000000000]
oscars = oscars.sort_values(by = 'gross')
GrossVsNomi = oscars.groupby(pd.cut(oscars['gross'],len(bins)))['Oscar_nominated'].mean()
GrossVsNomi.plot(kind='line',color = 'Coral')
axs = plt.subplot()
axs.set_xticks(range(len(bins)))
axs.set_xticklabels(bins)
plt.xlabel("Movie's Revenue")
plt.ylabel("Oscar Nominations")
plt.title("Connection Between a Movie's Gross & it's Nominations")
plt.show()

# Connection between a movie's gross & it's Rating
bins = [200000000, 400000000, 600000000, 800000000, 1000000000]
oscars = oscars.sort_values(by = 'gross')
GrossVsNomi = oscars.groupby(pd.cut(oscars['gross'],len(bins)))['rate'].mean()
GrossVsNomi.plot(kind='bar',color = 'Chartreuse')
axs = plt.subplot()
axs.set_xticks(range(len(bins)))
axs.set_xticklabels(bins)
axs.set_ylim((0,10))
plt.xlabel("Movie's Revenue ($)")
plt.ylabel("Movie Rating")
plt.title("Connection Between a Movie's Gross & it's Rating")
plt.show()

# Which age (adult/not) gets the movie higher ratings
AgeRating = movies.groupby('adult')['rating'].mean().reset_index()
x = ['Young','Adult']
y= list(AgeRating['rating'])
plt.bar(x,y,color='PaleTurquoise')
plt.xlabel('Age of Viewers')
plt.ylabel('Movie Rating')
plt.title("Which Type of Movies, for Young or for Adult, Has a Higher Rating?")
plt.show()

# Oscar Nominations of Movies Genres Throughout the Years
colors = ['DeepSkyBlue','PeachPuff','HotPink','PaleGreen','Tomato','SpringGreen','PaleTurquoise','Violet','Yellow','RoyalBlue','Crimson','Aquamarine','MediumOrchid','GreenYellow','OrangeRed','Gold','DodgerBlue']
genres = oscars.genre.unique()
for i in range(len(genres)):
    z = oscars[oscars.genre==genres[i]]
    GenresVsNomi = z.groupby('year')['Oscar_nominated'].mean().reset_index().sort_values(by='year')
    plt.plot(GenresVsNomi['year'],GenresVsNomi['Oscar_nominated'],color=colors[i])
plt.legend(genres,bbox_to_anchor=(1.01,1))
plt.xlabel('Year of Release')
plt.ylabel('Oscar Nominations')
plt.title("Oscar Nominations of Movies Genres Throughout the Years")
plt.show()

## Task That Was Given in Mid Presentation of The Project
# Conection Between a Movie's Duration & it's Rating
bins = ["short","short-medium","medium","medium-long","long"]
oscars = oscars.sort_values(by = 'duration')
TimeVsNomi = oscars.groupby(pd.cut(oscars['duration'],len(bins),labels = bins))['rate'].mean()
TimeVsNomi.plot(kind='bar',color = 'LightBlue')
plt.xlabel("Movie Duration")
plt.ylabel("Movie Rating")
plt.title("Connection Between a Movie Duration & it's Rating")
plt.show()
