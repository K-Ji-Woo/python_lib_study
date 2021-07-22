import numpy as np

# numpy version 확인
print(np.__version__)


# ndarray 생성 : np.arage(), np.zeros(), np.ones(), np.full(), np.empty() ... 등 
# 다른 ndarray와 동일한 형태를 가진 새로운 ndarray를 만드는 np.**_like()도 있음(**에는 zeros, ones 등)
# ndarray.reshape(@, @) : 인자로 넣은 형태로 ndarray 형태 변환
sample_array = np.arange(10).reshape(-1, 2)


# ndarray의 구성요소
print(sample_array.shape) # 형태
print(sample_array.size) # 원소의 수
print(sample_array.dtype) # 저장된 데이터 타입
print(sample_array.ndim) # 배열의 축(차원) 수