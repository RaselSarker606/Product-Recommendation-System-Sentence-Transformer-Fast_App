#using python 3.11.9
from flask import Flask, request, render_template
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load a pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')
# Load the embeddings and product data
df = pd.read_pickle('product_embeddings.pkl')


df['imgs'] = df['imgs'].apply(lambda x: eval(x) if isinstance(x, str) else x)

app = Flask(__name__)

# Function to get recommendations
def recommend_products(query, top_k=20):
    query = query.lower()
    query_embedding = model.encode(query)
    df['similarity'] = df['embeddings'].apply(lambda x: cosine_similarity([query_embedding], [x]).flatten()[0])
    recommendations = df.sort_values(by='similarity', ascending=False).head(top_k)
    return recommendations[['title', 'brand', 'category', 'similarity', 'imgs']]

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        query = request.form['query']
        recommendations = recommend_products(query).to_dict(orient='records')
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)