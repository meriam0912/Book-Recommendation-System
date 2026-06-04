import pickle
import streamlit as st
import numpy as np

st.header("Book Recommendation System")
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_names = pickle.load(open('artifacts/books_name_list.pkl', 'rb'))
final_set = pickle.load(open('artifacts/final_set.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/Book_Pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    poster_url = []
    #We loop through the recommended book positions
    for book_id in suggestion[0]:
        #get the real book title from the position
        book_title = book_pivot.index[book_id]

        #We want to find that book inside final_set
        ids = np.where(final_set['Title'] == book_title)[0][0]

        #get the cover image link
        url = final_set.iloc[ids]['Cover_Image']

        poster_url.append(url)
    return poster_url


def recommend_the_books(book_title):
    book_list = []
    book_id = np.where(book_pivot.index == book_title)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)


    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books :
            book_list.append(j)
    return book_list, poster_url


selected_book = st.selectbox("Type or select a book",books_names)

if st.button('Show Recommendations'):
    recommendation_books,poster_url = recommend_the_books(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])

    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])

    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])