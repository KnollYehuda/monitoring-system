import os
from pathlib import Path

CELERY_DIR = os.environ.get("CELERY_DIR", "/tmp/monitoring_system/celery")
CELERY_DIR_PATH = Path(CELERY_DIR)
DB_CONNECTION_STRING = "postgresql://guest:guest@postgres:5432/monitoring_system"
WEBSITES = [
    "https://www.nytimes.com/",
    "https://www.wsj.com/",
    "https://www.huffpost.com/",
    "https://www.latimes.com/",
    "https://www.reuters.com/",
    "https://abcnews.go.com/",
    "https://www.usatoday.com/",
    "https://www.bloomberg.com/",
    "https://www.nbcnews.com/",
    "https://www.bbc.com/news",
    "https://www.cnn.com/",
    "https://www.theguardian.com/us",
    "https://www.forbes.com/",
    "https://www.npr.org/",
    "https://www.foxnews.com/",
    "https://www.cbsnews.com/",
    "https://www.dailymail.co.uk/ushome/index.html",
    "https://www.aljazeera.com/",
    "https://www.politico.com/",
    "https://www.buzzfeednews.com/",
    "https://www.vox.com/",
    "https://www.propublica.org/",
    "https://www.economist.com/",
    "https://www.ft.com/",
    "https://www.msnbc.com/",
    "https://www.newyorker.com/",
    "https://www.time.com/",
    "https://www.newsweek.com/",
    "https://www.theatlantic.com/",
    "https://www.salon.com/",
    "https://www.slate.com/",
    "https://www.thedailybeast.com/",
    "https://www.vanityfair.com/",
    "https://www.nationalreview.com/",
    "https://www.thehill.com/",
    "https://www.chicagotribune.com/",
    "https://www.bostonglobe.com/",
    "https://www.sfchronicle.com/",
    "https://www.nydailynews.com/",
    "https://www.denverpost.com/",
    "https://www.startribune.com/",
    "https://www.seattletimes.com/",
    "https://www.azcentral.com/",
    "https://www.dallasnews.com/",
    "https://www.freep.com/",
    "https://www.tampabay.com/",
    "https://www.orlandosentinel.com/",
    "https://www.cleveland.com/",
    "https://www.philly.com/",
    "https://www.oregonlive.com/",
    "https://www.baltimoresun.com/",
    "https://www.nola.com/",
    "https://www.courant.com/",
    "https://www.indystar.com/",
    "https://www.dispatch.com/",
    "https://www.oklahoman.com/",
    "https://www.tennessean.com/",
    "https://www.jsonline.com/",
    "https://www.desmoinesregister.com/",
    "https://www.lasvegassun.com/",
    "https://www.arkansasonline.com/",
    "https://www.omaha.com/",
    "https://www.richmond.com/",
    "https://www.savannahnow.com/",
    "https://www.charlotteobserver.com/",
    "https://www.sun-sentinel.com/",
    "https://www.mercurynews.com/",
    "https://www.sandiegouniontribune.com/",
    "https://www.houstonchronicle.com/",
    "https://www.expressnews.com/",
    "https://www.statesman.com/",
    "https://www.abqjournal.com/",
    "https://www.sltrib.com/",
    "https://www.idahostatesman.com/",
    "https://www.spokesman.com/",
    "https://www.adn.com/",
    "https://www.wvgazettemail.com/",
    "https://www.burlingtonfreepress.com/",
    "https://www.unionleader.com/",
    "https://www.pressherald.com/",
    "https://www.providencejournal.com/",
    "https://www.theday.com/",
    "https://www.capecodtimes.com/",
    "https://www.telegram.com/",
    "https://www.sunjournal.com/",
    "https://www.benningtonbanner.com/",
    "https://www.concordmonitor.com/",
    "https://www.vnews.com/",
    "https://www.caledonianrecord.com/",
    "https://www.timesargus.com/",
    "https://www.reformer.com/",
    "https://www.sevendaysvt.com/",
    "https://www.valleynews.com/",
    "https://www.bostonglobe.com/metro/new-hampshire",
    "https://www.bostonglobe.com/metro/maine",
    "https://www.bostonglobe.com/metro/vermont",
    "https://www.bostonglobe.com/metro/rhode-island",
    "https://www.bostonglobe.com/metro/connecticut",
    "https://www.bostonglobe.com/metro/massachusetts",
    "https://www.bostonglobe.com/metro/boston",
    "https://www.bostonglobe.com/metro/worcester",
    "https://www.bostonglobe.com/metro/springfield",
    "https://www.bostonglobe.com/metro/cape-cod",
    "https://www.bostonglobe.com/metro/north-shore",
    "https://www.bostonglobe.com/metro/south-shore",
    "https://www.bostonglobe.com/metro/metro-west",
    "https://www.bostonglobe.com/metro/central-mass",
    "https://www.bostonglobe.com/metro/western-mass",
    "https://www.bostonglobe.com/metro/new-england",
    "https://www.bostonglobe.com/metro/nation",
    "https://www.bostonglobe.com/metro/world",
    "https://www.bostonglobe.com/metro/politics",
    "https://www.bostonglobe.com/metro/business",
    "https://www.bostonglobe.com/metro/technology",
    "https://www.bostonglobe.com/metro/health-science",
    "https://www.bostonglobe.com/metro/education",
    "https://www.bostonglobe.com/metro/arts",
    "https://www.bostonglobe.com/metro/sports",
    "https://www.bostonglobe.com/metro/lifestyle",
    "https://www.bostonglobe.com/metro/food",
    "https://www.bostonglobe.com/metro/travel",
    "https://www.bostonglobe.com/metro/magazine",
    "https://www.bostonglobe.com/metro/opinion",
    "https://www.ynet.co.il",
    "https://www.mako.co.il",
    "https://www.walla.co.il",
]
