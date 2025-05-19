# Chat Log Analyzer

This project is a Python-based tool for analyzing chat logs between a **User** and an **AI**. It parses chat logs, extracts messages, and summarizes the conversation by identifying key insights using either **TF-IDF-based** or **frequency-based** keyword extraction.

---

## 📂 Features

- Parses chat logs from a plain text file (`text.txt`)
- Separates user and AI messages
- Extracts top keywords using:
  - **TF-IDF (Term Frequency-Inverse Document Frequency)**
  - or **Raw frequency (token count)**
- Prints a summary of the conversation including:
  - Total message count
  - Breakdown by User and AI
  - Most relevant keywords using TF-IDF algo

---

## 🧪 Example Output
```
  Summary:
     - The conversation had 6 exchanges.
     - Messages from user: 3, from AI: 3.
     - Most common keywords: use, good, python, luck, hi
```

---

## 🔧 How It Works

### 1. `read_chat_log(file)`
Reads the chat file line by line.

### 2. `parse_chat(lines)`
Splits messages between the User and the AI.

### 3. `tfidf_keywords(messages, top_n=5)`
Extracts top N keywords based on TF-IDF scoring using `sklearn`.

### 4. `clean_and_tokenize(messages)`
Cleans and tokenizes the text using NLTK, removing stopwords and punctuation.

### 5. `get_frequent_keywords(words, top_n=5)`
Returns the most common keywords by raw count.

### 6. `generate_summary(user_msgs, ai_msgs, use_tfidf=True)`
Generates a readable summary using the selected keyword extraction strategy.

---

## 📁 Input File Format

Create a `text.txt` file in the same directory, formatted like this:

```
User: Hello!
AI: Hi there! How can I help you today?
User: What is TF-IDF?
AI: TF-IDF stands for Term Frequency-Inverse Document Frequency...
```

---

## ▶️ Run the Script

Make sure you've installed the dependencies on requirements.txt, then run:

```
python your_script_name.py
```

