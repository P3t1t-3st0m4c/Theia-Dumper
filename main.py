import requests
import urllib3
from bs4 import BeautifulSoup

THEIA_LINK = "https://elffe.theia.fr/"
PDF_LINK = "playtest/classic/print/{}/1/1"
INDEX = "learning/exam/index"
CORRECTION = "assessment/correction/{}"
COOKIES = {
    "THEIASESSIDB" : ""
}

def get_Base_Ids():
    ids = []
    r = requests.post(THEIA_LINK + INDEX, data={"grid_3f31d346c14f369a4c47908d3a0d82e3[assessmentStatus][from][]":"2"}, cookies=COOKIES)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.select("a.btn.btn-action.btn-warning.btn-xs.btn-action"):
        ids.append(a.attrs["data-id"])
    return ids

def get_PDF_id(base_id):
    r = requests.get(THEIA_LINK + CORRECTION.format(base_id), cookies=COOKIES)
    soup = BeautifulSoup(r.text, "html.parser")
    id = soup.select_one("assessment-correction-player")
    return id.attrs[":assessment-session-id"]

def get_PDF(id):
    r = requests.get(THEIA_LINK + PDF_LINK.format(id), cookies=COOKIES)
    title = r.headers["Content-Disposition"].strip('attachment; filename=').strip('"').strip(".pdf")
    title = " ".join(title.split("-")[3:]).capitalize()
    print("Downloading " + title)
    with open(f"./data/{title}.pdf", "wb") as f:
        f.write(r.content)

def main():
    COOKIES["THEIASESSIDB"] = input("Please enter your THEIA session cookie : ")
    ids = get_Base_Ids()
    with open("./data/ids.txt", "r") as f:
        old_ids = f.read().splitlines()
        for id in ids:
            if id not in old_ids:
                pdf_id = get_PDF_id(id)
                get_PDF(pdf_id)
                with open("./data/ids.txt", "a") as f:
                    f.write(id + "\n")

main()