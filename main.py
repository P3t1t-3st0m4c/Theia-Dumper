import requests
import threading
from bs4 import BeautifulSoup

THEIA_LINK = "https://elffe.theia.fr/"
PDF_LINK = "playtest/classic/print/{}/1/1"
INDEX = "learning/exam/index"
CORRECTION = "assessment/correction/{}"
GRID = "grid_3f31d346c14f369a4c47908d3a0d82e3"
COOKIES = {
    "THEIASESSIDB" : ""
}

def get_Base_Ids():
    ids = []
    with requests.Session() as s:
        s.post(THEIA_LINK + INDEX, data={GRID + "[assessmentStatus][from][]":"2"}, cookies=COOKIES)
        r = s.get(THEIA_LINK + INDEX, cookies=COOKIES)
        soup = BeautifulSoup(r.text, "html.parser")
        form = soup.select_one("#" + GRID)
        tab = form.select_one("table")
        for tr in tab.select("tr")[1:]:
            a = tr.select_one("a")
            if a is not None:
                ids.append(tr.attrs["data-id"])
        print(f"Found {len(ids)} new ids")
        return ids

def get_PDF_ids(base_ids):
    ids = []
    for base_id in base_ids:
        r = requests.get(THEIA_LINK + CORRECTION.format(base_id), cookies=COOKIES)
        soup = BeautifulSoup(r.text, "html.parser")
        id = soup.select_one("assessment-correction-player")
        if id is not None:
            ids.append(id.attrs[":assessment-session-id"])

    print(f"Found {len(ids)} new pdf ids")
    return ids

def get_PDF(id, cookies):
    r = requests.get(THEIA_LINK + PDF_LINK.format(id), cookies=cookies)
    title = r.headers["Content-Disposition"].strip('attachment; filename=').strip('"').strip(".pdf")
    title = " ".join(title.split("-")[3:]).capitalize()
    print("Downloading " + title)
    with open(f"./data/{title}.pdf", "wb") as f:
        f.write(r.content)

def get_PDFs(pdf_ids, cookies):
    if isinstance(pdf_ids, int):
        pdf_ids = [pdf_ids]
    for pdf_id in pdf_ids:
        get_PDF(pdf_id, cookies)

def main():
    COOKIES["THEIASESSIDB"] = input("Please enter your THEIA session cookie : ")
    # Set the speed of the download
    # 0 = 1 thread
    # 1 = slow
    # 10 = fast (1 thread per download)
    speed = int(input("Please enter the speed of the download (0-10) : "))
    if speed < 0:
        speed = 0
    elif speed > 10:
        speed = 10
    ids = get_Base_Ids()
    pdf_ids = get_PDF_ids(ids)
    nb_threads = len(pdf_ids) * speed // 10 + 1
    if nb_threads == 0:
        nb_threads = 1
    threads = []
    for i in range(nb_threads):
        t = threading.Thread(target=get_PDFs, args=(pdf_ids[i::nb_threads], COOKIES))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

main()