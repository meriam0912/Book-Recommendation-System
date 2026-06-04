# 📚 Book Recommendation System

A machine learning project that recommends similar books using **item-based collaborative filtering**.

## Overview

This system analyzes user ratings and finds books with similar rating patterns.  
If users rated two books in a similar way, the model considers them similar.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Streamlit
- Pickle

## How It Works

1. Load books, users, and ratings datasets
2. Clean and filter the data
3. Create a book-user pivot table
4. Convert it into a sparse matrix
5. Use `NearestNeighbors` to find similar books
6. Save the model and data using pickle

## Project Structure

```text
Book Recommendations/
├── artifacts/
├── dataset/
├── src/
├── app.py
├── setup.py
├── README.md
└── requirements.txt