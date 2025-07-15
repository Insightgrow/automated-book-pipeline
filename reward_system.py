import textstat
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import csv
import os

nltk.download('punkt')

def load_text(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def readability_score(text):
    return textstat.flesch_reading_ease(text)

def similarity_score(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    return cosine_similarity([vectors[0]], [vectors[1]])[0][0]

def reward_evaluation(original_file, ai_file, reviewed_file, final_file, chapter_id=None, url=None, log_file='logs.csv'):
    print("Evaluating Rewrites and Final Edits...\n")

    original = load_text(original_file)
    ai_version = load_text(ai_file)
    final_version = load_text(final_file)

    sim_ai = similarity_score(original, ai_version)
    sim_final = similarity_score(original, final_version)

    read_ai = readability_score(ai_version)
    read_final = readability_score(final_version)

    print(f"AI Rewrite Similarity with Original: {sim_ai:.2f}")
    print(f"Human Final Similarity with Original: {sim_final:.2f}")
    print(f"AI Rewrite Readability Score: {read_ai:.2f}")
    print(f"Final Version Readability Score: {read_final:.2f}")

    reward = "Yes" if sim_final > sim_ai and read_final >= read_ai else "No"
    print(f"\nReward Suggestion: Human-edited version rewarded? → {reward}")


    header = ["Chapter ID", "URL", "Similarity (AI)", "Similarity (Final)", "Readability (AI)", "Readability (Final)", "Human Rewarded?"]
    row = [chapter_id, url, f"{sim_ai:.2f}", f"{sim_final:.2f}", f"{read_ai:.2f}", f"{read_final:.2f}", reward]

    file_exists = os.path.exists(log_file)
    with open(log_file, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)
