
from extractors.drugs import get_drugs

import requests_cache
requests_cache.install_cache('ndacrawler.sqlite3')


if __name__ == "__main__":
    print(get_drugs()["Herbal Human"].to_csv_file("herbal_human.csv"))
