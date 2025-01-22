import numpy as np
import pandas as pd
import Library_of_defasification_functions 

def PDA_NDA(matrix, n, m, AV):

    for i in range(n):

        for j in range(m): 

            if matrix[i][j] > 0:
                PDA = np.maximum(0, (matrix - AV) / AV)
                NDA = np.maximum(0, (AV - matrix) / AV)
            else:
                PDA = np.maximum(0, (AV - matrix) / AV)
                NDA = np.maximum(0, (matrix - AV) / AV)

    return PDA, NDA 

percent_rubles = []
percent_currency = []
expert_estimates = []
bank_reliability_ratings = []
Expert_Estimates = []
Bank_Reliability_Ratings = []
matrix = []
income_rubles = []

deposit_amount = float(input("Enter the deposit amount:"))

rate = float(input("Enter the exchange rate against the ruble:"))

banks = int(input("Enter the number of banks:"))

print("Enter the interest rates on deposits in rubles")
for i in range(banks):
    percent_rubles.append(float(input()))

print("Enter the interest rates on deposits in the currency")
for i in range(banks):
    percent_currency.append(float(input()))

row_1 = int(input("Enter the number of experts:"))
print("Enter expert estimates in the form of a triangular number along by row")
for i in range(row_1):      
   a =[]  
   for j in range(3):      
      a.append(float(input()))
   expert_estimates.append(a) 

print("Enter bank reliability ratings in the form of a triangular number along the row")
for i in range(banks):      
   a =[]  
   for j in range(3):      
      a.append(float(input()))
   bank_reliability_ratings.append(a) 

# Увеличиваем наименьший массив (Increasing the smallest array)
if row_1 < banks:
    r = row_1
    i = 0
    while row_1 < banks:
        expert_estimates = np.append(expert_estimates, expert_estimates[i : :], 0)
        row_1 += 1
        i += 1
        row = row_1
        if i + 1 == r:
            i = 0
elif banks < row_1:
    R = banks
    r = banks
    i = 0
    while R < row_1:
        bank_reliability_ratings = np.append(bank_reliability_ratings, bank_reliability_ratings[i : :], 0)
        R += 1
        i += 1
        row = R
        if i + 1 == r:
            i = 0
else:
    row = banks


# Выбор метода дефаззификации (Choosing a defuzzification method)
method = input("Which method do you want to use? Input example: Adamo, CofMax, CofMass, Medians, Chang, PAv, Jager, USt1. ")
for i in range(row):
    if method == 'Adamo':
        E, B = Library_of_defasification_functions.Adamo(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    elif method == 'CofMax':
        E, B = Library_of_defasification_functions.CofMax(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    elif method == 'CofMass':
        E, B = Library_of_defasification_functions.CofMass(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    elif method == 'Medians':
        E, B = Library_of_defasification_functions.Medians(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    elif method == 'Chang':
        E, B = Library_of_defasification_functions.Chang(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    elif method == 'PAv':
        E, B = Library_of_defasification_functions.PAv(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    elif method == 'Jager':
        E, B = Library_of_defasification_functions.Jager(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    else:
        E, B = Library_of_defasification_functions.USt1(expert_estimates[i][0], expert_estimates[i][1], expert_estimates[i][2], bank_reliability_ratings[i][0], bank_reliability_ratings[i][1], bank_reliability_ratings[i][2])
    Expert_Estimates.append(E) 
    Bank_Reliability_Ratings.append(B) 

for i in range(banks):
    income_rubles.append(deposit_amount * (1 + percent_rubles[i] / 100))

# Построение матрицы принятия решений (Building a decision matrix)
r = 0
m = 0
for i in range(banks * 2):
    matrix.append([])
    for j in range(banks):
        if i % 2 == 0:
            matrix[i].append(income_rubles[m])
        else:
            matrix[i].append((deposit_amount / rate) * (1 + percent_currency[m] / 100) * Expert_Estimates[j])
    matrix[i].append(Bank_Reliability_Ratings[m])
    if r == 1:
        r = -1
        m += 1
    r +=1

# Определение среднего решения по всем критериям (Determination of the average solution by all criteria)
n = len(matrix)
AV = np.sum(matrix, axis = 0) / n

# Рассчет положительного расстояния от среднего (PDA) и отрицательного расстояния от среднего (NDA) матриц в соответствии с типом критериев
# Calculation of the positive distance from the mean (PDA) and negative distance from the mean (NDA) of matrices according to the type of criteria
PDA, NDA = PDA_NDA(matrix, banks * 2, banks, AV)

# Определение взвешенной суммы PDA и NDA для всех альтернатив
# Determining the weighted sum of PDA and NDA for all alternatives
omega = 1   # Вес (Weight)
SP = np.sum(omega * PDA, axis = 1)
SN = np.sum(omega * NDA, axis = 1)

# Нормализовать значения SP и SN для всех альтернатив
# Normalize SP and SN values for all alternatives
maxSP = np.amax(SP)
maxSN = np.amax(SN)

NSP = SP / maxSP
NSN = 1 - (SN / maxSN)

# Рассчет оценки (AS) для всех альтернатив (Estimation calculation (AS) for all alternatives)
AS = (NSP + NSN) / 2
#np.set_printoptions(precision=3)    # Устанавливает точность вывода (Sets the output accuracy)

# Ранжирование альтернатив в соответствии с убывающими значениями оценочного балла (AS).
# Ranking of alternatives according to decreasing values of the evaluation score (AS).
ind = np.arange(1, banks * 2 + 1)
s = pd.Series(AS, index=ind)

sorted_df = s.sort_values(ascending=False) 
# Альтернатива с наивысшим AS - лучший выбор среди возможных альтернатив.
# The alternative with the highest AS is the best choice among possible alternatives.
print('Result: \n', sorted_df)
