import pandas as pd

class Group(): 
    def __init__(self, dfM, title="Unnamed Group", SOC_Start=0, SOC_End=53+1, collar="none"):
        self.df = dfM.loc[(dfM['SOC_CODE']/10000).between(SOC_Start, SOC_End+1, inclusive='both')]
        if collar == 'white':
            self.df = (self.df.loc[(self.df['SOC_CODE']%10000).between(0, 2299, inclusive='both')])
            self.title = "White Collar"
        elif collar == 'blue':
            self.df = (self.df.loc[(self.df['SOC_CODE']%10000).between(3300, 9999, inclusive='both')])
            self.title = "Blue Collar"
        self.title = title

    
    def weightedMeanProb(self):
        return (self.df['Probability']*self.df['TOT_EMP']).sum() / self.df['TOT_EMP'].sum()
    
    def weightedMeanSallary(self):
        return (self.df['A_MEAN']*self.df['TOT_EMP']).sum() / self.df['TOT_EMP'].sum()
    
    def getTitle(self):
        return self.title
    # def getSOC_Range(self):
    #     return (self.SOC_Start, self.SOC_End)
    def getDF(self):
        return self.df
    
txt_file = open('Data/SOC_AGGREGATIONS.txt')

def aggregate(df, level): 
    groups = []
    levelFound = False
    for line in txt_file:
        if levelFound: 
            if line != '' and line != '\n':
                if '-' in line:
                    start = line[:line.index('-')] #Start SOC Range
                    end = line[line.index('-')+1:line.index(' ')] #End SOC Range
                else:
                    start = end = line[:line.index(' ')]
                title = line[line.index(' ')+1:] #Group Title
                groups.append(Group(df, title=title, SOC_Start=int(start), SOC_End=int(end)))
            else:
                return groups
        elif line == level.upper() or line == level.upper()+':\n':
            levelFound = True    
    raise Exception("Aggregation Level Specified Does Not Exist")

def weightedMeanProbs(df, ordered):
    l = []
    for state in ordered:
        l.append((df['Probability']*df[state]).sum() / df[state].sum())
    return l

def probability(df, thresheholdProb):
    return df.loc[df['Probability'] >= thresheholdProb]

def sortCollar(df):
    white = Group(df, title="White Collar Occupations", collar='white')
    blue = Group(df, title="Blue Collar Occupations", collar='blue')
    return [white, blue]