import requests
from bs4 import BeautifulSoup

from scrapping.so import so
from scrapping.remoteok import remoteok
from scrapping.wwr import wwr


def scrapping(term):
    datas = []
    if so(term):
        datas.extend(so(term))
    if remoteok(term):
        datas.extend(remoteok(term))
    if wwr(term):
        datas.extend(wwr(term))
    return datas
