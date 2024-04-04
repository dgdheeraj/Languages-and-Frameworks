'''
Newsletter and ppl subscribing to it. Once new news is added, all ppl are notified
'''

class Newsletter:
    def __init__(self):
        self.observers = []
        self.__news = []
    
    def addNews(self, article):
        self.__news.append(article)
        self.notify(article)
    
    def subscribe(self, user):
        self.observers.append(user)
    
    def unsubscribe(self, user):
        self.observers.remove(user)
    
    def notify(self, article):
        for user in self.observers:
            user.notify(article)

class User:
    def __init__(self, name):
        self.name = name
    
    def notify(self, article):
        print(f"User: {self.name} notified on article: {article}")

newsletter = Newsletter()
u1 = User("Dheeraj")
u2 = User("Anoop")
newsletter.subscribe(u1)
newsletter.subscribe(u2)
newsletter.addNews("Article 1")
