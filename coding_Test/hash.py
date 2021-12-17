# 마라톤 완주 
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant,completion ) :
        if p != c :
            return p

    return participant.pop()


   # zip : 배열을 같은 길이의 리스트를 같은 인덱스 끼리 잘라서 리스트로 반환해 준다.
   # 만약 배열의 길이가 다를 경우 같은 인덱스끼리만 짝지어주고, 
   # zip 객체에서 나머지 인덱스는 제외된다
   # zip은 함수안의 리스트, 튜플, 문자열에 대하여 각 요소를 짝지어 준다.


   # find(찾을문자, 찾기시작할위치) 문자열이 완전히 일치 해야 한다.
   # 문자열을 찾으면 위치를 반환해 주며, 찾으려는 문자열이 없으면 -1을 반환한다.

   # startswith(시작하는문자, 시작지점)
   # true 나 false를 반환한다.

   # 응용 사용법 : s.startswith('마',s.find('마')) 
   # #find는 '마' 의 시작지점을 알려줌 : 5

   # endswith(끝나는문자, 문자열의시작, 문자열의끝)



# 전화번호부 비교

       for p1, p2 in zip(phone_book, phone_book [1:]) : # 한 배열에서 자기 스스로 비교를 하려고 할때 
        if p2.startswith(p1) :
            return False
    return True



# 위장 
    # 같은 종류의 옷끼리 묶어서 사전에 저장   {'bluesunglass' : 'face', 'blacksunglass' : 'face', 'bluejean' : 'jean'} 식의 딕셔너리로 생김.
    for cloth in clothes:
        if cloth[1] in closet.keys():  # cloth[1] : 'face', 'jean' , 'hat' 들을 key 로 만들어줌
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    
    # 경우의 수 구하기            
    for value in closet.values():  # 5가지 종류( 머리 2종, 하의 1종 상의 1종, 코트 3종, 악세서리 5종) 이라면 각 종류의 갯수를 모두 곱하고 전체 입는 경우의 수도 포함.
        answer *= len(value) + 1
    
    # 아무것도 입지 않은 경우 하나 제외
    return answer-1