import csv


def sav_to_csv(title, data):
    file = open(f"{title}.csv", mode="w", encoding='utf-8-sig')
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
    return
