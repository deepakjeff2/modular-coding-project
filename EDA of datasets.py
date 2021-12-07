import pandas as pd
import scipy.stats as stats
import numpy as np

class numerical_treatment:
    def __init__(self,dataframe):
        self.dataframe = dataframe
    # this is the function for numerical treatment
    def num_df(self):
        null_column = []
        outliers_col = []
        # to seperate numerical columns
        numerical_columns = self.dataframe.select_dtypes(include = ['int64','float64']).columns
        for column in numerical_columns:
            #to check the null values column
            if self.null_checker(column):
                null_column.append(column)

        for column in null_column:
            #to check outliers column in null columns
            if self.outliers_check(column):
                outliers_col.append(column)

                #imputing with median if it has outliers
                self.median_imputation(column)
            else:
                # if it has no outliers imputing with mean
                self.mean_imputation(column)
        
        for column in outliers_col:
            #call a function to treat the outlier
            self.outlier_treatment(column)
        return self.dataframe
        
    def null_checker(self,column):
        #checking for null values
        if self.dataframe[column].isnull().sum() > 0:
            return True
        else:
            return False

    def outliers_check(self,column):
        #checking for outliers using IQR technique
        self.outliers_col = []
        IQR = self.dataframe[column].quantile(0.75) - self.dataframe[column].quantile(0.25)
        lower = self.dataframe[column].quantile(0.25) - (IQR*1.5)
        higher = self.dataframe[column].quantile(0.75) + (IQR*1.5)
        if (self.dataframe[column] < lower).any() or (self.dataframe[column] > higher).any():
            self.outliers_col.append(column)
            return True
        else:
            return False

    def median_imputation(self,column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].median())
        return self.dataframe

    def mean_imputation(self,column):
        self.dataframe[column] = self.dataframe[column].fillna(self.dataframe[column].mean())
        return self.dataframe

    def outlier_treatment(self,column):
        IQR = self.dataframe[column].quantile(0.75) - self.dataframe[column].quantile(0.25)
        lower = self.dataframe[column].quantile(0.25) - (IQR * 1.5)
        higher = self.dataframe[column].quantile(0.75) + (IQR * 1.5)
        x = np.where(self.dataframe[column] < lower,lower,self.dataframe[column])
        x = np.where(x>higher,higher,x)
        self.dataframe[column] = pd.DataFrame(x)
        return self.dataframe

