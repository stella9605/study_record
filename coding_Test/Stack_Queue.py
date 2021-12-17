# 기능개발 

# Stack 의 핵심 : 구하고자 하는 배열의 전체 길이 파악부터 하는게 중요
# len(배열)의 길이를 구해놓고 index와 값을 저장하는 배열을 생성해아 한다.

# emunarate () 함수 : index 와 value 를 동시에 접근 하면서 루프를 돌릴 수 있는 내장함수
# 사용법 : for 문의 in 뒷부분에 enumerate() 를 감싸주어 사용한다. 
>>> for entry in enumerate(['A', 'B', 'C']):
...     print(entry)
...
(0, 'A')
(1, 'B')
(2, 'C') 

# start = n 으로 시작 옵션을 바꿔 줄 수 있음. 

# 응용 


# progresses 배포되어야 하는 순서대로 작업의 진도
# speeds 각 작업의 개발 속도
# progresses + speeds > = 100 return 
# dictionary에 몇 번 째인지 저장후 같은날이면 +1 을 한다.


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:  # progresses의 길이를 알고 배열에 있는 갯수만큼 while을 돌려 실행해야 한다. 
        if (progresses[0] + time*speeds[0]) >= 100:  # 100 퍼센트가 넘으면 완료된 프로그램이다. 
            progresses.pop(0)  # 전체 실행해야 하는 progresses 에서 pop 한후
            speeds.pop(0)      # 마찬가지로 해당 progresses의 speeds도 pop 한다
            count += 1         # 몇번째로 빠졌는지 체크한다. 
            
        else:
            if count > 0:      
                answer.append(count)
                count = 0
            time += 1          # 첫번째가 100이 될때까지 loop 를 돌리며 time 을 +1 씩 늘린다.  
    answer.append(count)
    return answer


# deque

보통 큐(queue) 는 선입선출 방식으로 작동하는데
데크는 양방향 큐로 작동함

양끝 방향에서 element를 추가하거나 제거할수 있으므로 append 와 pop 의 속도가 빠르다
일반적인 list 가 연산에 O(n)이 소요되지만 데크는 O(1)로 접근이 가능하다.

사용법 : 
import 를 해야 사용할 수 있다. 
from collections import deque 

deq = deque() # 짧게 쓰기 위해 

# add element to the start 
deq.appendleft(10)

# add element to the end 
deq.append(0) 

# pop element from the start 
deq.popleft()

# pop element from the end
deq.pop() 


deque 에 존재하는 대략적인 메서드 종류 

1. deque.append(item) : item을 오른쪽 끝에 삽입한다.
2. deque.appendleft(item) : item을 데크의 왼쪽 끝에 삽입한다. 

3. deque.pop() : 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.

4. deque.extend(array) : 주어진 배열을 순환하면서 데크의 오른쪽에 추가한다. 

5. deque.remove(item) : item을 데크에서 찾아 삭제한다.

6. deque.rotate(num) : 데크를 num 만큼 회전한다. (양수면 오른쪽부터, 음수면 왼쪽부터)

# deque 를 언제써야 효율적인가 ? 
# stack 처럼 사용할수도, queue 처럼 사용할 수도 있다.
# 시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는데 최적화된 연산
# deque 는 list 보다 월등히 빠르다. 또한 push/pop에서도 빠르다. 


# 프린터 
def solution(priorities, location) :
    answer = 0
    from collections import deque  # deque 를 사용하겠다는 import 

    d = deque([(v,i) for i,v in enumerate(priorities)]) # priorities 의 index와 value를 동시에 접근하며 deque를 사용하겠다는 선언

    while len(d):
        item = d.popleft() # 데크를 왼쪽부터 미리 빼놓고
        if d and max(d)[0] > item[0]: # 빼놓은 것과 데크에 있는 첫번째를 크기 비교한다. 
            d.append(item) # 빼놓은 것이 더 크다면 item에 넣어두고 
        else:
            answer += 1    # 데크에 들어있는 것이 더 크다면 ( 우선순위와 리스트에 있는것이 일치하다면 프린트 한것으로 간주한다.)
            if item[1] == location: # 프린트 한것 = 우선순위가 높은것의 위치를 출력한다. 
                break
    return answer


# 다리를 지나는 트럭 

# bridge_length 다리의 길이수, 1 키로는 1초걸림, 다리 길이가 100 이면 1키로 짜리 트럭이 건너는데 100초걸림 + 시작시간 1 = 101초 
# weight 다리가 견딜 수 있는 무게
# truck_weights 트럭별 무게

# weight > truck_weights[0] + truck_weights[1] 이면 bridge_length 은 truck_weights의 수만큼 카운트 된다. 

# weight > truck_weights
# bridge_length 트럭이 건너는데 걸리는 시간



def solution(bridge_length, weight, truck_weights):
    
    bridge = [0] * bridge_length      # 항상 배열의 전체 길이를 파악하는 것이 중요함
    time = 0
    
    while bridge : 
        time += 1                       # 다리를 건널 때 마다 시간을 추가해 주어야 한다. 몇초 걸리는지 언제 트럭이 다리를 건너는지 알아야할것
        bridge.pop(0)
        
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight :   # 다리위의 트럭의 총합 무게가 다리가 견뎌야 하는 무게보다 작아야됨. 
                bridge.append(truck_weights.pop(0))         # 다리를 건넌 트럭은 빼야됨
            else :
                bridge.append(0)                            # 다리를 안건넜을시 다리위에 있다고 남겨놓음
    return time