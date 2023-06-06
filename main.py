import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox,QMainWindow
from PyQt5.uic import loadUi
import mysql.connector as con
from HomePage import *
from Login import LoginForm
from Register import Register_Form
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import psycopg2 



class DashBoard(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.Logout = self.ui.pushButton_11
        self.Logout.clicked.connect(self.login)
    def login(init):
        widget.setCurrentIndex(1)
        

        ###############################


class LoginApp(QDialog):
    def __init__(self):
        super(LoginApp,self).__init__()
        self.ls = LoginForm()
        self.ls.setupUi(self)
        self.show()
        self.Login = self.ls.Login
        self.RegisterHere = self.ls.RegisterHere
        self.Login.clicked.connect(self.login)
        self.RegisterHere.clicked.connect(self.register)
        

    def login(self):
        self.Lemail = self.ls.Lemail
        self.Lpassword =self.ls.Lpassword
        umi =  self.Lemail.text()
        #database =  con.connect(host="localhost",user="root",password="login123",db="Admin",auth_plugin='caching_sha2_password')
        #cursor = database.cursor()
        #cursor.execute("SELECT * FROM users WHERE email_id = '" + umi+ "'")
        #result = cursor.fetchone()
        conn = psycopg2.connect(
        host="localhost",
        database="Admin",
        user="postgres",
        password="login123") 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = '" + umi+ "'")
        result = cursor.fetchone()
        conn.commit()
        self.Lemail.setText("")
        self.Lpassword.setText("")
        

        if result:
            QMessageBox.information(self," User Login  " ," Success fully")
            widget.setCurrentIndex(2)


        else:
            QMessageBox.information(self," User Login " ," Invalid Data ")
        

    def register(self):
        widget.setCurrentIndex(1)
       
        

        


class RegisterApp(QDialog):
    def __init__(self):
        super(RegisterApp,self).__init__()
        self.rs = Register_Form()
        self.rs.setupUi(self)
        self.show()
        self.Register = self.rs.Register
        self.LoginHere = self.rs.LoginHere
        self.Register.clicked.connect(self.registered)
        self.LoginHere.clicked.connect(self.loginPage)

    def loginPage(self):
        widget.setCurrentIndex(0)
       
    def registered(self):
        self.Rusername = self.rs.Rusername
        self.Rpassword = self.rs.Rpassword
        self.Rmobilenumber = self.rs.Rmobilenumber
        self.Remail = self.rs.Remail
        
        un = self.Rusername.text()
        pwt = self.Rpassword.text()
        phn = self.Rmobilenumber.text()
        emi = self.Remail.text()
        #database =  con.connect(host="localhost",user="root",password="login123",db="Admin",auth_plugin='caching_sha2_password')
        #cursor = database.cursor()
        #cursor.execute("SELECT * FROM users WHERE user_name = '" + un + "' AND email_id = '"+ emi +"'")
        #result = cursor.fetchone()
        conn = psycopg2.connect(
        host="localhost",
        database="Admin",
        user="postgres",
        password="login123") 
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = '" + un + "' AND email = '"+ emi +"'")
        result = cursor.fetchone()
        
        if result:
            QMessageBox.information(self," User Registration " ," User Already Exit")
            

        else:
           cursor.execute("INSERT INTO users (user_name,password,email,phone_number) values('"+ un +"','"+ pwt +"','"+ emi +"','"+ phn +"')")
           QMessageBox.information(self," User Registration " ," Registered SuccessFully")
        widget.setCurrentIndex(0)
        conn.commit()










app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginform = LoginApp()
registerform = RegisterApp()
dashboard = DashBoard()
widget.addWidget(loginform)
widget.addWidget(registerform)
widget.addWidget(dashboard)
widget.setCurrentIndex(0)
widget.show()
#widget.setFixedSize(500,600)
widget.setWindowTitle("Count Ai")
widget.setFixedSize(1850,1050)


app.exec_()
     