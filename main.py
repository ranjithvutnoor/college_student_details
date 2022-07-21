from mysql_db import forest

def main():
    db = forest()
    while True:
        print('********* welcome **********')
        print()
        print("press 1 to insert new user")
        print("press 2 to dsiplay all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to exit program")
        print()
        try:
            choice = int(input())
            if choice ==1:
                #insert values
                co_name = input('enter college name : ')
                di= input('enter discpline : ')
                nam = input('enter user name : ')
                ro = input('enter roll no : ')
                lo = input('enter location: ')
                db.insert_values(co_name,di,nam,ro,lo)
               
            elif choice==2:
                #display user
                db.fetch_all()

            elif choice==3:
                #delete user
                ro = int(input('enter roll number to be deleted'))
                db.delete_user(ro)
                
            elif choice==4:
                #update user
                co_name = input('enter college name which you want to be update: ')
                nam = input('enter new name : ')
                ro = input('enter new roll no : ')
                db.update_users(co_name,nam,ro)
            elif choice==5:
                break
            else:
                print('invalid input')
        except Exception as e:
            print(e)
            print('invalid details ! try again')        

if __name__ == "__main__":
    main()           