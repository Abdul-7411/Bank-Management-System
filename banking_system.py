import random
class Bank:
    
    def __init__(self,name=None,age=None,account_type=None,ph_no=None):
        self.name = name
        self.age = age
        self.account_type = account_type
        self.ph_no = ph_no
        
    def save_data(self): 
        self.name = input("Entre Name: ").strip()
        self.age = input("Entre age: ").strip()
        self.account_type = input("Select account type (Saving / Current): ").strip()
        self.ph_no = int(input("Entre phone number: ").strip())
        self.acc_data = [f"Name: {self.name} | Age: {self.age} |" f"Account type: {self.account_type} | Phone: {self.ph_no} |" f"Account number: {random.randint(100000 ,999999)}\n"]
        
        with open('bank.txt','a') as file:
            file.writelines(self.acc_data)
            print("Account Added successfully...\n")    
        
    def search_account(self,ph_no):
        found = False
        try:
            with open('bank.txt','r') as file:
                acc_data = file.readlines()
        except:
            print('No data found!\n')
            return
        
        for data in acc_data:
            if ph_no in data:
                print(f"Data Found:\n{data}")
                found = True
                break
        if not found:
            print("No account found with this phone number\n")
    
    def credit(self,ph_no):
        found = False
        with open('bank.txt','r') as f:
            acc_data = f.readlines()
        updated_data = []
        for data in acc_data:
            if ph_no in data:
                found = True
                amount = int(input("Entre the amount want to credit: "))
                data = data.strip() + f' | Amount: {amount}\n'
            updated_data.append(data)
            
        if found:
            with open('bank.txt','w') as f1:
                f1.writelines(updated_data)
            print("Amount added successfully...\n")
        else:
            print("No data found...\n")

    def remove_account(self,ph_no):
        found = False
        new_data = []
        with open("bank.txt",'r') as f1:
            all_data = f1.readlines()
        for data in all_data:
            if ph_no in data:
                print(f"\n{data.strip()}")
                found = True
            else:
                new_data.append(data)
        with open('bank.txt','w') as f2:
            updated_data = f2.writelines(new_data)
        if found:
            print("Account Removed Successfully...\n")
        else:
            print("No data found...\n")
        
    def withdraw(self, ph_no):
        updated_data = []
        amount_found= False
        found = True
        with open('bank.txt','r') as f:
            lines = f.readlines()
            
        for line in lines:
            if ph_no in line and 'Amount' in line:
                amount_found = True
                found = True
                
                # removing extra spaces and seprating with '|'
                parts = line.strip().split('|')
                
                new_balance = []
                for part in parts:
                    if 'Amount' in part:# checking if amount in list of parts
                        amount_str = part.split(':')[1].strip()# accessing the amount
                        amount = int(amount_str)
                        withdraw = int(input("Entre the amount to withdraw: "))
                        
                        if amount >= withdraw:
                            amount-=withdraw
                            print("Amount withdraw successfully...")
                            print(f"Balance: {amount}\n")
                        else:
                            print("Insufficient balance...\n")
                        
                        part = f"Amount: {amount}"# remaining balance
                    new_balance.append(part.strip())
                    
                updated_line = '|'.join(new_balance) + '\n'# redesign the data col
                updated_data.append(updated_line)# updated in to th list
                
            else:
                updated_data.append(line)
        if not found:
            print('No account found..\n')
        elif not amount_found:
            print("No balance in account\n")
        
        #Updating data
        with open('bank.txt','w') as f1:
            f1.writelines(updated_data)
    
    def check_bal(self,ph_no):
        updated = []
        found = False
        amount_found = False
        with open('bank.txt','r') as file:
            lines = file.readlines()
        for line in lines:
            if ph_no in line and 'Amount' in line:
                found = True
                amount_found = True
                
                #seprating with |
                line_parts = line.strip().split('|')
                
                for part in line_parts:
                    if 'Amount' in part:
                        amount = part.split(':')[1].strip()
                        print(f"Balance: {amount}\n")
            else:
                updated.append(line)        
        if not found:
            print("Account not found...\n")
            
        elif not amount_found:
            print("no balance in account..\n")
          
    def show_all(self):
        try:
            with open("bank.txt",'r') as file:
                all_acc = file.read()
                
        except:
            print("No acconts found")
                
        if all_acc:
            print(f"All Accounts\n{all_acc}")
        else:
            print("No data found...\n")
            
## user handle
def main():
    while True:
        print("---Bank Managment System---")
        print("1. Add account")
        print("2. Search account")
        print("3. Remove account")
        print("4. Show all accounts")
        print("5. Credit money")
        print("6. Withdraw money")
        print("7. Check balance")
        
        user = input("Choose option: ")
        
        bank = Bank()
        
        if user == '1':
            bank.save_data()
            
        elif user == '2':
            ph_no = input("Entre Phone number:").strip()
            bank.search_account(ph_no)
            
        elif user == '3':
            ph_no = input("Entre Phone number:").strip()
            bank.remove_account(ph_no)
            
        elif user == '4':
            bank.show_all()
            
        elif user == '5':
            ph_no = input("Entre Phone number:").strip()
            bank.credit(ph_no)
            
        elif user == '6':
            # print("Inservice...\n")
            ph_no = input("Entre Phone number:").strip()
            bank.withdraw(ph_no)
            
        elif user == '7':
            ph_no = input("Entre Phone number: ").strip()
            bank.check_bal(ph_no)
        
        else:
            print('Invalid option')
            
if __name__=='__main__':
    main()
        
        