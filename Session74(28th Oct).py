import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

st.set_page_config(page_title="Text Preprocessing Tool 🌸", page_icon="🌸", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #fffafc;
    font-family: 'Poppins', sans-serif;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 0.6rem 2rem;
    font-size: 1.1rem;
    font-weight: 500;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    white-space: nowrap;  /* 👈 added this line */
}
div.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0px 6px 12px rgba(0,0,0,0.15);
}

/* Badge */
.badge {
    display: inline-block;
    margin-top: 20px;
    margin-bottom: 10px;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    background: linear-gradient(to right, #f9d1f7, #d7e1fa);
    color: #333;
    font-weight: 500;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
}

/* Output Box */
.output-box {
    background: #f8f5ff;  /* soft lilac */
    border-radius: 15px;
    padding: 1.5rem;
    color: #2d2d2d;  /* visible dark text */
    font-size: 1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    word-wrap: break-word;
    border: 1px solid #e4d8ff;
}
</style>
""", unsafe_allow_html=True)


st.title("🌸 Text Preprocessing Playground")

# Input
text_input = st.text_area("Paste your text here 👇", height=180, placeholder="Enter your paragraph for preprocessing...")

col1, col2, col3, col4 = st.columns(4)

# Initialize output
output = None
process_name = ""

# Check if input is provided
if text_input.strip():
    tokens = word_tokenize(text_input)

    # Tokenization
    if col1.button("Tokenize"):
        process_name = "🔹 Tokenization Result"
        output = tokens

    # Stopword Removal
    if col2.button("Stopwords"):
        process_name = "🧹 Stopword Removal Result"
        output = [word for word in tokens if word.lower() not in stopwords.words('english')]

    # Stemming
    if col3.button("Stemming"):
        process_name = "🌿 Stemming Result"
        stemmer = PorterStemmer()
        output = [stemmer.stem(word) for word in tokens]

    # Lemmatization
    if col4.button("Lemmatization"):
        process_name = "🪷 Lemmatization Result"
        lemmatizer = WordNetLemmatizer()
        output = [lemmatizer.lemmatize(word) for word in tokens]

# Show badge and output
if output is not None:
    st.markdown(f"<div class='badge'>{process_name}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='output-box'>{output}</div>", unsafe_allow_html=True)
elif text_input.strip():
    st.info("Click any preprocessing button to see results 💫")
else:
    st.info("Paste text above and choose a preprocessing step 💫")

# Footer badge
st.markdown("<div style='text-align:center; margin-top:20px;'><span class='badge'>Made with ❤️ by UMAR IMAM</span></div>", unsafe_allow_html=True)
