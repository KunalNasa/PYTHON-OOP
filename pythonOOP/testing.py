# x = input("Enter the name of book you want")
# with open("KunalLib.txt", 'r') as f:
#     content = str(f.read())
#
# replace = content.replace(x,"None")
# with open("KunalLib.txt",'w') as k:
#     k.write(replace)


# class A:
#     def __init__(self,books):
#         self.books = books
#     def removing(self):
#         print("Books are")
#         x = input("Enter the name of book")
#         self.books.remove(x)



# kunal = A(["Hindi","English","Maths","Science"])
# kunal.removing()
lst = ['"To Kill a Mockingbird" by Harper Lee\n', '"Pride and Prejudice" by Jane Austen\n', '"The Diary of Anne Frank" by Anne Frank\n', '"1984" by George Orwell\n', 'Harry Potter and the Sorcerer\'s Stone" by J.K. Rowling\n', '"The Lord of the Rings" (1-3) by J.R.R. Tolkien\n', '"The Great Gatsby" by F. Scott Fitzgerald\n', '"Charlotte\'s Web" by E.B. White\n', '"The Hobbit" by J.R.R. Tolkien\n', '"Little Women" by Louisa May Alcott\n', '"Fahrenheit 451" by Ray Bradbury\n', '"Jane Eyre" by Charlotte Bronte\n', '"Animal Farm" by George Orwell\n', '"Gone with the Wind" by Margaret Mitchell\n', '"The Catcher in the Rye" by J.D. Salinger\n', '"The Book Thief" by Markus Zusak\n', '"The Adventures of Huckleberry Finn" by Mark Twain\n', '"The Hunger Games" by Suzanne Collins\n', '"The Help" by Kathryn Stockett\n', '"The Lion, the Witch, and the Wadrobe" by C.S. Lewis\n', '"The Grapes of Wrath" by John Steinbeck\n', '"The Lord of the Flies" by William Golding\n', '"The Kite Runner" by Khaled Hosseini\n', '"Night" by Elie Wiesel\n', '"Hamlet" by William Shakespeare\n', '"A Wrinkle in Time" by Madeleine L\'Engle\n', '"Of Mice and Men" by John Steinbeck\n', '"A Tale of Two Cities" by Charles Dickens\n', '"Romeo and Juliet" by William Shakespeare\n', '"The Hitchhikers Guide to the Galaxy" by Douglas Adams\n', '"The Secret Garden" by Frances Hodgson Burnett\n', '"A Christmas Carol" by Charles Dickens\n', '"The Little Prince" by Antoine de Saint-Exupéry\n', '"Brave New World" by Aldous Huxley\n', '"Harry Potter and the Deathly Hallows" by J.K. Rowling\n', '"The Giver" by Lois Lowry\n', '"The Handmaid\'s Tale" by Margaret Atwood\n', '"Where the Sidewalk Ends" by Shel Silverstein\n', '"Wuthering Heights" Emily Bronte\n', '"The Fault in Our Stars" by John Green\n', '"Anne of Green Gables" by L.M. Montgomery\n', '"The Adventures of Tom Sawyer" by Mark Twain\n', '"Macbeth" by William Shakespeare\n', '"The Girl with a Dragon Tattoo" by Stieg Larrson\n', '"Frankenstein" by Mary Shelley\n', '"The Holy Bible: King James Version"\n', '"The Color Purple" by Alice Walker\n', '"The Count of Monte Cristo" by Alexandre Dumas\n', '"A Tree Grows in Brooklyn" by Betty Smith\n', '"East of Eden" by John Steinbeck\n', '"Alice in Wonderland" by Lewis Carroll\n', '"In Cold Blood" by Truman Capote\n', '"Catch-22" by Joseph Heller\n', '"The Stand" by Stephen King\n', '"Outlander" by Diana Gabaldon\n', '"Harry Potter and the Prisoner of Azkaban" by J.K. Rowling\n', '"Enders Game" by Orson Scott Card\n', '"Anna Karenina" by Leo Tolstoy\n', '"Watership Down" by Richard Adams\n', '"Memoirs of a Geisha" by Arthur Golden\n', '"Rebecca" by Daphne du Maurier\n', '"A Game of Thrones" by George R.R. Martin\n', '"Great Expectations" by Charles Dickens\n', '"The Old Man and the Sea" by Ernest Hemingway\n', '"The Adventures of Sherlock Holmes" (#3) by Arthur Conan Doyle\n', '"Les Misérables" by Victor Hugo\n', '"Harry Potter and the Half-Blood Prince" by J.K. Rowling\n', '"Life of Pi" by Yann Martel\n', '"The Scarlet Letter" by Nathaniel Hawthorne\n', '"Celebrating Silence: Excerpts from Five Years of Weekly Knowledge" by Sri Sri Ravi Shankar\n', '"The Chronicles of Narnia" by C.S. Lewis\n', '"The Pillars of the Earth" by Ken Follett\n', '"Catching Fire" by Suzanne Collins\n', '"Charlie and the Chocolate Factory" by Roald Dahl\n', '"Dracula" by Bram Stoker\n', '"The Princess Bride" by William Goldman\n', '"Water for Elephants" by Sara Gruen\n', '"The Raven" by Edgar Allan Poe\n', '"The Secret Life of Bees" by Sue Monk Kidd\n', '"The Poisonwood Bible: A Novel" by Barbara Kingsolver\n', '"One Hundred Years of Solitude" by Gabriel Garcí\xada Márquez\n', '"The Time Traveler\'s Wife" by Audrey Niffenegger\n', '"The Odyssey" by Homer\n', '"The Good Earth (House of Earth #1)" by Pearl S. Buck\n', '"Mockingjay (Hunger Games #3)" by Suzanne Collins\n', '"And Then There Were None" by Agatha Christie\n', '"The Thorn Birds" by Colleen McCullough\n', '"A Prayer for Owen Meany" by John Irving\n', '"The Glass Castle" by Jeannette Walls\n', '"The Immortal Life of Henrietta Lacks" by Rebecca Skloot\n', '"Crime and Punishment" by Fyodor Dostoyevsky\n', '"The Road" by Cormac McCarthy\n', '"The Things They Carried" by Tim O\'Brien\n', '"Siddhartha" by Hermann Hesse\n', '"Beloved" by Toni Morrison\n', '"Slaughterhouse-Five" by Kurt Vonnegut\n', '"Cutting For Stone" by Abraham Verghese\n', '"The Phantom Tollbooth" by Norton Juster\n', '"The Brothers Karamazov" by Fyodor Dostoyevsky\n', '"The Story of My Life" by Helen Keller']
otherlist = sorted(lst)
print(otherlist)
j = open("books.txt")
print(type(j))
# lst = [i for i in j if i != 0]
print(lst)