import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Madina Munavvara")

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# ---------------------- MA'LUMOTLAR ----------------------

FAZILATLAR = [
    {
        "sarlavha": "Madinaning fazilati Rasulullohning hadislarida",
        "matn": "Payg'ambarimiz sallallohu alayhi vasallam Madinani \"Toyba\" (pokiza) va \"Tabo\" deb nomlaganlar. Bu shahar hijrat diyori bo'lib, unda ko'plab sahobalar dafn etilgan."
    },
    {
        "sarlavha": "Dajjol Madinaga kira olmaydi",
        "matn": "Rivoyatlarga ko'ra, Makka va Madina shaharlariga Dajjol kira olmaydi, chunki bu ikki muqaddas shaharni farishtalar qo'riqlab turadi."
    },
    {
        "sarlavha": "Madinada vabo va tounga qarshi himoya",
        "matn": "Hadislarda aytilishicha, Madinaga vabo va tun kasalligi kirmaydi, bu shahar Alloh tomonidan alohida himoyalangan."
    },
    {
        "sarlavha": "Masjidi Nabaviyda namoz o'qishning savobi",
        "matn": "Masjidi Nabaviyda o'qilgan bir namoz, Masjidi Harom bundan mustasno, boshqa masjidlarda o'qilgan ming namozdan afzaldir."
    },
    {
        "sarlavha": "Riyazul Jannah - Jannat bog'chasi",
        "matn": "Payg'ambarimizning minbari bilan uylari orasidagi joy \"Riyazul Jannah\" (Jannat bog'chalaridan bir bog'cha) deb ataladi va u yerda duo qilish alohida fazilatga ega."
    },
    {
        "sarlavha": "Madinada vafot etishning fazilati",
        "matn": "Rasululloh sollallohu alayhi vasallam kim Madinada vafot etsa, u qiyomat kuni Rasulullohning shafoatiga muyassar bo'lishini bashorat qilganlar."
    },
]

DUOLAR = [
    {
        "nomi": "Madinaga kirishda o'qiladigan duo",
        "arab": "اللَّهُمَّ هَذَا حَرَمُ نَبِيِّكَ فَاجْعَلْهُ وِقَايَةً لِي مِنَ النَّارِ",
        "tarjima": "Ey Alloh! Bu Sening Payg'ambaring harami (muqaddas hududi)dir. Uni men uchun do'zaxdan himoya qiluvchi qilgin."
    },
    {
        "nomi": "Masjidi Nabaviyga kirishda",
        "arab": "بِسْمِ اللَّهِ وَالصَّلَاةُ وَالسَّلَامُ عَلَى رَسُولِ اللَّهِ، اللَّهُمَّ افْتَحْ لِي أَبْوَابَ رَحْمَتِكَ",
        "tarjima": "Alloh nomi bilan, Rasulullohga salovat va salom bo'lsin. Ey Alloh, menga rahmating eshiklarini ochib qo'ygin."
    },
    {
        "nomi": "Payg'ambarga salom berish",
        "arab": "السَّلَامُ عَلَيْكَ يَا رَسُولَ اللَّهِ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ",
        "tarjima": "Senga salom bo'lsin, ey Allohning Rasuli, Allohning rahmati va barakoti ham bo'lsin."
    },
    {
        "nomi": "Riyazul Jannahda o'qiladigan duo",
        "arab": "رَبِّ اغْفِرْ لِي وَلِوَالِدَيَّ وَارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا",
        "tarjima": "Robbim, meni va ota-onamni mag'firat qilgin, ular meni kichikligimda tarbiyalaganlariga o'xshab, ularga rahm qilgin."
    },
    {
        "nomi": "Masjiddan chiqishda",
        "arab": "اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ",
        "tarjima": "Ey Alloh, men Sendan fazlingdan (ne'matingdan) so'rayman."
    },
]

JOYLAR = [
    {
        "nomi": "Masjidi Nabaviy",
        "tavsif": "Payg'ambarimiz sollallohu alayhi vasallam qurgan va o'zlari dafn etilgan muqaddas masjid. Dunyodagi eng fazilatli uchinchi masjid.",
        "fazilati": "Bu yerda o'qilgan bir namoz 1000 namozga teng savobga ega (Masjidi Haromdan tashqari)."
    },
    {
        "nomi": "Riyazul Jannah",
        "tavsif": "Payg'ambarimizning uyi bilan minbari orasidagi kichik maydon bo'lib, Masjidi Nabaviy ichida joylashgan.",
        "fazilati": "Rasululloh: \"Uyim bilan minbarim orasi jannat bog'laridan bir bog'chadir\", deganlar."
    },
    {
        "nomi": "Jannatul Baqiy qabristoni",
        "tavsif": "Ko'plab sahobalar, Payg'ambarimizning oila a'zolari va yaqinlari dafn etilgan qadimiy qabriston.",
        "fazilati": "Bu yerga ziyorat qilish va marhumlarga duo qilish sunnatga muvofiqdir."
    },
    {
        "nomi": "Uhud tog'i",
        "tavsif": "Mashhur Uhud jangi bo'lib o'tgan joy, shu jangda shahid bo'lgan 70 dan ortiq sahobalar shu yerda dafn etilgan.",
        "fazilati": "Rasululloh: \"Uhud shunday tog'ki, u bizni sevadi, biz ham uni sevamiz\", deganlar."
    },
    {
        "nomi": "Quba masjidi",
        "tavsif": "Islom tarixidagi birinchi qurilgan masjid bo'lib, Payg'ambarimiz Madinaga hijrat qilganlarida qurdirganlar.",
        "fazilati": "Bu yerda ikki rakat namoz o'qigan kishiga umra savobi yoziladi, degan rivoyat bor."
    },
    {
        "nomi": "Qiblatayn masjidi",
        "tavsif": "Qiblaning Baytul Maqdisdan Ka'baga o'zgartirilishi shu masjidda namoz vaqtida amalga oshirilgan.",
        "fazilati": "Islom tarixida qibla o'zgargan yagona joy sifatida alohida ahamiyatga ega."
    },
]

@app.get("/", response_class=HTMLResponse)
async def bosh_sahifa(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/fazilatlar", response_class=HTMLResponse)
async def fazilatlar_sahifa(request: Request):
    return templates.TemplateResponse(request, "fazilatlar.html", {"fazilatlar": FAZILATLAR})

@app.get("/duolar", response_class=HTMLResponse)
async def duolar_sahifa(request: Request):
    return templates.TemplateResponse(request, "duolar.html", {"duolar": DUOLAR})

@app.get("/joylar", response_class=HTMLResponse)
async def joylar_sahifa(request: Request):
    return templates.TemplateResponse(request, "joylar.html", {"joylar": JOYLAR})

@app.get("/haqida", response_class=HTMLResponse)
async def haqida_sahifa(request: Request):
    return templates.TemplateResponse(request, "haqida.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

