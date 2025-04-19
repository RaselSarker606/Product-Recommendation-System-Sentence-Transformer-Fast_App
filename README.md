# 🚀 Product Recommendation System with Sentence-BERT & Flask

## 📖 Overview

This system recommends laptops, mobiles, watches, and earbuds based on user queries using Sentence-BERT embeddings. Whether users search by product name or specification—like “8GB RAM”, “50MP camera”, or “5000mAh battery”—the system understands the intent and returns the most relevant results with images and key details via a simple Flask web interface.

---

## 📂 Features

- 🧠 **Semantic Search**: Understands user intent using `all-MiniLM-L6-v2` from Sentence-BERT.
- 🎯 **Cosine Similarity Ranking**: Retrieves and ranks products by similarity to the query.
- 🖼️ **Product Image Display**: Shows product images along with title, brand, and category.
- 🌐 **Flask Web App**: Simple interface for interactive recommendations.
- ⚡ **Fast Results**: Real-time product search based on vector similarity.

---

## 🛠️ Technologies Used

- **Python 3.11.9**
- **Flask** – Lightweight web framework
- **Pandas** – For data processing
- **Scikit-learn** – For cosine similarity
- **Sentence-Transformers** – For generating text embeddings
- **HTML + Jinja2** – Frontend templating

---

## 🚀 Installation & Setup

### 📦 Prerequisites

- Python 3.7+
- Precomputed `product_embeddings.pkl` file with the following columns:
  - `title`
  - `brand`
  - `category`
  - `imgs` (a list of image URLs)
  - `embeddings` (precomputed Sentence-BERT vectors)

### 🔧 Installation

```bash
git clone https://github.com/your-username/product-recommender-flask.git
cd product-recommender-flask
pip install flask pandas scikit-learn sentence-transformers
```

Make sure to place your `product_embeddings.pkl` file in the root directory of the project.

---

## ▶️ Running the App

```bash
python app.py
```

Open your browser and go to:  
`http://127.0.0.1:5000/`

---

## 💬 Example Use Cases

- *“Suggest me a budget smartphone”*  
- *“Show me men's running shoes”*  
- *“Need protein-rich snacks”*  

The app will return the most relevant products with images and details.

---

## 📌 Future Enhancements

- 📦 **Filter by Brand, Price, or Rating**
- 🌍 **Multilingual Query Support**
- 🧠 **Fine-tuned Embedding Models for Product Domains**
- 📈 **Logging & Analytics for User Search Behavior**

---

🚀 **Smarter product discovery with semantic search.**
