def atm():
  #bal=5000
  def login(uname,pin):
    if (uname=='pg' and pin=='12345'):
      print('\nWelcome {}!!!'.format(uname))
      c_s()
    elif(uname!='pg' and pin!='12345'):
      print("\nBOTH INVALID")
      ip()
    elif (uname != 'pg'):
      print('\nINVALID USERNAME')
      ip()
    elif (pin != '12345'):
      print("\nINVALID PIN")
      ip()


  def c_s():
    opt=int(input("\n1.Current\n2.Savings\n"))
    if(opt==1):
      option()
    elif(opt==2):
      option()
    else:
      print("INVALID OPTION")
      con()


  def option():
    bal1=5000
    opt1=int(input("\n1.Deposit \n2.Withdraw \n3.Balance Enquiry\n"))
    if (opt1==1):
      dep(bal1)
    elif (opt1==2):
      withdraw(bal1)
    elif (opt1==3):
      balEnq(bal1)
    else:
      print("\nINVALID OPTION")
      con()

  def dep(bal1):
    depvalue=int(input("\nEnter Deposit Amount: "))
    bal1=bal1+depvalue
    print("\nYour Deposited Amount is {} and Balance is {}".format(depvalue,bal1))
    con()
    return bal1

  def withdraw(bal1):
    wvalue=int(input("\nEnter Withdrawal Amount: "))
    if (wvalue <= bal1):
      bal1=bal1-wvalue
      print("\nYour Balance is {}".format(bal1))
      con()
      return bal1
    else:
      print("INSUFFICIENT BALANCE")
      con()


  def balEnq(bal1):
    print("\nBalance: {}".format(bal1))
    con()

  def con():
    yn=input("Do you Want to Continue (YES/NO): ")
    if (yn=="YES"):
      c_s()
    elif(yn=="NO"):
      ip()
    else:
      print("INVALID INPUT")

  def ip():
    uname=(input("Enter Username: "))
    pin=(input("Enter PIN: "))
    login(uname,pin)

  ip()

atm()
