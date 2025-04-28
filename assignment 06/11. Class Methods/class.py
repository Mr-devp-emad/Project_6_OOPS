class Book:
    # Class variable to keep track of total books
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment the total books count when a new book is created
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        """Class method to increment the total number of books"""
        cls.total_books += 1
    
    def __str__(self):
        return f"{self.title} by {self.author}"

# Example usage
if __name__ == "__main__":
    # Create some books
    book1 = Book("Pride and Prejudice" , "Jane Austen")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
    book3 = Book("War and Peace", "Leo Tolstoy")
    
    # Print the total number of books
    print(f"Total books in library: {Book.total_books}")
