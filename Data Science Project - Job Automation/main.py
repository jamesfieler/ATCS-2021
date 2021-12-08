import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sorting

df1 = pd.read_csv('Data/job_data.csv').dropna() #df1 = JOB_DATA
df2 = pd.read_csv('Data/state_data.csv').dropna() #df2 = STATE_DATA

df1['SOC_CODE'] = df1['SOC_CODE'].astype(int)
df2['SOC_CODE'] = df2['SOC_CODE'].astype(int)

df1['OCC_TITLE'] = df1['OCC_TITLE'].astype(str)
df1['A_MEAN'] = df1['A_MEAN'].astype(int)

dfM = pd.merge(df1, df2, how="inner", on="SOC_CODE")
dfM['TOT_EMP'] = dfM.iloc[:, 4:].sum(axis=1)

dfM.to_csv("Data/MASTER.csv", index=False)

#print(sort.probability(dfM, 0.9))
print("*** WEIGHTED MEAN PROBABILITY OF AUTOMATION: " + str((dfM['Probability']*dfM['TOT_EMP']).sum() / dfM['TOT_EMP'].sum()) + " ***")


x = dfM['A_MEAN']
y = dfM["Probability"]
m, b = np.polyfit(x, y, 1)
correlation = y.corr(x)
print("CORRELATION [Figure 1]: " + str(correlation))

plt.title("Occupation Mean Annual Sallary and Probability of Automation")
plt.xlabel("Mean Annual Sallary")
plt.ylabel("Automaiton Probability")
plt.scatter(x, y, alpha = 0.5)
plt.plot(x, m*x + b, color = 'red') #linnear regression - GET RID OF NEGATIVE!!
plt.show()
plt.clf()



dfU = pd.read_csv('Data/urbanization_data.csv')
dfU = dfU.sort_values(by='Urbanization_Percentage',ascending=True)
x = list(dfU['States'])  
y = sorting.weightedMeanProbs(dfM.iloc[:, 3:55], x)

plt.title("State and Occupation Weighted Mean Automation Probability")
plt.xlabel("District Ordered By Urbanization (Ascending)")
plt.ylabel("Weighted Mean Automation Probability")
plt.bar(x, y)
plt.show()
plt.clf()



barTitles = []
i = 1
groupTitles = []
groupWeightedProbs = []
key = {}
for group in sorting.aggregate(dfM, 'high'):
    groupWeightedProbs.append(group.weightedMeanProb())
    groupTitles.append(group.getTitle())
    barTitles.append(i)
    key[barTitles[i-1]] = groupTitles[i-1]
    i += 1
x = barTitles
y = groupWeightedProbs

for i in key:
    print(str(i) + ": " + key[i])
plt.title("Job Aggregation and Weighted Mean Automation Probability")
plt.xlabel("Job Aggregation")
plt.ylabel("Weighted Mean Automation Probability")
plt.bar(x, y)
plt.show()
plt.clf()



barTitles = []
i = 1
groupTitles = []
groupWeightedProbs = []
key = {}

for group in sorting.aggregate(dfM, 'major'):
    groupTitles.append(group.getTitle())
    groupWeightedProbs.append(group.weightedMeanProb())
    barTitles.append(i)
    key[barTitles[i-1]] = groupTitles[i-1]
    i += 1
    
x = barTitles
y = groupWeightedProbs

for i in key:
    print(str(i) + ": " + key[i])
plt.title("Job Aggregation and Weighted Mean Automation Probability")
plt.xlabel("Job Aggregation")
plt.ylabel("Weighted Mean Automation Probability")
plt.bar(x, y)
plt.show()
plt.clf()



bwCollar = sorting.sortCollar(dfM) #white, blue
bwCollarProbs = [bwCollar[0].weightedMeanProb(), bwCollar[1].weightedMeanProb()]
bwCollarTitles = [bwCollar[0].getTitle(), bwCollar[1].getTitle()]

plt.title("Blue vs White Collar Automation Probability")
plt.bar(bwCollarTitles, bwCollarProbs)
plt.xlabel("White vs Blue Collar")
plt.ylabel("Weighted Mean Automation Probability")
#plt.pie(bwCollarProbs)
plt.show()