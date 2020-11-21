class event:
    def __init__(self,province,id,location,title,party,link,date):
        self.province = province
        self.id = id
        self.location = location
        self.title = title
        self.party = party
        self.link = link
        self.date = date
        

    def __str__(self):
        return"""
        title: %s
        id: %s
        location: %s
        province: %s
        party: %s
        link: %s
        date: %s
        """%(self.title,self.id,self.location,self.province,self.party,self.link,self.date)
