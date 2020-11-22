from bs4 import BeautifulSoup
import urllib3
import event as evnt


def get_on_lib_event():
    ulr_manager = urllib3.PoolManager()
    site = "https://ontarioliberal.ca/events/"
    page = ulr_manager.request('GET',site)
    soup = BeautifulSoup(page.data,"html.parser")

    block_list = soup.find_all(class_="cell large-4 medium-6 events-listing-single")

    #basic information
    province = "Ontario"
    party = "Liberal"
    id = 0
    event_list = []

    for block in block_list:
        title = block.h2.string
        date = block.find("p",class_="entry-date").string
        link = block.a["href"]
        detail_page = ulr_manager.request('GET',link)
        detail_soup = BeautifulSoup(detail_page.data,"html.parser")
        location = detail_soup.find("p",class_="location").span.string
        event_list.append(evnt.event(province,id,location,title,party,link,date))
        id += 1
        print("%s Liberal event found"%id)

    return event_list