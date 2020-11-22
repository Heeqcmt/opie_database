from bs4 import BeautifulSoup
import urllib3 as urlib
import event as evnt
import re #for regex in the link


def get_ndp_on_event ():
    #get the site
    urlManager = urlib.PoolManager()

    site = "https://www.ontariondp.ca/events"

    page = urlManager.request('GET',site)

    #parse the site
    soup = BeautifulSoup(page.data,'html.parser')
    event_blocks = soup.find_all("div",{"class":"block--event-list--event"})

    #creating events list
    counter = 0
    province = "Ontario"
    party = "NDP"
    event_list = []

    #each intro event block
    for block in event_blocks:

        location = block.find("div",class_="event-location").decode_contents()
        location = location.replace("<br/>"," ").lstrip().rstrip() #clean up location data 
        #get link to individual event
        link = block.find("a")['href']
        #if link doesnt have the https://www.ontariondp.ca then add one to it
        head_found = re.search("http",link)
        if not head_found:
            link = "https://www.ontariondp.ca"+link
        
        indi_event_page = urlManager.request('GET',link)
        indi_soup = BeautifulSoup(indi_event_page.data,'html.parser')
        title = indi_soup.find("h1").string 
        date = indi_soup.p.string
        id = counter

        event_temp = evnt.event(province,id,location,title,party,link,date)

        event_list.append(event_temp)
        counter += 1

        
        
        print("%s NDP event found"%id)



   

    return event_list


    