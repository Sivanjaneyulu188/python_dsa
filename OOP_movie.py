class Movie:
    def __init__(self,name,price,genre):
        self.name=name
        self.price=price
        self.genre=genre
        
    def display_info(self):
        print("Movie Name:{}".format(self.name))
        print("price:{}".format(self.price))
        print("Genre:{}".format(self.genre))
        
    def get_price(self):
        return self.price
    
class TicketBooking(Movie):
    def __init__(self,name,price,genre):
        super().__init__(name,price,genre)
    def display_info(self):
        super().display_info()
        
class cart:    
    def __init__(self,theater):
        self.movie=[]
        self.theater=theater
                
    def add_to_cart(self,moviename,tickets):
        item =(moviename,tickets)
        self.movie.append(item)
        
    def view_bill(self):
        total=0
        for moviename, tickets in self.movie:
            price=moviename.get_price()
            total+=price*tickets 
        return total
    
    def cart_details(self):
        for moviename, tickets in self.movie:
            moviename.display_info()
            print("no of tickets:{}".format(tickets))
            print("Theater:{}".format(self.theater))
            print()
        print("-------------")
        bil=self.view_bill()
        print("Total bill:{}".format(bil))

m1=TicketBooking("Mirai",250,"Animation")
m2=TicketBooking("Avatar",300,"Sci-fi")
c1=cart("PVR")
c1.add_to_cart(m1,2)
c1.add_to_cart(m2,3)        
c1.cart_details()