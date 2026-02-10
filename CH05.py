# Team Study CH05 
'''
### CH05 (망가진 데이터 고치기 (전처리 & 파생변수))
**No.15 결측치 처리 (`isnull`, `fillna`):** 비어있는 혈압 데이터를 '평균값'으로 채우거나, 데이터가 없는 행을 지우기(`dropna`).
**No.16 파생변수 만들기:** 키(Height)와 몸무게(Weight) 컬럼을 이용해 **'BMI'** 컬럼을 새로 만들어 표에 붙이기.
**No.17 미션: "BMI 자동 계산기"**
  - 키(cm)와 몸무게(kg) 데이터가 있는 표를 만들고, 코드로 계산하여 맨 오른쪽 열에 `BMI` 수치를 자동으로 채워 넣으세요. (결측치가 있다면 0으로 채우세요!)
'''

import pandas as pd

# 더미 데이터 생성 (결측치 포함)
data = {
    '이름': ['김철수', '이영희', '박민수', '최지영', '정수진', '한대호', '윤미라', '강동욱', '임소연', '조현우'],
    '나이': [35, 32, 28, 45, 38, 65, 72, 58, 42, 68],
    '성별': ['남', '여', '남', '여', '여', '남', '여', '남', '여', '남'],
    '혈압': [125, 135, None, 142, 128, 150, None, 145, 120, 160],  # 결측치 포함
    '혈당': [95, 105, 88, 155, 98, 165, 180, 142, 110, 195],
    'Height': [175, 162, 180, 158, 165, 170, 155, 178, 160, 172],  # 키 (cm)
    'Weight': [75, 58, 82, 65, 62, 78, 55, 85, 60, 80]  # 몸무게 (kg)
}

df = pd.DataFrame(data)

# No.15 결측치 처리 - 평균값
result_15_1 = df['혈압'].fillna(df['혈압'].mean())
print(result_15_1)

# No.15 결측치 처리 - 데이터가 없는 행 제거
result_15_2 = df['혈압'].dropna()
print(result_15_2)

# No.15 결측치 처리 - 결측을 문자열 'null'로 채우기
result_15_3 = df['혈압'].fillna('null')  # 잘못된 예: .isnull().fillna('null') → bool 시리즈가 됨
print(result_15_3)


# No.16 파생변수 만들기 - BMI 계산 후 표에 붙이기
# BMI = 몸무게(kg) / 키(m)²  → 키는 cm이므로 100으로 나눠서 m로 변환
df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)
print(df)

# No.17 미션: "BMI 자동 계산기"
# 키(cm)와 몸무게(kg) 데이터가 있는 더미 데이터를 생성하세요. (결측치 포함)
bmi_data = {
    '이름': ['홍길동', '김영희', '이철수', '박미영', '최진수'],
    'Height': [175, 160, 168, None, 155],
    'Weight': [70, None, 60, 48, 50]
}

df_bmi = pd.DataFrame(bmi_data)


def calculate_bmi(height, weight):
  # pandas의 결측치는 None이 아니라 NaN이므로 pd.isna() 또는 pd.isnull() 사용
  if pd.isna(height) or pd.isna(weight):
    return 0
  return weight / ((height / 100) ** 2) 

df_bmi['BMI'] = df_bmi.apply(lambda row: calculate_bmi(row['Height'], row['Weight']), axis=1)

# df_bmi['BMI'] = calculate_bmi(df['Height'].fillna(0), df['Weight'].fillna(0))
print(df_bmi)