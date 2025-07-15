from scrapper import scrapping_ch
from ai_writer import rewrite_chapter
from ai_reviewer import review_chapter
from human_editor import human_edit
from reward_system import reward_evaluation
import os
import csv

def load_chapters(file_path):
    chapters = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        chapters = [(int(row["id"]), row["url"]) for row in reader]
    return chapters

def full_pipeline(url, chapter_id):
    print(f"\nScraping Chapter {chapter_id}...")
    txt_file = f"chapter{chapter_id}.txt"
    screenshot_file = f"chapter{chapter_id}.png"
    scrapping_ch(url, output_file=txt_file, screenshot_file=screenshot_file)

    print(f"\nAI Rewriting Chapter {chapter_id}...")
    rewrite_chapter(input_file=txt_file, output_file=f"chapter{chapter_id}_ai.txt")

    print(f"\nAI Reviewing Chapter {chapter_id}...")
    review_chapter(input_file=f"chapter{chapter_id}_ai.txt", output_file=f"chapter{chapter_id}_reviewed.txt")

    print(f"\nHuman Editing Chapter {chapter_id}...")
    human_edit(input_file=f"chapter{chapter_id}_reviewed.txt", output_file=f"chapter{chapter_id}_final.txt")

    print(f"\nRewarding Chapter {chapter_id}...")
    reward_evaluation(
        original_file=txt_file,
        ai_file=f"chapter{chapter_id}_ai.txt",
        reviewed_file=f"chapter{chapter_id}_reviewed.txt",
        final_file=f"chapter{chapter_id}_final.txt",
        chapter_id=chapter_id,
        url=url
    )

if __name__ == "__main__":
    chapter_list = load_chapters("chapters.csv")
    for chapter_id, url in chapter_list:
        full_pipeline(url, chapter_id=chapter_id)
