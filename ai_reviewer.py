from transformers import pipeline
import os

def review_chapter(input_file='chapter1_ai.txt', output_file='chapter1_reviewed.txt'):
    print("Reading AI-rewritten chapter...")
    with open(input_file, 'r', encoding='utf-8') as f:
        rewritten_text = f.read()

    print("Loading Hugging Face reviewer model...")
    reviewer = pipeline("text2text-generation", model="google/flan-t5-base")

    print("Asking AI to review and improve...")
    prompt = f"Review the following text for readability, tone, and engagement. Suggest improved version:\n\n{rewritten_text}"

    response = reviewer(prompt, max_length=1024, do_sample=True, temperature=0.7)

    reviewed_text = response[0]['generated_text']

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(reviewed_text)

    print(f"Reviewed chapter saved as: {output_file}")
    print("\nPreview:\n")
    print(reviewed_text[:1000], "...\n")

if __name__ == "__main__":
    review_chapter()
