import csv


def save_csv(term, datas):
    file = open(f"{term}.csv", mode="w", encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "href"])
    for data in datas:
        writer.writerow(data.values())
