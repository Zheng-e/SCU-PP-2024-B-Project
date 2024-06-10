from library import Library
from borrow_return import BorrowReturn

def main():
    library = Library()
    br_system = BorrowReturn(library)
    
    while True:
        print("1. 添加书籍")
        print("2. 查看所有书籍")
        print("3. 搜索书籍")
        print("4. 借书")
        print("5. 还书")
        print("6. 退出")
        
        choice = input("请选择操作: ")
        
        if choice == '1':
            title = input("书名: ")
            author = input("作者: ")
            isbn = input("ISBN: ")
            quantity = int(input("数量: "))
            library.add_book(title, author, isbn, quantity)
        elif choice == '2':
            for book in library.view_books():
                print(book)
        elif choice == '3':
            keyword = input("请输入书名或作者: ")
            results = library.search_books(keyword)
            for book in results:
                print(book)
        elif choice == '4':
            isbn = input("请输入ISBN: ")
            print(br_system.borrow_book(isbn))
        elif choice == '5':
            isbn = input("请输入ISBN: ")
            print(br_system.return_book(isbn))
        elif choice == '6':
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()