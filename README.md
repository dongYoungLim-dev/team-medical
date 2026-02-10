# Team Study Medical Data start


# CH04, CH05

> 26.02.10 Study Mission

CH04 : 데이터 추출, 데이터 정렬 학습
CH05 : 데이터 전처리, 파생 변수 학습

데이터 : cursor agent 를 이용하여 각 챕터에 필요한 더미 데이터 생성
> 

---

### 조건 필터링

DataFrame은 열에 접근을 할때 조건문을 이용하여 데이터를 추출 할 수 있다.

```python
result_11 = df[(df['나이'] >= 30) & (df['성별'] == '여') & (df['혈압'] >= 130)]
# []안 조건 문에 해당하는 행 데이터 추출 가능.

'''
# 결과 데이터
    이름  나이 성별   혈압   혈당  진단명
1  이영희  32  여  135  105  고혈압
3  최지영  45  여  142  155   당뇨
6  윤미라  72  여  138  180   당뇨
'''

```

---

### 정렬

Pandas DataFrame 메서드중 “sort_values” 메서드 이용 

sort_values : 특정 열(column) 값 기준으로 정렬할때 쓰이는 메소드

```python
df.sort_values(by='혈당', ascending=False)

# by : 정렬 기준이 되는 열 이름
# ascending : 오름 차순(True), 내림 차순(False) 
```

---

### 특정 열만 뽑기

Pandas DataFrame 는 열(column) 데이터를 추출 하기 위해서 `df['column name']` 처럼 작성하여 데이터를 추출한다. (만약, 여러 열의 데이터를 한번에 뽑고 싶으면 ‘column name’ 에 list 를 전달하면 된다.)

```python
# 여러 열 데이터 추출하기
df[['이름', '진단명']]

# 결과 

'''
    이름     진단명
0  김철수      정상
1  이영희     고혈압
2  박민수      정상
3  최지영      당뇨
4  정수진      정상
5  한대호  고혈압+당뇨
6  윤미라      당뇨
7  강동욱     고혈압
8  임소연      정상
9  조현우  고혈압+당뇨
'''
```

---

### 결측치 처리

1. 평균값 삽입

```python
result_15_1 = df['혈압'].fillna(df['혈압'].mean())
# fillna 로 결측치를 만나면, df['혈압'].mean() 으로 혈압의 평균을 내어 그 값을 삽입
```

1. 행 제거

```python
result_15_2 = df['혈압'].dropna()
# '혈압' 열에 결측치가 발견되면 데이터가 없는 '행' 제거
```

1. null 채우기

```python
# fillna 를 이용하여 'null'로 채운다.
df['혈압'].fillna('null')
```

---

### BMI 자동화

BMI 계산 수식 : `BMI = 몸무게(kg) / (키(cm)/100)²  → 키는 cm이므로 100으로 나눠서 m로 변환` 

```python
def calculate_bmi(height, weight):
  # pandas의 결측치는 None이 아니라 NaN이므로 pd.isna() 또는 pd.isnull() 사용
  if pd.isna(height) or pd.isna(weight):
    return 0
  return weight / ((height / 100) ** 2) 

# apply -> 행 또는 열에 함수를 적용시켜 새 Series 또는 DataFrame 반환 메서드
# axis -> 0(default): 열(column), 1: 행(row)
df_bmi['BMI'] = df_bmi.apply(lambda row: calculate_bmi(row['Height'], row['Weight']), axis=1)

# lambda 를 이용 행단위로 row 한개씩 calculate_bmi 함수로 전달.
```
