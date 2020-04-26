import requests
from bs4 import BeautifulSoup


def remoteok(term):
    try:
        datas = []
        url = f"https://remoteok.io/remote-dev+{term}-jobs"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        checking(soup)
        jobsboard = soup.find("table", {"id": "jobsboard"})
        tr = jobsboard.find_all("tr", {"class": "job"})
        for box in tr:
            time = box.find("td", {"class": "time"}).string
            if "d" in time:
                company = box.find("td", {"class": "company"})

                companyName = company.find(
                    "a", {"class": "companyLink"}).find("h3").string

                title = company.find("h2").string

                href = box.find("td", {"class": "time"}).find("a")["href"]

                data = {
                    "title": title,
                    "company": companyName,
                    "href": f"https://remoteok.io{href}"
                }
                datas.append(data)
        return datas
    except:
        return False


def checking(soup):
    title = soup.find("title").string
    if("Not Found" in title):
        raise Exception()
