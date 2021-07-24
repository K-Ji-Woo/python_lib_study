import numpy as np

# numpy version 확인
print("버전 확인")
print(np.__version__)


# ndarray 생성 : np.arage(), np.zeros(), np.ones(), np.full(), np.empty() ... 등 
# 다른 ndarray와 동일한 형태를 가진 새로운 ndarray를 만드는 np.**_like()도 있음(**에는 zeros, ones 등)
# ndarray.reshape(@, @) : 인자로 넣은 형태로 ndarray 형태 변환
print("\nndarray 생성")
sample_array = np.arange(10).reshape(-1, 2)


# ndarray의 구성요소
print("\n기본 구성 요소")
print(sample_array.shape) # 형태
print(sample_array.size) # 원소의 수
print(sample_array.dtype) # 저장된 데이터 타입
print(sample_array.ndim) # 배열의 축(차원) 수


# 데이터 타입 변경 : ndarray.astype(type)
print("\n데이터 타입 변경")
new_arr = sample_array.astype(str)


# 기본 연산(연산기호 사용하거나 함수 사용하거나) => 모든 연산은 배열의 각 요소별로 적용됨
# 비교연산자를 넣으면 True False값 반환
print("\n기본연산과 비교연산")
a = np.arange(1, 13).reshape(2, 2, 3)
b = np.arange(12, 0, -1).reshape(2, 2, 3)
print(a + b)
print(np.add(a,b))
print('--------------------------------------')
print(a - b)
print(np.subtract(a, b))


# 집계함수 (집계 방향이 매우 중요!!)
# 집계방향(axis = default | 1 | 2 | 3 | ...)
# axis = defaul면 모든 요소를 연산 대상으로 설정
print("\n집계함수 / aixs를 변경하며 확인해보기")
print("\n원본 a 배열\n", a)
print(np.sum(a))
print(np.mean(a))
print(a.std()) 
print(a.max())
print(a.min())





