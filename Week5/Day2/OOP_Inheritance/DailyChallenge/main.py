# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

class Pagination:
    def __init__(self, items = [], pagesize = 10) -> None:
        self.items = items
        self.pagesize = pagesize
        self.num_pages = (len(self.items)//self.pagesize)+1
        self.current_page = 1


    def getVisibleItems(self):
        visible_list = []
        if self.current_page == 1:
            visible_list = [self.items[i] for i in range(self.pagesize)]
            print(visible_list)
        else:
            for i in range(self.current_page*self.pagesize-self.pagesize, self.current_page*self.pagesize):
                visible_list.append(self.items[i])
            print(visible_list)
    
    def nextPage(self):
        print(self.current_page)
        self.current_page += 1
        print(self.current_page)
        return self.current_page

    def prevPage(self):
        if self.current_page == 1:
            print("You are already on the 1st page")
            
        else:
            self.current_page -= 1
        return self.current_page
    
    def firstPage(self):
        self.current_page = 1
        return self.current_page

    def goToPage(self, pageNum):
        if pageNum > self.num_pages:
            print("There aren't enough pages for your appetite")
        else:
            self.current_page = pageNum

    def lastPage(self):
        self.current_page = self.num_pages





alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# print(alphabetList)

p = Pagination(alphabetList, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# # ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# # ["y", "z"]