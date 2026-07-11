from playwright.sync_api import Page

class WikipediaPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.wikipedia.org")

    def search(self, term):
        self.page.locator('input[name="search"]').fill(term)
        self.page.keyboard.press("Enter")

    def get_title(self):
        return self.page.title()
    
def test_wikipedia_title(page: Page):
    wiki = WikipediaPage(page)
    wiki.goto()
    assert "Wikipedia" in wiki.get_title()

def test_wikipedia_search_python(page: Page):
    wiki = WikipediaPage(page)
    wiki.goto()
    wiki.search("Python programming")
    assert "Python" in wiki.get_title()