class BookStore():

    NoOfBooks = 0

    def __init__ (self,A,B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name,"by",self.Author,". no of books: ",BookStore.NoOfBooks)

def main ():
    obj1=BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2=BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()