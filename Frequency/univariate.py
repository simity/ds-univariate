class univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            print (columnName)
            if (dataset[columnName].dtypes=="O"):
                print("qual")
                qual.append(columnName)
            else:
                print("quan")
                quan.append(columnName)
        return quan,qual
    
    def descriptive(dataset,quan):
    descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max","Kurtosis","Skew"],columns=quan)
    for columnName in quan:
        descriptive[columnName]["Mean"]=dataset[columnName].mean()
        descriptive[columnName]["Median"]=dataset[columnName].median()
        descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
        descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
        descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
        descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
        descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
        descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
        descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
        descriptive[columnName]["1.5Rule"]=1.5*descriptive[columnName]["IQR"]
        descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5Rule"]
        descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5Rule"]
        descriptive[columnName]["Min"]=dataset[columnName].min()
        descriptive[columnName]["Max"]=dataset[columnName].max()
        descriptive[columnName]["Kurtosis"]=dataset[columnName].kurtosis()
        descriptive[columnName]["Skew"]=dataset[columnName].skew()
    return descriptive

    desc_stats=descriptive(dataset,quan)
    def outliers(desc_stats,quan):
        lesser=[]
        greater=[]
        for columnName in quan:
            if (desc_stats.at["Min",columnName]<desc_stats.at["Lesser",columnName]):
                lesser.append(columnName)
            if (desc_stats.at["Max",columnName]>desc_stats.at["Greater",columnName]):
                greater.append(columnName)
        return lesser,greater
        
        
        def freqTable(dataset,columnName):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","Cumsum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumsum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable
    