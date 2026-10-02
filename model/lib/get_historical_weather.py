import requests

params = {
    "station": "DEN", "data": ["tmpf", "sknt", "gust", "vsby", "p01i", "wxcodes", "skyc1"],
    "year1": 2022, "month1": 1, "day1": 1,
    "year2": 2025, "month2": 12, "day2": 31,
    "tz": "America/Denver", "format": "onlycomma", "missing": "empty", "trace": "0.0001",
    "report_type": [3, 4],
}
r = requests.get("https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py", params=params, timeout=300)
open("model/data/raw/den-weather.csv", "w").write(r.text)