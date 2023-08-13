# Movie-Recommender-System
Project Objective: To build a recommender system for movies that could give us the top 5 similar movies for an input movie name.

This project was completed using the content-based filtering approach.
It also covers the steps we did for the app webpage design & project deployment using Heroku.

### **Data Collection:**
- Data used to build this was taken from Kaggle:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv

- There are 2 datasets used here.
    - tmdb_5000_credits.csv - cast & crew information about the movie.
    - tmdb_5000_movies.csv - movie information with around 20 columns.
      
### **Data Understanding & exploration**
- Credits data consists of the below columns:
  - 'movie_id': id of the movie
  - 'title': movie title
  - 'cast': list of dictionaries ( key: element_id, value: element_values) - this stores info such as  character name, actor name, etc.
  - 'crew': list of dictionaries ( key: element_id, value: element_values) - this stores info such as director details, crew details, etc.

- Movies dataset consists of the below columns:
  - 'budget': integer type- budget of the movie
  - 'genres': list of dictionaries( key:genre_id, name:genre) - multiple genres tagged to a movie
  - 'homepage': homepage URL of the movie
  - 'id': id of the movie
  - 'Keywords': list of dictionaries( key: keyword_id, name:keyword) - multiple keywords tagged to a movie
  - 'original_language': the original language of the movie
  - 'original_title': the original title of the movie
  - 'overview': string - overview of the movie plot
  - 'popularity': popularity rating of the movie
  - 'production_companies': list of dictionaries( key: production_comp name, value: prod_comp id) - multiple prod companies involved in a movie
  - 'production_countries': list of dictionaries( key: country_id, value: country_name) - countries belonging to the prod companies
  - 'release_date': date of release of the movie
  - 'revenue': revenue collected by the movie
  - 'runtime': total runtime of the movie
  - 'spoken_languages': list of dictionaries( key:language_id, value:language_name)- languages spoken in the movie
  - 'status': movie released/rumored/post-production phase
  - 'tagline': tagline of the movie
  - 'title': movie title
  - 'vote_average': vote average of the movie
  - 'vote_count': total votes received for the movie

- Merging both the datasets based on 'movie_id'.
- Histogram of vote_average of movies:
  - ![image](https://github.com/priyaranjankar/Movie-Recommender-System/assets/106653725/da1dbed8-56d9-4b83-9899-360613bd7898)
- Histogram of the runtime of movies:
  - ![image](https://github.com/priyaranjankar/Movie-Recommender-System/assets/106653725/d375a076-dc32-4299-85ff-47abeb443b01)
  - Mean Runtime: 107.66072177926983
  - Median Runtime: 104.0
  - Mode Runtime: 90.0
  - Standard Deviation Runtime: 20.747246944946795
  - We can see, it's a near-normal distribution.
  - There are some movies in the data which have a runtime as low as 14 minutes, which suggest they might be short stories may be for children or general purpose.
    So, these movies still can remain in the data.
  - However, we found some movies to be unusual of runtime 0 mins which suggests these movies should be removed as there is no runtime of a movie, then we don't have content here to recommend.

- As we are building our recommendation system on a content-based approach, we only need to pick the variables needed for us to achieve that.
- The basic idea is to create an attribute as 'tags' for every movie which will be then projected into 
n-dimensional space which will give us the similarity between movies using various distance metrics.
- After careful observation, picked the below attributes for our model here:
  - genres
  - movie_id
  - keywords
  - title
  - overview
  - cast
  - crew

### **Data Pre-Processing**

We are in the most important part of this project now, as this step decides how well we refine our content to fuel our recommendation engine.
- The basic idea here is to get a cleaner dataframe for our recommendation systems.
- We will then check the missing or null values in the columns.
- Then, we will be merging the **genres, overview, keywords, cast & crew** details together into a single corpus.
    - Currently the info on keywords, cast & crew is in a list of dictionaries format where dictionary contains different information about a specific entity or person.
    - Hence, we will be extracting only the names of entities / persons here.
        - We will go with first 3 entities in 'cast' column
        - Also, for column 'crew' , we will go with the director name as director of the movie is important in recommending a movie to any user based on content based filtering.
- Created functions that work to fetch the above info from the cast, crew & director info from data. For more details refer to the "Movie_Recommendor_System.ipynb" notebook uploaded.
- Transformations we would need to apply now:
  - We will be merging the 4 columns into a single feature which will store tags for the respective movies.
  - However, before that, we need to apply some transformation on 4 columns too.
    - We need to merge the words found in a single element which will be stored as comma-separated tags.

### **Data Preparation**

Now that we have our desired data, our next steps would be as follows.

- text cleaning: stemming using PorterStemmer() from 'nltk' library
- remove stopwords from tags
- apply word vectorization ( using CountVectorizer Class in sci-kit learn library )

- Post the vectorization of the movies, calculating the distances between 2 vectors (movies)
  - We cannot use 'Euclidean distance' as it doesn't perform well in higher dimensions ( Curse of dimensionality )
  - Instead, we can calculate the cosine distance ( angle between the vectors in that dimensional space)
    
- Then, we can calculate similarity based on cosine distance (cosine similarity) as the distance is inversely proportional to similarity.
  - using cosine_similarity function from sklearn.metrics.pairwise

### **Recommender function**

- Creating a recommender function that will recommend 5 movies out when provided with a movie as input
    - when provided with a movie title as input, find the index position in the data.
    - using the index of the input movie, fetch the cosine similarity vector for that index position.
        - fetch the top 5 movies ( first 5 similar movies from the descending sorted cosine similarity vectors)
    - Saving data frame used for similarity scores to retrieve the index positions along with the similarity_scores as pickle files.
          - We will be using these files in order to make our webpage.

### **Data Deployment**
- Pending. Will update soon.

- Webpage using Streamlit:
    - use custom functions to get the poster & info around movies from the "tmdb" website.
    - creating a selection box that stores a dropdown menu of all the movies - for input from the user.
    - creating a recommend button that fires the top 5 similar books similar to the input.
          - get the poster for the result movies using their "poster_path" column values & using API key to get that from tmdb website.
        
