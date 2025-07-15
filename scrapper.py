from playwright.sync_api import sync_playwright
def scrapping_ch(url, output_file='chapter1.txt', screenshot_file='chapter1.png'):
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        print(f"Navigating to {url}...")
        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)
        page.screenshot(path=screenshot_file)
        print(f" Screenshot saved as {screenshot_file}")
        content=page.content()
        text=page.inner_text('body')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Chapter content saved as {output_file}")
        browser.close()

if __name__ == "__main__":
    chapter_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scrapping_ch(chapter_url)