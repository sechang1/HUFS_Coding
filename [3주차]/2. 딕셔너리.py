# 서술형 문제

# 오류가 발생하는 이유는 딕셔너리의 키로는 변하는(mutable) 값을 사용할 수 없기 때문이다. 
# 위 예에서 키로 사용된 [1]은 리스트이므로 변하는 값이다. 다른 예에서 키로 사용된 문자열, 튜플, 숫자는 변하지 않는(immutable) 값이므로 딕셔너리의 키로 사용이 가능하다.
