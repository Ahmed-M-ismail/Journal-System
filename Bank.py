#===================<< DB connection & try Except >>============================
try:

    import MySQLdb  # 34an a3rf a connect bl DB.
    DB = MySQLdb.Connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db = 'bank'
    )
    cursor = DB.cursor()
except:
    print 'No DB Connection'
#==========================<< Main Program >>========================================
from Tkinter import *
from distutils.core import setup
import py2exe
#import tkFont
import tkMessageBox

root = Tk()
root.title("Bank System")

canvas = Canvas(width = 370, height = 240, bg = "#ffffff")
photo = PhotoImage(file="53770.gif")  
canvas.create_image(185, 120, image = photo, )
canvas.pack()
time = 5
def tick():
    global time
    time -= 1
    
    if time == 0: 
        #root.update()
        canvas.destroy()
        root.geometry('380x220+400+100')
        root.title('Bank Management System')  
        root.configure(background="#FFFFFF")
        Banklabel = Label(root,text="Bank System" ,bg="#FFFFFF", fg="#19BB9B" )
        Banklabel.config(height=2, width=20)
        Banklabelfont = ('Tahoma', 30, 'bold')
        Banklabel.config(font=Banklabelfont)
        Banklabel.pack()     
    
        UserObj = user()
        RegisterLabel = Label(root,text="(1) Press here for Create Account : ",bg="#F39B11",fg="white" ,pady=5 )
        Registerfont = ('times', 11, 'bold')
        RegisterLabel.config(font=Registerfont)  
        RegisterLabel.place(x=30,y=100)
        Register = Button(root,text="Register",bd=5 ,bg=  "#1ABC9C " ,fg="white",command= lambda: UserObj.CreateRegisterPage('Registration Page For Customers','Customer'))
        Register.place(x=295,y=100 , width = 70, height = " 30" )
        Registerfont = ('Tahoma' , 8 , 'bold')
        Register.config(font = Registerfont)
        
        LoginLabel = Label(root,text="(2) Press To Login for Your Account : ",bg="#F39B11",fg="white",pady=5)
        Loginfont = ('times', 11, 'bold')
        LoginLabel.config(font=Loginfont)  
        LoginLabel.place(x=30,y=150)
        Login = Button(root,text="Login" ,bd=5 ,bg=  "#1ABC9C ",fg="white",command = UserObj.CreateLoginPage)
        Login.place(x=295,y=150 , width =70, height = " 30" )
        Loginfont = ('Tahoma' , 8 , 'bold')
        Login.config(font = Loginfont)                  
    else:
        canvas.after(1000, tick)
