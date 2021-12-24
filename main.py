from book import Book # book.py 파일안에서 => Book 클래스를 main.py에 가져오기.
# 만들어둔 클래스들을 활용해서 실제 동작 관련 코드 작성

# 책의 인스턴스 하나를 생성. + 변수에 담아두자.
book1 = Book()

# 방금 만든 책의 데이터 설정. (타짜, 700, 19)

# set_date 메쏘드의 self 파라미터에는 => book1이 대입됨.
book1.set_data('타짜', 700, 19)  # 전달인자(arguments)들을, self 파라미터만 제외하고 작성.

book1.print_book_info()


# 두번째 책의 인스턴스를 추가로 생성.
book2 = Book()

# 두번째 책의 데이터 설정. (드래곤볼, 1000, 15)
book2.set_data('드래곤볼', 1000, 15)

# 두번째 책의 정보 출력
book2.print_book_info()

# 연습문제. 연령제한이 0 => 그때는 전체 이용가로 나타나도록.
# 연령제한이 그 외의 숫자 => ~세 이용가로 나타나도록.
book3 = Book()
book3.set_data('뽀로로', 500, 0)
book3.print_book_info()


test02 = '테스트 변수'

# 함수와의 비교를 위한 예시 코드.
def add_and_print(num1, num2):
    print(num1 + num2)
    print(test02)
    
    test = 10
    

add_and_print(5, 11)


book1.is_rent_available( 2000 )


num = 10

if num > 5:
    result = '5보다 크다.'
    
print(result)