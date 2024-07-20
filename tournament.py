import random 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

class nima() :
    q = int(input("How many teams are playing? ")) 
    teamname = [] #لیست تیم ها
    
    def __init__(self) :  #مقدار دهی اولیه

        self.scores = None #دیکشنری لیست تیم ها و امتیازات
        self.goal_zadeh = None #دیکشنری لیست تیم ها و گل های زده
        self.gole_khorde = None #دیکشنری لیست تیم ها و گل های خورده
        self.win = None # دیکشنری لیست تیم ها و برد های هر تیم
        self.loss = None # دیکشنری لیست تیم ها و باخت های هر تیم
        self.barabar = None # دیکشنری لیست تیم ها و مساوی های هر تیم




    def select_nameteam(self)  :#نام تیم بازی ها 
        a = input("Do you want to enter team names manually? (y/n) ")  #دستی یا خودکار
        if a == "y" or a == "yes": #دستی
            for i in range(self.q): 
                name = input("Enter the team name: ") 
                nima.teamname.append(name) #اضافه کردن نام تیم ها به لیست

        elif a == "n" or a == "no": #خودکار  
            name = ["Esteghlal", "Persepolis", "Tractor Sazi", "alnasr", 
                "PSG", "Sepahan", "Foolad", "Machine Sazi Tabriz", "Barcelona", 
                "Bayern Munich", "Chelsea", "Juventus", "Liverpool", "Manchester City", 
                "Manchester United", "Real Madrid", "Napoli" , "inter milan" , "Al-Hilal" , "Porto" , "Arsenal"
                 , "Atalant" , "naft" , "nasaji" , "havadar" , "malavan" , "peykan" ,  ] 
            nima.teamname = random.sample(name, self.q) #اضافه کردن نام تیم ها به لیست
            print("The list of team names is automatically as follows:") 
            print(nima.teamname) #چاپ نام تیم های ترنومنت

        else: 
            print("Please enter yes or no") 


    def select_macthgame(self):#ساخت نتایج تیم ها
        c = input("Do you want to enter the results of the games manually? (y/n) ") #انتخاب خودکار یا دستی
        point = dict.fromkeys(nima.teamname, 0)#دیکشنری امتیازات و اسم تیم ها
        goale1 = dict.fromkeys(nima.teamname, 0)#دیکشنری مجموع گل های زده و اسم تیم ها
        goale2 = dict.fromkeys(nima.teamname, 0)#دیکشنری مجموع گل های خورده و اسم تیم ها
        win = dict.fromkeys(nima.teamname, 0)#دیکشنری برد های هر تیم و اسم تیم ها
        loss = dict.fromkeys(nima.teamname, 0)#دیکشنری باخت های هر تیم و اسم تیم ها
        barabar = dict.fromkeys(nima.teamname, 0)#دیکشنری مساوی های هر تیم و اسم تیم ها



        if c == "y" or c == "yes":  #دستی
            for i in range(self.q): #حلقه برای رو به رو قرار دادن تیم ها
                for j in range(self.q): 
                    if i == j: 
                        continue 
                    else: 
                        score = input(f"{nima.teamname[i]} vs {nima.teamname[j]}: ")
                        score_list = score.split("-") #جداسازی اعداد گرفته شده
                        team1_goals = score_list[0]  #عدد اول برابر با گل تیم میزبان
                        team2_goals = score_list[1] #عدد دوم برابر با گل تیم مهمان

                        #گل های زده  هر تیم
                        goale1[nima.teamname[i]] += int(team1_goals)
                        goale2[nima.teamname[j]] += int(team2_goals)

                        #گل های خورده هر تیم
                        goale1[nima.teamname[i]] += int(team2_goals)
                        goale2[nima.teamname[j]] += int(team1_goals)

                        #امتیازات بنابر برد باخت یا مساوی
                        if team1_goals > team2_goals:
                            point[nima.teamname[i]] += 3 
                            win[nima.teamname[i]] += 1
                            loss[nima.teamname[j]] += 1

                            print(point) 
                        elif team1_goals == team2_goals:
                            point[nima.teamname[i]] += 1  
                            point[nima.teamname[j]] += 1  
                            barabar[nima.teamname[i]] += 1  
                            barabar[nima.teamname[j]] += 1                                                       
                        else:
                            point[nima.teamname[j]] += 3
                            win[nima.teamname[j]] += 1
                            loss[nima.teamname[i]] += 1


            self.scores = point
            self.goal_zadeh = goale1
            self.gole_khorde = goale2
            self.win = win
            self.loss = loss
            self.barabar = barabar

            max_score = max(point.values())#عدد بیشترین امتیاز
            for key, value in point.items():#همه دیکشنری
                if value == max_score:#مطابقت عدد بیشترین امتیاز با تیم
                    print("The champion is ",key, "with " ,value, "points!")
            se=pd.Series(point)
            print(se)
            self.scores = point

        elif c == "n" or c == "no": #خودکار
            for i in range(nima.q): #روبهرو قرار دادن تیم ها
                for j in range(nima.q): 
                    if i == j: 
                        continue 
                    else: 
                        team1 = random.choice([1,2,3,4,5,6]) #تعداد گل
                        team2 = random.choice([1,2,3,4,5,6]) #تعداد گل
                        print(f"{nima.teamname[i]} vs {nima.teamname[j]}: {team1} - {team2} ") 
                        #گل های زده  هر تیم
                        goale1[nima.teamname[i]] += team1
                        goale1[nima.teamname[j]] += team2

                        #گل های خورده هر تیم
                        goale2[nima.teamname[i]] += team2
                        goale2[nima.teamname[j]] += team1

                        #دادن امتیازات بر اساس باخت و برد و مساوی
                        if team1 > team2:
                            point[nima.teamname[i]] += 3   
                            win[nima.teamname[i]] += 1
                            loss[nima.teamname[j]] += 1

                        elif team1 == team2:
                            point[nima.teamname[i]] += 1  
                            point[nima.teamname[j]] += 1
                            barabar[nima.teamname[i]] += 1  
                            barabar[nima.teamname[j]] += 1
                        else:
                            point[nima.teamname[j]] += 3
                            win[nima.teamname[j]] += 1
                            loss[nima.teamname[i]] += 1


            max_score = max(point.values())#بیشترین امتیاز
            for key, value in point.items():#تطابق بیشترین امتیاز 
                if value == max_score:
                    print(f"The champion is {key} with {value} points!")#اعلام قهرمان
                    self.scores = point
                    self.goal_zadeh = goale1
                    self.gole_khorde = goale2
                    self.win = win
                    self.loss = loss
                    self.barabar = barabar
        else: 
            print("Please enter yes or no")


    def table (self):#کشیدن جدول
        scores = n.scores
        goal_zade = n.goal_zadeh
        gole_khorde = n.gole_khorde
        win = n.win
        loss = n.loss
        D1 = n.barabar


        # جدا کردن کلید و مقدار
        keys_scores = list(scores.keys())
        vals_scores = list(scores.values())
        vals_goal_zade = list(goal_zade.values())
        vals_gole_khorde = list(gole_khorde.values())
        vals_win = list(win.values())
        vals_loss = list(loss.values())
        vals_barabar = list(D1.values())

        # محاسبه تفاضل گل
        diff_goal = [vals_goal_zade[i] - vals_gole_khorde[i] for i in range(len(vals_goal_zade))]

        #محاسبه بازی های انجام شده هر تیم
        MP = [vals_win[i] + vals_loss[i] + vals_barabar[i]  for i in range(len(vals_scores))]


        # ساخت دیکشنری برای ساخت جدول
        a = {'Name': keys_scores, 'Score': vals_scores ,'MP': MP ,'W':vals_win ,'L':vals_loss ,'D':vals_barabar, 'GF': vals_goal_zade, 'GA': vals_gole_khorde, 'Dif' : diff_goal }
        a1 = pd.DataFrame(a)
        #کشیدن جدول بر اساس دیکشنری
        table = pd.DataFrame.from_dict(a)
        table = table.sort_values(by='Score',ascending=False)#مرتب سازی بر اساس امتیازات و نزولی
        table.index = range(1, len(table.Name)+1) # از 1 شروع بشود
        a1.to_csv(r'C:/Users/mgs/Desktop/TOURNOMENT/output.csv', index=False)
        print(table)




    
n = nima()          
n.select_nameteam()
n.select_macthgame()
n.table()

