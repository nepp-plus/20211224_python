from book import Book # book.py 파일안에서 => Book 클래스를 main.py에 가져오기.
# 만들어둔 클래스들을 활용해서 실제 동작 관련 코드 작성

# 책의 인스턴스 하나를 생성. + 변수에 담아두자.
book1 = Book()

# 방금 만든 책의 데이터 설정. (타짜, 700, 19)

# set_date 메쏘드의 self 파라미터에는 => book1이 대입됨.
book1.set_data('타짜', 700, 19)  # 전달인자(arguments)들을, self 파라미터만 제외하고 작성.

book1.print_book_info()

