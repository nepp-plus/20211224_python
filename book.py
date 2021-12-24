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