## 문제 1 아이디 추천 
# 문자열 맨 뒤에 거를 제외하고 나머지를 배열에 넣을 때 
        elif new_id[-1] == '.':
            new_id = new_id[: len(new_id) -1]

# 처음 했던 방법 
new_id = new_id[: -1]

# 차이점
# 배열은 0 부터 시작하여 전체 길이에서 -1 을 빼서 가져가야 길이 범위를 벗어나지 않는다? 

## 문제 2 영어 숫자 치환
def solution(s):
    
    string = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'};
    for i, j in string.items():
        s = s.replace(i,j)
    
    
    answer = int(s)
    return answer

# 딕셔너리로 key value 값을 주면 쉽게 치환 가능.
# 되도록 키, 값 쌍이면 딕셔너리로 지정해줄것. items(), keys() 잘 활용해서 뽑기
# 단점 노가다 필요
# key 값만 주고 value 는 for 문 돌려서 주는 법 ???

# a.rjsut(n,'0') 문자열 맨 앞이 공백일 경우 0으로 채워준다