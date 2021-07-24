import pandas as pd

# pandas version 확인
print("버전 확인")
print(pd.__version__)


# Pandas의 자료구조 - Series
# 1차원 배열 구조, 한 Series에는 동일한 데이터 타입의 값을 저장 가능
# Series 생성 1
year = [2017, 2018, 2019, 2020, 2021, 2022]
sample_seires = pd.Series(year)

# index이름 및 Series 이름 설정 (.name은 Series객체 선언할 때 인자로 넣어줄 수 있음)
sample_seires.name = 'Year'
sample_seires.index.name = "No"

print("\nSeires 생성 1")
print(sample_seires)

# Series 생성 2
score = {'Kim' : 100, 'Park' : 90, 'Choi' : 93}
sample_seires = pd.Series(data=score, name='score')
sample_seires.index.name = 'f_n'
print("\nSeires 생성 2")
print(sample_seires)


# Series의 주요 속성
print('\n Series객체의 주요 속성')
print(sample_seires.index) # 인덱스 정보
print(sample_seires.index.name) # 인덱스의 이름
print(sample_seires.name) # column의 이름(한개의 열 밖에 없지만)
print(sample_seires.values) # 저장된 데이터
print(sample_seires.dtype) # 저장된 데이터의 데이터형
print(sample_seires.shape) # 객체의 형태


# Pandas의 자료구조 - DataFrame
# 2차원 자료구조(테이블 형태), 여러개의 Series가 결합된 형태, 1개의 열은 1개의 Series
# DataFrame의 생성
score = {'name': ['Jessi', 'Emma', 'Alex', 'Tom'],
         'score': [100, 95, 80, 85],
         'grade': ['A', 'A', 'B', 'B']}
sample_df = pd.DataFrame(score)
print("\nDataFrame 생성\n", sample_df)


# DataFrame의 주요 속성
print("\nDataFrame객체의 주요 속성")
print(sample_df.index) # 인덱스
print(sample_df.columns) # 칼럼
print(sample_df.values) # 저장된 데이터
print(sample_df.dtypes) # 데이터 타입
print(sample_df.shape) # 데이터 형태