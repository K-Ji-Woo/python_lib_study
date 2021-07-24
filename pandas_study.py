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