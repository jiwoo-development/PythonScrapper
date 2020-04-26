import requests
from bs4 import BeautifulSoup


def so(term):
    try:
        datas = []
        url = f"https://stackoverflow.com/jobs?r=true&q={term}"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        checking(soup)
        listResults = soup.find("div", {"class": "listResults"})
        job = listResults.find_all("div", {"class": "-job"})
        for item in job:
            title = item.find("h2")

            href = title.find("a")["href"]

            title = title.get_text().strip()

            h3 = item.find("h3")
            company = h3.find("span").string.strip()

            data = {
                "title": title,
                "company": company,
                "href": f"https://stackoverflow.com{href}"
            }
            datas.append(data)
        return datas
    except:
        print("error")
        return False


def checking(soup):
    description = soup.find("span", {"class": "description"}).string
    if("0 jobs" in description):
        raise Exception()
