class TestBlogPage(object):

    def test_blog_page(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/')
        assert browser.status_code == 200
        assert browser.is_text_present('blog')

    def test_blog_page_click_search(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/')
        browser.fill('q', 'test')
        button = browser.find_by_css('.btn-default')[0]
        button.click()
        assert browser.url == 'http://127.0.0.1:8000/blog/search/?q=test'
        assert browser.status_code == 200
        assert browser.is_text_present('Entries for search')
