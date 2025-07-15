from transformers import pipeline
import os

def rewrite_chapter(input_file='chapter1.txt', output_file='chapter1_ai.txt'):
    print("Reading original chapter content")
    with open(input_file, 'r', encoding='utf-8') as f:
        original_text = f.read()

    print("Loading Hugging Face model")
    rewrite = pipeline("text2text-generation", model="google/flan-t5-base")

    print("Rewriting with Hugging Face model...")
    prompt = f"Rewrite this chapter content in modern English, making it easier to understand while keeping the content and tone intact:\n\n{original_text[:1000]}"

    response = rewrite(prompt, max_length=1024, do_sample=True)[0]['generated_text']

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(response)

    print(f"Rewritten version saved as {output_file}")
    print("\nPreview:\n")
    print(response[:1000], "...\n")

if __name__ == "__main__":
    rewrite_chapter()
