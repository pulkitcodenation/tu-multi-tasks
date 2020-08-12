from requests_futures.sessions import FuturesSession
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    session = FuturesSession()
    req_list = []
    for url in sites:
        req_list.append(session.get(url))
    for req, url in zip(req_list, sites):
        response = req.result()
        print(f"Read {len(response.content)} from {url}")


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
