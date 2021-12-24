# 책방에서 관리할 책에 대해 표현하는 클래스

class Book:
    # 책의 정보 (변수)가 어떤것들이 있는지를 별도로 명시하지 않는다.
    # 메쏘드 (+ 생성자) 에서 객체에 달린 변수로 정의함.
    
    # 책의 하위 정보 (제목, 대여료, 연령제한(나이)) => 변수로 명시하지 않는다.
    
    # 책의 데이터들을 세팅하는 기능 - 메쏘드 : set_data
    
    def set_data( self, title, rent_fee, limit_age ):
        # self : 어떤 책을 다룰지, 인스턴스를 가리킴.
        # self 변수의, 하위 정보들을 세팅해주자.
        
        # 파이썬의 변수 : 변수이름 = 자료  => 변수 생성/대입 자동 진행.
        
        self.t = title  # 책 한권의 t 변수에 => title에 적힌 값 기록.
        self.rf = rent_fee
        self.la = limit_age
        
        main_title = '임시 제목'
        
    # 책의 정보를 출력하는 기능.
    def print_book_info(self):  # 파라미터 필요 없다.
        print('===== 도서 정보 출력 =====')
        print(f'제목 : {self.t}')  # 명령을 시킨 책의 제목에 접근
        print(f'대여료 : {self.rf}')
        
        # self.la 에 담긴 값에 따라 -> 다르게 출력 (if 활용)
        if self.la == 0:
            print(f'연령제한 : 전체 이용가')
        else:
            print(f'연령제한 : {self.la}세 이용가')
            
    # 어떤 사람의 출생년도를 파라미터로 받아서, 대여 가능 여부를 판단해주는 메쏘드.
    def is_rent_available(self, birth_year):
        # 문제풀이 하는 방식으로 코드 작성.
        age = 2021 - birth_year + 1
        
        if age >= self.la:
            print('대여 가능합니다.')
        else:
            print('나이가 어려서 대여 불가능합니다.')