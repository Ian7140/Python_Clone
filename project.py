#list , tuple , dictionary = data structure (데이터 구조)
#0,1,2 순서의 인덱스를 가짐 / -1,-2,-3도 가능 (뒤에서 첫번째, 두번째 ...)
#list : 한 변수에 모든 값을 넣을 수 있어야함 / 대괄호 사용 / 쉼표로 구분함(mutable)
#fuction : print같은거 / method : 변수 '.' 뒤에 붙어있는 것 -> 함수를 부르는 방식이 유일한 차이점
#tuple : 대괄호말고 소괄호 사용 / 내용변경 불가능(immutable)
#dictionary : key-value 형식 / 중괄호 사용 / 사전같은 형식이라 key : value / 내용 변경 가능 (mutable)

#list
days_of_week = ["mon","tue","wed","thu","fri"]
print(days_of_week.count("wed"))

#tuple
food = ('noodle','burger','salad','chips')
print(food)

#dictionary
player={
    'name':"Ian",
    'age' : 17,
    'alive' : True,
    'fav' : ["pizza","burger"]
    }
player['fav'].append("noodle")
print(player)
