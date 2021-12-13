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
class categorical_imputation(numerical_treatment):
    def cat_df(self):
        null_cols = []
        cat_cols = []
        class_count=0
        # to classifing the columns into catogerical columns
        cat_cols = self.catogerical_columns()

        # to check the number class in the column
        for column in cat_cols:
            if self.check_null(column):
                null_cols.append(column)
        for column in null_cols:
            self.dataframe[column] = self.mode_imputation(column)
        
        for column in cat_cols:
            class_count = self.check_class(column)
            if class_count <2:
                self.dataframe = self.one_hot_encoding(column)
            elif (class_count<6) and (class_count>2):
                self.dataframe = self.label_encoding(column)
            else:
                self.dataframe = self.drop(column)

        return self.dataframe

    # to divide categorical columns
    def catogerical_columns(self):
        return self.dataframe.select_dtypes(include='object').columns

    # to check whether the column has null values
    def check_null(self, column):
        if self.dataframe[column].isnull().sum() > 0:
            return True

    # to check number of class
    def check_class(self, column):
        a = (self.dataframe[column].value_counts().count())
        return a


    # to do mode imputation
    def mode_imputation(self, column):
        return self.dataframe[column].fillna(self.dataframe[column].mode()[0])

    # for one hot encoding
    def one_hot_encoding(self, column):
        dummy = pd.get_dummies(self.dataframe[column],prefix=column)
        self.dataframe.drop([column], inplace=True, axis=1)
        c = pd.concat([self.dataframe, dummy], axis=1, )
        return c

    # for label_encoding
    def label_encoding(self,column):
        labelencoding = LabelEncoder()
        self.dataframe[column] = labelencoding.fit_transform(self.dataframe[column])
        return self.dataframe

    # to drop
    def drop(self,column):
        self.dataframe = self.dataframe.drop([column],axis=1,inplace=True)



if __name__=='__main__':
    df = pd.read_csv(input("Enter only name of the dataset if it is in the same directory else enter the name with directory:"))
    print('Loading...')
    ob1 = numerical_treatment(df)
    b=ob1.num_df()
    ob2 = categorical_imputation(b)
    a = ob2.cat_df()
    a.to_csv(input('Enter the name of the cleaned dataset to be saved:'))
    print("completed")


