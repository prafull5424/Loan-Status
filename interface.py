from flask import Flask, jsonify, request, render_template
import config
from Project_data.utiles import LoanStatus
# from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "Stella@5424" or "12345678"
# app.config["MYSQL_DB"] = "loan"
# mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Loan_Status", methods = ["GET","POST"])
def get_status():
    data = request.form

    Current_Loan_Amount = eval(data["Current_Loan_Amount"])
    Term = data["Term"]
    Credit_Score = eval(data["Credit_Score"])
    Years_in_current_job = data["Years_in_current_job"]
    Home_Ownership = data["Home_Ownership"]
    Annual_Income = eval(data["Annual_Income"])
    Purpose = data["Purpose"]
    Monthly_Debt = eval(data["Monthly_Debt"])
    Years_of_Credit_History = eval(data["Years_of_Credit_History"])
    Months_since_last_delinquent = eval(data["Months_since_last_delinquent"])
    Number_of_Open_Accounts = eval(data["Number_of_Open_Accounts"])
    Number_of_Credit_Problems = eval(data["Number_of_Credit_Problems"])
    Current_Credit_Balance = eval(data["Current_Credit_Balance"])
    Maximum_Open_Credit = eval(data["Maximum_Open_Credit"])
    Bankruptcies = eval(data["Bankruptcies"])
    Tax_Liens = eval(data["Tax_Liens"])

    ls = LoanStatus(Current_Loan_Amount, 
    Term, Credit_Score, Years_in_current_job,
    Home_Ownership, Annual_Income, Purpose, 
    Monthly_Debt, Years_of_Credit_History, 
    Months_since_last_delinquent, Number_of_Open_Accounts, 
    Number_of_Credit_Problems, Current_Credit_Balance, 
    Maximum_Open_Credit, Bankruptcies, Tax_Liens)

    status = ls.get_loan_status()
    # cursor = mysql.connection.cursor()
    # query1 = 'CREATE TABLE IF NOT EXISTS loan_detais(Current_Loan_Amount float,Term varchar(20),Credit_Score float,Years_in_current_job varchar(20),Home_Ownership varchar(30),Annual_Income float,Purpose varchar(50),Monthly_Debt float,Years_of_Credit_History float,Months_since_last_delinquent float,Number_of_Open_Accounts float,Number_of_Credit_Problems float,Current_Credit_Balance float,Maximum_Open_Credit float,Bankruptcies float,Tax_Liens float);
    # cursor.execute(query1)
    # cursor.execute(f'INSERT INTO loan_detais Values ({Current_Loan_Amount}, {Term}, {Credit_Score}, {Years_in_current_job},{Home_Ownership}, {Annual_Income}, {Purpose}, {Monthly_Debt}, {Years_of_Credit_History}, {Months_since_last_delinquent}, {Number_of_Open_Accounts}, {Number_of_Credit_Problems}, {Current_Credit_Balance}, {Maximum_Open_Credit}, {Bankruptcies}, {Tax_Liens})')
   
    # mysql.connection.commit()
    # cursor.close()

    if status == 0:
        z1 = "Approved"
    else:
        z1 = "Refused"
    


    return render_template("index1.html",z1=z1)


if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)
    



 