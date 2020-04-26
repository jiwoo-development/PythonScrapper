import requests
from bs4 import BeautifulSoup


def wwr(term):
    try:
        datas = []
        url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        job_list = soup.find("div", {"id": "job_list"})
        checking(job_list)
        sections = job_list.find_all("section")
        for section in sections:
            tagAs = section.select("li.feature > a")
            for tagA in tagAs:
                href = tagA["href"]

                company = tagA.find("span", {"class": "company"}).string

                title = tagA.find("span", {"class": "title"}).string

                data = {
                    "title": title,
                    "company": company,
                    "href": f"https://weworkremotely.com{href}"
                }
                datas.append(data)
        return datas
    except:
        return False


def checking(soup):
    try:
        results = job_list.find("div", {"class": "no_results"})
        raise Exception()
    except:
        pass