canvas.after(1, tick)
#========================<< class User >>==========================================
class user:
    def __init__(self):
        ID=0
    def setuserID(self,ID):
        self.ID = ID
    def getuserID(self):
        return self.ID     


    def setName(self,name):
        if len(name) > 4:
            
            if re.match("[0-9]", name) != None:
                self.name= "invaild"
            else:
                self.name=name 
        else:
            self.name= "invaild"        
        
        
        
    def getName(self):
        return self.name    



    def setPhone(self,phone):
        
        if len(phone) > 10:
            
            if re.match("[0-9]", phone) != None:
                self.phone=phone
            else:
                self.phone= "invaild" 
                
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",phone)!= None:
                self.phone= "invaild"
        else:
            self.phone= "invaild"
            
    def getPhone(self):
        return self.phone    



    def setEmail(self,email):
        
        if len(email) > 7:
            
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                self.email=email
            else:
                self.email= "invaild" 
        else:
            self.email= "invaild"
            
    def getEmail(self):
        return self.email


    def setAdress(self,adress):
        self.adress = adress
    def getAdress(self):
        return self.adress    


    def setUsername(self,username):
        self.username = username
    def getUsername(self):
        return self.username

    def setPassword(self,password):
        self.password = password
    def getPassword(self):
        return self.password
    
        

    def CreateLoginPage(self): # to create login form
        #root.withdraw()
        #root.destroy()
        self.LoginPage = Tk()
        self.LoginPage.geometry('350x150+400+100')
        self.LoginPage.title('Login Page')
        label = Label(self.LoginPage,text="Login Page",bg="#FFFFFF",fg="#000")
        label.config(height=2, width=20)
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont)        
        self.LoginPage.configure(background="#FFFFFF")   
        label.pack()
                
        Username = Label(self.LoginPage, text = "Username :",bg="#FFFFFF",fg="#F5B516" )
        Username.grid(row = 0, column = 0, sticky = E)
        Username.place(x=50 , y = 50)
        Usernamefont = ('Tahoma', 10, 'bold')
        Username.config(font=Usernamefont )
        self.ValueUsername = Entry(self.LoginPage,width=25  , bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueUsername.grid(row = 0, column = 1, sticky = W)
        self.ValueUsername.place(x = 140 , y = 55 )

        Password = Label(self.LoginPage, text = "Password :",bg="#FFFFFF",fg="#F5B516" )
        Password.grid(row = 1, column = 0, sticky = E)
        Password.place(x=50 , y = 78)
        Passwordfont = ('Tahoma', 10, 'bold')
        Password.config(font=Passwordfont )        
        self.ValuePassword = Entry(self.LoginPage,show='*',width=25 , bg="#1ABB9B" , fg="#FFFFFF" )
        self.ValuePassword.grid(row = 1, column = 1)
        self.ValuePassword.place(x=140 , y = 80)

        self.Login_btn = Button(self.LoginPage, text = "Login",bd=4 ,width="15",bg=  "#1ABC9C ",fg="white", command = self.login)
        self.Login_btn.place(x=50,y=110)
        self.Login_btnfont = ('Tahoma', 8, 'bold')
        self.Login_btn.config(font=self.Login_btnfont)
        
        self.Forget_btn = Button(self.LoginPage, text = "Forget Password",width="15",bd=4 ,bg=  "#F5B516 ",fg="white", command = self.CreateForgetPage)
        self.Forget_btn.place(x=175,y=110)
        self.Forget_btnfont = ('Tahoma', 8, 'bold')
        self.Forget_btn.config(font=self.Forget_btnfont)                  


        self.LoginPage.mainloop()



    def CreateForgetPage(self): # to create forget password form
        self.LoginPage.destroy()
        self.ForgetPage = Tk()
        self.ForgetPage.geometry('350x200+400+100')
        self.ForgetPage.title('Forget Your Password ')
        label = Label(self.ForgetPage,text="Forget Password Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=2, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont)        
        self.ForgetPage.configure(background="#FFFFFF")  
        label.pack()

        Email = Label(self.ForgetPage, text = "Email:",bg="#FFFFFF",fg="#F5B516")
        Email.grid(row = 2, column = 0, sticky = E)
        Email.place(x=45 , y = 50)
        Emailfont = ('Tahoma', 11, 'bold')
        Email.config(font=Emailfont )        
        self.ValueEmail = Entry(self.ForgetPage,width=31, bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueEmail.grid(row = 2, column = 1, sticky = W) 
        self.ValueEmail.place(x=122 , y = 53)

        QuestionLabl = Label(self.ForgetPage, text = "Question:",bg="#FFFFFF",fg="#F5B516")
        QuestionLabl.grid(row = 4, column = 0, sticky = E)             
        QuestionLabl.place(x=40,y=85)
        QuestionLablfont = ('Tahoma', 11, 'bold')
        QuestionLabl.config(font=QuestionLablfont )         
        QuestionKinds  = ['What is your favorite color ?' ,'Your Mother Name ?']
        self.QuestionVariable  = StringVar(self.ForgetPage)
        self.QuestionVariable.set('What is your favorite color ?')
        Questions = OptionMenu(self.ForgetPage,self.QuestionVariable,*QuestionKinds)
        Questions.config(bg="#1ABB9B" , fg="#ffffff" , bd=0)
        Questions["menu"].config(bg="#1ABB9B", fg="#ffffff")
        Questions.pack()
        Questions.grid(row = 4, column = 1, sticky = W)
        Questions.place(x=122 , y = 83)

        Answer = Label(self.ForgetPage, text = "Answer:",bg="#FFFFFF",fg="#F5B516")
        Answer.grid(row = 5, column = 0, sticky = E)
        Answer.place(x=45 , y = 120)
        Answerfont = ('Tahoma', 11, 'bold')
        Answer.config(font=Answerfont )        
        self.ValueAnswer = Entry(self.ForgetPage,width=31 ,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueAnswer.grid(row = 5, column = 1, columnspan = 2 ,sticky = W) 
        self.ValueAnswer.place(x=122 , y = 123)

        self.Remember_btn = Button(self.ForgetPage, text = "Remember", width=20 ,bg="#F29A0D",fg="#ffffff" ,command = self.ForgetPassword)
        self.Remember_btn.place(x=122,y=150) 
        Remeberfont = ('Tahoma' , 11 , 'bold')
        self.Remember_btn.config(font = Remeberfont)


        self.ForgetPage.mainloop()


    def CreateRegisterPage(self,PageName,Type): # to create Register form page
        
        self.RegisterPage = Tk() 
        self.RegisterPage.geometry('350x350+400+100')
        self.RegisterPage.title(PageName)
        label = Label(self.RegisterPage,text="Regsiter Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=1, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont)          
        self.RegisterPage.configure(background="#FFFFFF") 
        label.pack()

        Name = Label(self.RegisterPage, text = "Name :*",bg="#FFFFFF",fg="#F5B516")
        Name.grid(row = 0, column = 0, sticky = E)
        Name.place(x=45 , y = 42)  
        Namefont = ('Tahoma', 10, 'bold')
        Name.config(font=Namefont )            
        self.ValueName = Entry(self.RegisterPage,width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueName.grid(row = 0, column = 1, sticky = W)
        self.ValueName.place(x=127 , y= 45)

        Phone = Label(self.RegisterPage, text = "Phone :*",bg="#FFFFFF",fg="#F5B516")
        Phone.grid(row = 1, column = 0, sticky = E)
        Phone.place(x=45 , y = 65)
        Phonefont = ('Tahoma', 10, 'bold')
        Phone.config(font=Phonefont )        
        self.ValuePhone = Entry(self.RegisterPage,width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValuePhone.grid(row = 1, column = 1, sticky = W)
        self.ValuePhone.place(x=127 , y= 67)

        Email = Label(self.RegisterPage, text = "Email :*",bg="#FFFFFF",fg="#F5B516")
        Email.grid(row = 2, column = 0, sticky = E)
        Email.place(x=45 , y = 87)
        Emailfont = ('Tahoma', 10, 'bold')
        Email.config(font=Emailfont )          
        self.ValueEmail = Entry(self.RegisterPage,width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueEmail.grid(row = 2, column = 1, sticky = W)
        self.ValueEmail.place(x=127 , y= 89)
        
        Adress = Label(self.RegisterPage, text = "Adress :",bg="#FFFFFF",fg="#F5B516")
        Adress.grid(row = 3, column = 0, sticky = E)
        Adress.place(x=45 , y = 109)
        Adressfont = ('Tahoma', 10, 'bold')
        Adress.config(font=Adressfont )          
        self.ValueAdress = Entry(self.RegisterPage,width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueAdress.grid(row = 3, column = 1, sticky = W)   
        self.ValueAdress.place(x=127 , y= 111)

        QuestionLabl = Label(self.RegisterPage, text = "Question :*",bg="#FFFFFF",fg="#F5B516")
        QuestionLabl.grid(row = 4, column = 0, sticky = E)  
        QuestionLabl.place(x=45 , y = 139)
        QuestionLablfont = ('Tahoma', 10, 'bold')
        QuestionLabl.config(font=QuestionLablfont )        
        QuestionKinds  = ['What is your favorite color ?' ,'Your Mother Name ?']
        self.QuestionVariable  = StringVar(self.RegisterPage)
        self.QuestionVariable.set('What is your favorite color ?')
        Questions = OptionMenu(self.RegisterPage,self.QuestionVariable,*QuestionKinds)
        Questions.config(bg="#1ABB9B" , fg="#ffffff" , width=25)
        Questions["menu"].config(bg="#1ABB9B", fg="#ffffff")
        Questions.pack()        
        Questions.grid(row = 4, column = 1, sticky = W)
        Questions.place(x=127 , y= 133)

        Answer = Label(self.RegisterPage, text = "Answer :*",bg="#FFFFFF",fg="#F5B516")
        Answer.grid(row = 5, column = 0, sticky = E)
        Answer.place(x=45 , y = 166)
        Answerfont = ('Tahoma', 10, 'bold')
        Answer.config(font=Answerfont )        
        self.ValueAnswer = Entry(self.RegisterPage,width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueAnswer.grid(row = 5, column = 1, sticky = W)          
        self.ValueAnswer.place(x=127 , y= 168)

        Username = Label(self.RegisterPage, text = "Username:*",bg="#FFFFFF",fg="#F5B516")
        Username.grid(row = 6, column = 0, sticky = E)
        Username.place(x=45 , y = 188)
        Usernamefont = ('Tahoma', 10, 'bold')
        Username.config(font=Usernamefont )         
        self.ValueUsername = Entry(self.RegisterPage,width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueUsername.grid(row = 6, column = 1, sticky = W)
        self.ValueUsername.place(x=127 , y= 190)
        
        Password = Label(self.RegisterPage, text = "Password:*",bg="#FFFFFF",fg="#F5B516")
        Password.grid(row = 7, column = 0, sticky = E)
        Password.place(x=45 , y = 210)
        Passwordfont = ('Tahoma', 10, 'bold')
        Password.config(font=Passwordfont )         
        self.ValuePassword = Entry(self.RegisterPage,show='*',width=32,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValuePassword.grid(row = 7, column = 1, sticky = W)
        self.ValuePassword.place(x=127 , y= 212)
        
        self.Register_btn = Button(self.RegisterPage, text = "Register" ,width="20" ,bg="#F29A0D",fg="#ffffff" ,command = lambda: self.Register(Type))
        self.Register_btn.place(x=129,y=240)         
        Registerfont = ('Tahoma' , 11 , 'bold')
        self.Register_btn.config(font = Registerfont)
        self.RegisterPage.mainloop()        



    def login(self):# to check the authentication (login function)


        query = "SELECT * FROM user WHERE user.Username = '" + self.ValueUsername.get()+ "' AND user.Password = '" +self.ValuePassword.get()+  "'"
        cursor.execute(query)
        result = cursor.fetchall()
    
        if result:
            for row in result:
                self.setuserID(row[0])  
            
            
            tkMessageBox.showinfo('Login Result','You are Logged in Successfully !')
            if result[0][9] == "Admin":
                root.destroy()
                self.LoginPage.destroy()#to close login form
                objAdmin = Admin() # create object to call function from other class
                objAdmin.setcustID(self.getuserID())
                objAdmin.CreateAdminPanel()#to redirect to admin page
                            
            if result[0][9] == "Customer":
                root.destroy()
                self.LoginPage.destroy()#to close login form
                objCustomer = customer()# create object to call function from other class
                objCustomer.setcustID(self.getuserID())
                objCustomer.CreateCustomerPanel()#to redirect to operation page 
            
              
        else:
            tkMessageBox.showinfo('Login Result','Wrong Username Or Password !')    



    def ForgetPassword(self):# function forget password
        self.setEmail(self.ValueEmail.get())
        query = "SELECT * FROM user WHERE user.Email = '" + self.getEmail()+ "' AND user.Question = '" +self.QuestionVariable.get()+"' AND user.Answer = '" +self.ValueAnswer.get()+ "'"
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            tkMessageBox.showinfo('Remember Your Password','You Password is : '+`result[0][6]`)
            self.ForgetPage.destroy()
        else:
            tkMessageBox.showinfo('Remember Your Password','Wrong Email Or Question Answer !')        



    def Register(self,Type):#function Registration
    
        if self.ValueName.get().strip() != '' and self.ValuePhone.get().strip() != '' and self.ValueEmail.get().strip() != '' and self.ValueUsername.get().strip() != '' and self.ValuePassword.get().strip() != '' :
    
            self.setName(self.ValueName.get())
            self.setPhone(self.ValuePhone.get())
            self.setEmail(self.ValueEmail.get())
            self.setAdress(self.ValueAdress.get())
            self.setUsername(self.ValueUsername.get())
            self.setPassword(self.ValuePassword.get())  
            #print 'el mfrood hna el mail'
            if self.getEmail() == "invaild":
                tkMessageBox.showinfo('Registeration Result','Invaild Email ... rewrite a vaild one !')
            
            if self.getPhone() == "invaild":
                tkMessageBox.showinfo('Registeration Result','Invaild Number Phone')
            
            if self.getName() == "invaild":
                tkMessageBox.showinfo('Registeration Result','Invaild Name')            
        
            
            if self.getEmail() != "invaild" and self.getPhone() != "invaild" and self.getName() != "invaild":
                    
                try:#f 7alt eno d5l nfs el username aw email kan mwgood f el DB abl kda
                    result = cursor.execute("""INSERT INTO user (Name,Question,Answer,Phone,Email,Adress,Username,Password,Type,Active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(self.getName(),self.QuestionVariable.get(),self.ValueAnswer.get(),self.getPhone(),self.getEmail(),self.getAdress(),self.getUsername(),self.getPassword(),Type,1))
                    DB.commit() #34an tsgl el klam dh f el DB
                    if result:
                        tkMessageBox.showinfo('Registeration Result','You are sign up Successfully !')
                        self.RegisterPage.destroy()#to close Register form       
                except:#f 7alt eno d5l nfs el username aw email kan mwgood f el DB abl kda
                    tkMessageBox.showinfo('Registeration Result','This Email Or Username is used before...Try another Mail or Username')
                
        else:#f 7alt f field mn el required fady lazm ymlah
            tkMessageBox.showinfo('Registeration Result','please Fill Required fields')        

#==========================================<< class Admin >>==================================   
class Admin(user):
    def setcustID(self,custID):
        self.custID = custID
    def getcustID(self):
        return self.custID 
    
    
    
    
    def Createsearchtransaction(self):
        #self.AdminPage.destroy()
        searchtransaction = Tk()
        searchtransaction.geometry('350x200+400+100')#btn : bg="#1ABB9B",fg="#ffffff"  #txt : ,bg="#F39B11",fg="white"
        searchtransaction.title('Welcome To seacrh transaction Panel')
        label = Label(searchtransaction,text="Search transaction Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=1, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont)         
        searchtransaction.configure(background="#ffffff")
        label.pack()
        custID = Label(searchtransaction, text = "Customer  ID :",bg="#F39B11",fg="white")
        custID.grid(row = 0, column = 1, sticky = E)
        custID.place(x=40 ,y = 50,height="25")
        self.ValuecustID = Entry(searchtransaction,bg="#1ABB9B",fg="#ffffff" )
        self.ValuecustID.grid(row = 0, column = 1, sticky = W)  
        self.ValuecustID.place(x=130 , y = 50,height="25" ,width ="170")
        search_user = Button(searchtransaction,text="Search transactions",bg="#F39B11",fg="white",command= lambda: self.search_transaction())
        search_user.place(x=130,y=80,width="170") 
        search_userfont = ('Tahoma' , 10 , 'bold')
        search_user.config(font = search_userfont)
           
        searchtransaction.mainloop()           
    def search_transaction(self):
        search=Tk()
        search.title('Transaction Result')
        search.configure(background="#ffffff")      
        self.setcustID(self.ValuecustID.get())
        cursor.execute("""select * from account where  CustID ='%s' """ , (int(self.getcustID())))
        result1=cursor.fetchall()
        if result1:
            for row in result1:
                ID=row[0]
        
            cursor.execute("""select  *  from transaction where AccID='%s' """ ,int(ID))
            results=cursor.fetchall()
            i=0
            try:
                for row in results:
                    ID = row[0]
                    AccID=row[1]
                    Type=row[2]
                    Amont = row[3] 
                    Time = row[4]
                    ID1=Label( search,text=ID)
                    AccID1=Label( search,text=AccID)
                    Type1=Label( search,text=Type )
                    Amont1=Label( search,text=Amont)
                    Time=Label( search,text=Time)
            
                    ID1.grid(row=i,column=0)
                    AccID1.grid(row=i,column=1)
                    Type1.grid(row=i,column=2)
                    Amont1.grid(row=i,column=3)
                    Time.grid(row=i,column=4)
                    i+=1
                search.mainloop()   
            except:
                    tkMessageBox.showinfo('Result','not connected !')        
            
       
        else:
            
            cursor.execute("""select * from user where  User_ID ='%s' """ , (int(self.getcustID())))
            result4=cursor.fetchall()
            if result4:
                
                tkMessageBox.showinfo('Error Found','this custome has no account id Yet !')
            else:
                tkMessageBox.showinfo('Error Found','No customer have this iD !')        
       
                    
            
                
       
                
          
    
    def CreateAdminPanel(self):
        self.AdminPage = Tk()
        self.AdminPage.geometry('350x280+400+100')
        self.AdminPage.title('Welcome To Admin Panel')
        label = Label(self.AdminPage,text="Admin Panel Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=1, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont) 
        label.pack()        
        self.AdminPage.configure(background="#ffffff")  
        self.AddAdmin = Button(self.AdminPage,text="Add New Admin", bg="#1ABB9B",fg="#ffffff",command= lambda: self.CreateRegisterPage('Registration Page For Admins','Admin'))
        self.AddAdmin.place(x=80 , y = 40 ,width=200)
        AddAdminFont = ('Tahoma' , 11 , 'bold')
        self.AddAdmin.config(font = AddAdminFont)
        
        showcustomer = Button(self.AdminPage,text="Show All Users ",bg="#F39B11",fg="white",command= lambda: self.showall())
        showcustomer.place(x=80 , y = 90 ,width=200)
        showcustomerFont = ('Tahoma' , 11 , 'bold')
        showcustomer.config(font = showcustomerFont)        
        
        searchcustomer = Button(self.AdminPage,text="Show user  Transactions ",bg="#1ABB9B",fg="#ffffff" ,command= lambda: self.Createsearchtransaction())
        searchcustomer.place(x=80 , y = 140 ,width=200)
        searchcustomerFont = ('Tahoma' , 11 , 'bold')
        searchcustomer.config(font = searchcustomerFont)        
        
        TransReport = Button(self.AdminPage,text="Transaction Report",bg="#F39B11",fg="white",command= lambda: self.TransReport())
        TransReport.place(x=80 , y = 190 ,width=200)
        TransReportFont = ('Tahoma' , 11 , 'bold')
        TransReport.config(font = TransReportFont)        
          
        self.logout = Button(self.AdminPage, text = "LogOut",bg="#1ABB9B",fg="#ffffff", command =lambda:  self.AdminPage.destroy())
        self.logout.place(x=80,y=240,width=200) 
        self.logoutFont = ('Tahoma' , 11 , 'bold')
        self.logout.config(font = self.logoutFont)         
        self.AdminPage.mainloop()
        
    def showall(self):

        show=Tk()
        show.title("All User In System")
        query="SELECT * from user where Active=1"
        cursor.execute(query)
        result=cursor.fetchall() 
        i=0
        try:
            for row in result:
                user_id=row[0]
                name=row[1]
                phone=row[2]
                email=row[3]
                addres=row[4]
                typeO_cus=row[9]
                id=Label(show,text=user_id)
                name1=Label(show,text=name)
                phone1=Label(show,text=phone)
                email1=Label(show,text=email)
                addres1=Label(show,text=addres)
                Ocust=Label(show,text=typeO_cus)  
                dele=Button(show,text="Delet",command= lambda: self.enterid())
                id.grid(row=i,column=0)
                name1.grid(row=i,column=1)
                phone1.grid(row=i,column=2)
                email1.grid(row=i,column=3)
                addres1.grid(row=i,column=4)
                Ocust.grid(row=i,column=5)
                dele.grid(row=i,column=6)
                i+=1
            show.mainloop()
        except:
            tkMessageBox.showinfo('Result','not connected !')
                
    def enterid(self):
        get_id=Tk()
        get_id.title("Delete User")
        var=IntVar( value=0)
        lbl_id = Label(get_id, text = "ID:")
        lbl_id.grid(row = 1, column = 0, sticky = E) 
        self.tb_id = Entry(get_id,width=32)
        self.tb_id.grid(row = 1, column = 1)
        btn2=Button(get_id,text="delete",command=lambda: self.deluser())
        btn2.grid(row=1,column=3) 
        get_id.mainloop(n=0)

    def deluser(self):
        
        id=int(self.tb_id.get())
        query="SELECT * from user where Active=1"
        cursor.execute(query)
        result=cursor.fetchall() 
        i=0
        for row in result:
            user_id=row[0]
            if(id==user_id):
                quer="Update user SET Active=0 Where User_ID='%d'" %(id)
                cursor.execute(quer)
                DB.commit()
                i=1
            else:
                DB.rollback()
        if(i==0):
            tkMessageBox.showinfo('Result','Not Found !')
        else:
            tkMessageBox.showinfo('Result','Deleted !')

    def TransReport(self):
        #self.AdminPage.destroy()
        query1 = "SELECT * FROM transaction"
        cursor.execute(query1)            
        final=cursor.fetchall()    
        i = 0
        if(final):
            TransReport = Tk()
            TransReport.geometry('350x380+400+100')
            TransReport.title(string='Tranaction Report')            
            for row in final:                       
                ID = row[0]
                AccID = row[1]
                Type = row[2]
                Amount = row[3]
                Time = row[4]
                ID1=Label(TransReport,text=ID)
                AccID1=Label(TransReport,text=AccID)
                Type1=Label(TransReport,text=Type)
                Amount1=Label(TransReport,text=Amount)
                Time1=Label(TransReport,text=Time)
                ID1.grid(row=i,column=0)
                AccID1.grid(row=i,column=1)
                Type1.grid(row=i,column=2)
                Amount1.grid(row=i,column=3)
                Time1.grid(row=i,column=4)
                i+=1
            TransReport.mainloop()
        else: tkMessageBox.showerror(title='Error', message='There are no Transactions!!')                      
#========================================<< Customer >>============================================
            
class customer(user):
        
    def setcustID(self,custID):
        self.custID = custID
    
    
    def getcustID(self):
        return self.custID 
    
    def setAmont(self,Amont):
        self.Amont = Amont
    def getAmont(self):
        return self.Amont    
    
    def CreateCustomerPanel(self):
        
        self.CustomerPanel = Tk()
        self.CustomerPanel.geometry('350x200+400+100')
        self.CustomerPanel.title('Welcome To Customer Panel')
        self.CustomerPanel.configure(background="#ffffff")  
        label = Label(self.CustomerPanel,text="Customer Panel Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=1, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont) 
        label.pack()
        
        DepositeLabel = Label(self.CustomerPanel,text="(1) Press here for Deposite : ",bg="#F39B11",fg="white" ,pady=5 )
        DepositeLabel.place(x=30,y=40)
        self.Deposite_btn = Button(self.CustomerPanel, text = "Deposite" ,bg="#1ABB9B",fg="#ffffff", command =lambda: self.CreateoperationPage())
        self.Deposite_btn.place(x=210,y=41,width="115")
        self.Deposite_btnfont = ('Tahoma', 9, 'bold')
        self.Deposite_btn.config(font=self.Deposite_btnfont)  
        
        WithdrawLabel = Label(self.CustomerPanel,text="(2) Press here for Withdraw : ",bg="#F39B11",fg="white" ,pady=5 )
        WithdrawLabel.place(x=30,y=80)        
        self.Withdraw_btn = Button(self.CustomerPanel, text = "Withdraw",bg="#1ABB9B",fg="#ffffff", command =lambda: self.CreateoperationPage2())
        self.Withdraw_btn.place(x=210,y=81,width="115")
        self.Withdraw_btnfont = ('Tahoma', 9, 'bold')
        self.Withdraw_btn.config(font=self.Withdraw_btnfont)        

        ShowLabel = Label(self.CustomerPanel,text="(2) Press here for Withdraw : ",bg="#F39B11",fg="white" ,pady=5 )
        ShowLabel.place(x=30,y=120)        
        self.search_btn = Button(self.CustomerPanel, text = "show my account",bg="#1ABB9B",fg="#ffffff", command =lambda: self.search_account())
        self.search_btn.place(x=210,y=121,width="115")   
        self.search_btnfont = ('Tahoma', 9, 'bold')
        self.search_btn.config(font= self.search_btnfont)        
                 
        self.logout = Button(self.CustomerPanel, text = "LogOut",bg="#1ABB9B",fg="#ffffff",command =lambda: self.CustomerPanel.destroy() )
        self.logout.place(x=210,y=160,width="115")         
        self.logoutfont = ('Tahoma', 9, 'bold')
        self.logout.config(font=  self.logoutfont)  
        
    def CreateoperationPage(self): # to create operation page
        #self.CustomerPanel.destroy()
        self.operationPage = Tk()
        self.operationPage.geometry('350x200+400+100')
        self.operationPage.title('Deposite Page')
        self.operationPage.configure(background="#ffffff") 
        label = Label(self.operationPage,text="Deposite Panel Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=1, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont)
        label.pack()
        
        Amont = Label(self.operationPage, text = "Amont of money  :",bg="#F39B11",fg="white" ,pady=5)
        Amont.grid(row = 1, column = 1, sticky = E)
        Amont.place(x=40, y = 90)
        self.ValueAmont = Entry(self.operationPage,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueAmont.grid(row = 1, column = 1, sticky = W)  
        self.ValueAmont.place(x=170,y=93, height = 25)
            
        self.Register_btn = Button(self.operationPage, text = "confirm" ,bg="#F39B11",fg="white", command = self. deposite)
        self.Register_btn.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        self.Register_btn.place(x=100,y=140,width="150")
            
            
        self.RegisterResult = Label(self.operationPage , bg="#1ABB9B",fg="white")
        self.RegisterResult.grid(row = 3, column = 1, columnspan = 2, sticky = W)  
        self.RegisterResult.place(x=100 , y = 170 , height = 25 , width="180")
            
            
            
        self.operationPage.mainloop()        
            
            
    def CreateoperationPage2(self): # to create operation page
        #self.CustomerPanel.destroy()
        self.operationPage = Tk()
        self.operationPage.geometry('350x200+400+100')
        self.operationPage.title('Withdraw Page')
        self.operationPage.configure(background="#ffffff") 
        label = Label(self.operationPage,text="Withdraw Panel Page",bg="#FFFFFF",fg="#000" , bd=4)
        label.config(height=1, width=20 )
        labelfont = ('Tahoma', 15, 'bold')
        label.config(font=labelfont)
        label.pack()

            
        Amont = Label(self.operationPage, text = "Amont of money  :",bg="#F39B11",fg="white" ,pady=5)
        Amont.grid(row = 1, column = 1, sticky = E)
        Amont.place(x=40, y = 90)
        self.ValueAmont = Entry(self.operationPage,bg="#1ABB9B" , fg="#FFFFFF")
        self.ValueAmont.grid(row = 1, column = 1, sticky = W)  
        self.ValueAmont.place(x=170,y=93, height = 25)
            
        self.Register_btn = Button(self.operationPage, text = "confirm" ,bg="#F39B11",fg="white", command = self. withdraw)
        self.Register_btn.grid(row = 2, column = 1, columnspan = 2, sticky = W)
        self.Register_btn.place(x=100,y=140,width="150")
            
            
        self.RegisterResult = Label(self.operationPage , bg="#1ABB9B",fg="white")
        self.RegisterResult.grid(row = 3, column = 1, columnspan = 2, sticky = W)  
        self.RegisterResult.place(x=100 , y = 170 , height = 25 , width="180")  
        
    def deposite(self):#function Deposite
        
        self.setAmont(self.ValueAmont.get())
        cursor.execute("""select * from account where  CustID ='%s' """ , (int(self.getcustID())))
        result1=cursor.fetchall()
        if result1:
            for row in result1:
                ID=row[0]
                        
            result= cursor.execute("""INSERT INTO transaction (AccID,Type,Amont) VALUES (%s,%s,%s)""",(int(ID),'Deposite',int(self.getAmont())))
           
            
            result2=cursor.execute("""update account  set money_amount= money_amount+'%s'  where id='%s'  """ , ( int(self.getAmont()) , int(ID)) )  
            DB.commit() #34an tsgl el klam dh f el DB
            if result:
                self.RegisterResult["text"] = "Deposite  done successfully"
            else:
                self.RegisterResult["text"] = "process has not been completed "            

        else:
            cursor.execute("""select * from user where  User_ID ='%s' """ , (int(self.getcustID())))
            result4=cursor.fetchall()
                       
            if result4:
                
                cursor.execute("""INSERT INTO account (CustID,money_amount) VALUES (%s,%s)""",(int(self.getcustID()),int(self.getAmont())))
                DB.commit() #34an tsgl el klam dh f el DB
                cursor.execute("""select * from account where  CustID ='%s' """ , (int(self.getcustID())))
                result6=cursor.fetchall()
                for row in result6:
                    ID=row[0]                
                
                result= cursor.execute("""INSERT INTO transaction (AccID,Type,Amont) VALUES (%s,%s,%s)""",(int(ID),'Deposite',int(self.getAmont())))
                DB.commit() #34an tsgl el klam dh f el DB
                self.RegisterResult["text"] = "Deposite  done successfully"
            else:
                tkMessageBox.showinfo('Error Found','No customer have this iD !')
            
    def withdraw(self):#function Withdraw
         
        self.setAmont(self.ValueAmont.get())
        cursor.execute("""select * from account where  CustID ='%s' """ , (int(self.getcustID())))
        result1=cursor.fetchall()
        if result1:
            for row in result1:
                ID=row[0]
                money_amount=row[2]
                if int(money_amount)<int(self.getAmont()):
                    tkMessageBox.showinfo('cant withdraw  ','your amount of money is less than money you want to draw  !')
                else:    
                    result= cursor.execute("""INSERT INTO transaction (AccID,Type,Amont) VALUES (%s,%s,%s)""",(int(ID),'Withdraw',int(self.getAmont())))
           
            
                    result2=cursor.execute("""update account  set money_amount= money_amount-'%s'  where id='%s'  """ , ( int(self.getAmont()) , int(ID)) )  
                    DB.commit() #34an tsgl el klam dh f el DB
                    if result:
                        self.RegisterResult["text"] = "Withdraw  done successfully"
                    else:
                        self.RegisterResult["text"] = "process has not been completed "            
        else:
            
            cursor.execute("""select * from user where  User_ID ='%s' """ , (int(self.getcustID())))
            result4=cursor.fetchall()
            if result4:
                
                tkMessageBox.showinfo('Error Found','this custome has no account id Yet !')
            else:
                tkMessageBox.showinfo('Error Found','No customer have this iD !')
                
   
        
    def search_account(self):  
        
        ID = int(self.getcustID())
        quer="select money_amount from account where CustID ='%d' " %(ID)
        cursor.execute(quer)
        result=cursor.fetchall()
        if(result):
            search=Tk()
            search.geometry('200x100+100+50')
            search.title(string='The Credit')
            label = Label(search,text="The Credit",bg="#FFFFFF",fg="#000")
            label.config(height=1, width=20)
            labelfont = ('Tahoma', 15, 'bold')
            label.config(font=labelfont)  
            label.pack()
            credit_label = Label(search, text="Your Credit is: ", bg="#F39B11",fg="white" ,pady=5)
            credit_label.grid(row=0, column=0)
            credit_display = Label(search, relief=FLAT)
            credit_display.grid(row=0, column=1)
            credit_display.configure(text = result)
            credit_label.pack(side = LEFT)
            credit_display.pack(side = LEFT)
            search.mainloop()            
        else: tkMessageBox.showerror(title='Error', message='Laaaaaaaaaa!!')     
#======================================<< End Main >>====================================
root.mainloop()




