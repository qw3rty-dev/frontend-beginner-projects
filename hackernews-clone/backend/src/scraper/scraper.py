import asyncio

import httpx
from bs4 import BeautifulSoup


def int_extractor(text):
    if text is None:
        return None
    digits = "".join(x for x in text if x.isdigit())
    return int(digits) if digits else None

def get_comments_link(subtext):
    links = subtext.select("a")
    for link in links:
        text = link.text
        if "comment" in text or "discuss" in text:
            path = link.get("href")
            return f"https://news.ycombinator.com/{path}"
    return None
        
def get_comments(subtext):
    links = subtext.select("a")
    for link in links:
        text = link.text
        if "comment" in text or "discuss" in text:
            # print(link)
            return int_extractor(text)
    return None

def get_score(subtext):
    raw_score = subtext.select_one(".score")
    if raw_score and "points" in raw_score.text:
        return int_extractor(raw_score.text)
    return None

async def news_scraper(url):
    posts =[]
    async with httpx.AsyncClient(timeout=10.0) as client:
        req = await client.get(url)
        if req.status_code != 200:
            print("Request failed")
            return None
        soup=BeautifulSoup(req.text,"lxml")
        data=soup.select(".athing")
        for news in data:
            
            rank_tag = news.select_one(".rank")
            rank = rank_tag.text if rank_tag else None

            title_tag = news.select_one(".titleline a")
            title = title_tag.text
            
            link = title_tag.get("href")

            domain_tag = news.select_one(".sitestr")
            domain = domain_tag.text if domain_tag else None
            domain_link = f"https://news.ycombinator.com/from?site={domain}"

            subtext = news.find_next_sibling("tr")
            score = get_score(subtext)
            comments = get_comments(subtext)
            comments_link = get_comments_link(subtext)

            author_tag = subtext.select_one(".subtext .subline a")
            author = author_tag.text if author_tag else None
            author_info = f"https://news.ycombinator.com/user?id={author}"
            
            time_ago_tag = subtext.select_one(".age a")
            time_ago = time_ago_tag.text if time_ago_tag else None

            post = {
                "rank": rank,
                "title": title,
                "link": link,
                "score": score,
                "author": author,
                "author_info_link": author_info,
                "comments": comments,
                "comments_link": comments_link,
                "domain": domain,
                "domain_link": domain_link,
                "time_ago":time_ago
            }
            posts.append(post)
            # print(comments)
        return posts


if __name__== "__main__":
    asyncio.run(news_scraper("https://news.ycombinator.com/"))