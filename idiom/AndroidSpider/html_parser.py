import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, url, content, html_encode="utf-8"):
        if url is None or content is None:
            return
        soup = BeautifulSoup(content, "html.parser", from_encoding=html_encode)
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data


    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"zishu_12\w+"))
        for link in links:
            url_path = link["href"]
            new_url = urljoin(url, url_path)
            new_urls.add(new_url)
        return new_urls


    def _get_new_data(self, url, soup):
       # data = {"url": url}
        aList = []
        title_node = soup.find("ul", class_="l3 center f14").findAll("li")
        for i in title_node:
            tds = i("a")
            aList.append(tds[0].string)



        return aList