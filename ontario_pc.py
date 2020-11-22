from bs4 import BeautifulSoup
import urllib3 as urlib
import event as evnt


def get_on_pc_event():
    url_manager = urlib.PoolManager()
    site = "https://www.ontariopc.ca/events"
    main_site = url_manager.request('GET',site)

    soup = BeautifulSoup(main_site.data,"html.parser")
    event_block = soup.find_all("div",class_="event")

    #baisc information 
    party = "PC"
    province = "Ontario"
    id = 0
    event_list = []
    for event in event_block:
        link = site+event.find("a",class_="event__register")["href"]
        date = event.find("div",class_="event__date--month").string.lstrip().rstrip()+ " " + event.find("div",class_="event__date--day").string.lstrip().rstrip()
        location = event.find("div",class_="event__venue").string
        if location == None:#sometime it is not in the div tag directly but in a tag
            location = event.find("div",class_="event__venue").a.string
        location = location.lstrip().rstrip()
        title = event.find("h4",class_="event__headline").string
        event_list.append(evnt.event(province,id,location,title,party,link,date))
        id += 1
        print("%s PC event found"%id)

    return event_list
