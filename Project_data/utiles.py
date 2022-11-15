import pickle
import json
import config
import numpy as np
import re

class LoanStatus():
    def __init__(self,Current_Loan_Amount, Term, Credit_Score,
        Years_in_current_job, Home_Ownership, Annual_Income, 
        Purpose, Monthly_Debt, Years_of_Credit_History, 
        Months_since_last_delinquent, Number_of_Open_Accounts, 
        Number_of_Credit_Problems, Current_Credit_Balance, 
        Maximum_Open_Credit, Bankruptcies, Tax_Liens):
   
        self.Current_Loan_Amount = Current_Loan_Amount
        self.Term = Term
        self.Credit_Score = Credit_Score
        self.Years_in_current_job = Years_in_current_job
        self.Home_Ownership = Home_Ownership
        self.Annual_Income = Annual_Income
        self.Purpose = Purpose
        self.Monthly_Debt = Monthly_Debt
        self.Years_of_Credit_History = Years_of_Credit_History
        self.Months_since_last_delinquent = Months_since_last_delinquent
        self.Number_of_Open_Accounts = Number_of_Open_Accounts
        self.Number_of_Credit_Problems = Number_of_Credit_Problems
        self.Current_Credit_Balance = Current_Credit_Balance
        self.Maximum_Open_Credit = Maximum_Open_Credit
        self.Bankruptcies = Bankruptcies
        self.Tax_Liens = Tax_Liens

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_loan_status(self):
        self.load_model()
        years = re.findall("\d+",self.Years_in_current_job)[0]
        

        test_array =np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.Current_Loan_Amount
        test_array[1] = self.json_data["Term"][self.Term]
        test_array[2] = self.Credit_Score
        test_array[3] = int(years)
        test_array[4] = self.json_data["Home Ownership"][self.Home_Ownership]
        test_array[5] = self.Annual_Income
        test_array[6] = self.Monthly_Debt
        test_array[7] = self.Years_of_Credit_History
        test_array[8] = self.Months_since_last_delinquent
        test_array[9] = self.Number_of_Open_Accounts
        test_array[10] = self.Number_of_Credit_Problems
        test_array[11] = self.Maximum_Open_Credit
        test_array[12] = self.Bankruptcies
        test_array[13] = self.Tax_Liens
        purpose_index = self.json_data["columns"].index(self.Purpose)
        test_array[purpose_index] = 1
        
        loan_status = self.model.predict([test_array])
        return loan_status