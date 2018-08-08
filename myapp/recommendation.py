import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ds = pd.read_csv("myapp/finalDataset.csv")#you can plug in your own list of products or movies or books here as csv file

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
######ngram (1,3) can be explained as follows#####
#ngram(1,3) encompasses uni gram, bi gram and tri gram
#consider the sentence "The ball fell"
#ngram (1,3) would be the, ball, fell, the ball, ball fell, the ball fell

tfidf_matrix = tf.fit_transform(ds['description'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

results = {}# dictionary created to store the result in a dictionary format (ID : (Score,item_id))

for idx, row in ds.iterrows():
    # the below code 'similar_indice' stores similar ids based on cosine similarity. sorts them in ascending order. [:-5:-1] is then used so that the indices with most similarity are got. 0 means no similarity and 1 means perfect similarity
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

    # First item is the item itself, so remove it.
    # Each dictionary entry is like: [(1,2), (3,4)], with each tuple being (score, item_id)
    results[row['id']] = similar_items[1:]

#below code 'function item(id)' returns a row matching the id along with description. Initially it is a dataframe, then we convert it to a list
def item(id):
    return ds.loc[ds['id'] == id]['description'].tolist()[0].split(' - ')[0]

# Just reads the results out of the dictionary. No real logic here.
def recommend(item_id, num):
    print("Recommending " + str(num) + " products similar to " +str(item_id)  + "...")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:

        print("Recommended: " + str(rec[1]) +item(rec[1]) + " (score:" + str(rec[0]) + ")")
    return recs

# Just plug in any item id here (1-500), and the number of recommendations you want (1-99)
# You can get a list of valid item IDs by evaluating the variable 'ds', or a few are listed below

#the first argument in the below function to be passed is the id of the book, second argument is the number of books you want to be recommended