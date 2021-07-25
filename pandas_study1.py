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


# 인덱스 및 칼럼명 추가 방법(DataFrame 객체 생성할 때 파라미터로 넣어주는 방법도 있음)
sample_df.index = ['a', 'b', 'c', 'd']
sample_df.columns = ['이름', '점수', '평가등급']
print('\n인덱스와 칼럼명 추가\n', sample_df)
print(sample_df.index) 
print(sample_df.columns) 


# DataFrame의 데이터 살펴보기
print("\n데이터 살펴보기")
print('\n전반적인 정보 제공\n', sample_df.info())
print('\n.head()\n', sample_df.head(2)) # defualt값은 5
print('\n.tail()\n', sample_df.tail(3)) # defualt값은 5
print('\n.sample()\n', sample_df.sample(2)) 


# 수치형과 범주형 데이터
# 수치형데이터 : 관측된 값이 연속적으로 측정된 데이터 / 산술적인 연산(평군, 중앙값, 표준편차 등)이 의미가 있음
# 범주형 데이터 : 범주나 항목으로 표현할 수 있는 데이터 / 수치적인 의미 x / 범주의 종류나 빈도수로 접근
score = {'name': ['Jessi', 'Emma', 'Alex', 'Jessi', 'Tom'],
         'age': [20, 24, 23, 20, 27],
         'score': [100, 95, 80, 85, 97],
         'grade': ['A', 'A', 'B', 'B', 'A'],
         'subject':['python', 'java', 'python', 'c', 'java']}

df = pd.DataFrame(data=score)

# df.describe() : 수치형 데이터의 기술통계, 범주형 데이터의 빈도수 관련 정보 반환 / defualt -> 수치형 데이터만 알아서 파악
print('\n수치형 데이터 describe()\n', df.describe())
print('\n범주형 데이터 describe()\n', df[['name','grade', 'subject']].describe())
print('\n모든 열에 대한 describe()\n', df.describe(include='all'))

# df.unque() : 범주형 데이터의 고유한 종류 반환
print('\ndf.uniqe()')
print(df['name'].unique())
# df.value_counts() : 범주형 데이터의 각 항목의 빈도수 반환 / 인자로 normalize=True : 비율 반환
print('\ndf.value_counts()')
print(df['grade'].value_counts())
print(df['grade'].value_counts(normalize=True))







