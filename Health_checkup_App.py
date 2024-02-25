from tkinter import *
def scroll_screen(screen):
    main_frame=Frame(screen)
    main_frame.pack(fill=BOTH,expand=1)
    mycanvas=Canvas(main_frame)
    mycanvas.pack(side="left",fill=BOTH,expand=1)
    #ADD A SCROLLBAR
    myscroll=Scrollbar(main_frame,orient=VERTICAL,command=mycanvas.yview)
    myscroll.pack(side="right",fill=Y)
    #configure the canvas
    mycanvas.configure(yscrollcommand=myscroll.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox("all")))
    return mycanvas
page=Tk()
def que1(y):
        print("haha")
        print("inside question1 function")
        file=open("shruti.txt","a")
        file.write("\n***Blood Pressure Testt***\n")
        file.close()
        
        if(y.get()=="below90"):
                file=open("shruti.txt","a")
                file.write("BLOOD PRESSURE RANGE (systolic/Diatolic)(mm/Kg):  below-90\n")
                file.write("level:LOW\n")
                file.write("following is the precautions for you below\n1)Avoid Alcohol \n2)Drink More Water\n3)Eat More Salt \n4)Balanced Diet(increase zinc, calcium, spinach, milk intake)\n5)Avoid Caffeine Intake") 
                file.close()
        elif(y.get()=="90-140"):
                file=open("shruti.txt","a")
                file.write("BLOOD PRESSURE RANGE (systolic/Diatolic)(mm/Kg): 90-140\n")
                file.write("level:ELEVATED\n")
                file.write("Following are the precautions for you\n1)Proper Diet\n2)Avoid eating More Salt\n3)Drink Water alot\n4)Avoid Alcohol\n")
                file.close()
        elif(y.get()=="140-190"):
                file=open("shruti.txt","a")
                file.write("BLOOD PRESSURE RANGE (systolic/Diatolic)(mm/Kg): 140-190\n")
                file.write("level:HIGH\n")
                file.write("following are the precautions for you\n1)Lose Weight \n2)Do Regular Exercise\n3)Avoid Alcohol\n4)Limit Salt Consumption\n5)Manage Stress\n")
                file.close()
def que2(y):
        file=open("shruti.txt","a")
        file.write("\n\n***SKIN  TEST***")
        file.close()
        if(y.get()=="yes"):
                file=open("shruti.txt","a")
                file.write("\nRashes on Skin : yes\n")
                file.write("following are the precautions for you below\n1)Use gentle cleansers.\n2)Avoid applying cosmetic lotions or ointments directly on the rash\n3)Stop using any recently added cosmetics or lotions\n4)Avoid scrubbing your skin\n")
                file.close()
        elif(y.get()=="NO"):
                file=open("shruti.txt","a")
                file.write("Rashes on Skin : No\n")
                file.close()
                
def que3(y):
        
        if(y.get()=="yes"):
                
                file=open("shruti.txt","a")
                file.write("\nOily Skin: yes\n")
                file.write("following are the Precautions for you below\n1)Stay Hydrated by Drinking Enough Water \n2)Apply Good mMisturizers\n3)Avoid Using Harsh Products \n4)Reduce Stress By proper Exercise\n")
                file.close()
                
        elif(y.get()=="NO"):
                file=open("shruti.txt","a")
                file.write("oily Skin : No\n")
                file.close()
def que4(y):
        if(y.get()=="yes"):
                file=open("shruti.txt","a")
                file.write("\nSpots on Skin : yes\n")
                file.write("folowing are the precautions for you as below\n1)Keep Your Face Clean 2)Follow Good Diet Plan \n3)Avoid Directly Exposed To sunlight \n4)Avoid Touching face Frequently")
                file.close()
                print("suiiiiii")
        elif(y.get()=="NO"):
                file=open("shruti.txt","a")
                file.write("Spot on Skin : No\n")
                file.close()
                print("hahahaha")
def que5(y):
        file=open("shruti.txt","a")
        file.write("\n\n****CHOLESTROL LEVEL TEST***\n")
        file.close()
        if(y.get()=="below-200"):
                file=open("shruti.txt","a")
                file.write("You Have Normal Cholestrol Level")
                file.close()
                
        elif(y.get()=="200-239"):
                file=open("shruti.txt","a")
                file.write("you have moderate cholestrol \n precautions for you below\n 1)exercise\n 2)maintain healthy weight\n 3)substitute your oil\n 4)eat fruits,nuts,vegetables\n")
                file.close()
        elif(y.get()=="240-above"):
                file=open("shruti.txt","a")
                file.write("you have high cholestrol \n precautions for you below\n 1)doctor advice\n 2)yoga\n 3)quit smoking\n 4)manage stress")
                file.close()
               
def que6(y):
        file=open("shruti.txt","a")
        file.write("\n\n***CLEANLINESS TEST***\n")
        file.close()
        
        if(y.get()=="regular"):
                file=open("shruti.txt","a")
                file.write("Self-Clealiness:Better\n")
                file.close()
                print("hello world")
        elif(y.get()=="2-3"):
                file=open("shruti.txt","a")
                file.write("Self-Clealiness:NEED TO IMPROVE\n")
                file.close()
                print("no bath 2 -3 times")
                
        elif(y.get()=="less 2"):
                file=open("shruti.txt","a")
                file.write("self-cleanliness:VERY BAD.NEED TO IMPROVE\n")
                file.close()
                print("no bath at all")
                
def que7(y,x):
        file=open("shruti.txt","a")
        file.write("\n\n***PHYSICAL FITNESS TEST***\n")
        result=y.get()/(x.get()* x.get())
        if(result<18.5):
                 file=open("shruti.txt","a")
                 file.write("your are under weight\n")
                 file.write("precautions for you below\n 1)adding snacks \n2)several small means a day\n 3)eating high nutrients food\n")
                 file.close()
        elif(result>18.5 and result<24.9):
                
                file=open("shruti.txt","a")
                file.write("you are normal weighted\n")
                file.write("precautions for you below\n 1)keep having good nutrient food 2)daily yoga 3)having luch,dinner at proper time\n")
                file.close()
        elif(result>25):
                
                file=open("shruti.txt","a")
                file.write("you are ovr weighted\n")
                file.write("precautions for you below\n 1)exercise \n2)daily running \n3)low calories food \n4)proper diet\n")
                file.close()
                
                
                
                
                
        
def que8(y):
        file=open("shruti.txt","a")
        file.write("\n\n***SUGAR TEST***\n")
        file.write("Before Eating(fasting)\n")
        file.close()
        
        if(y.get()=="80-100"):
                file=open("shruti.txt","a")
                file.write("SUGAR LEVEL: LOW\n")
                file.close()
                print("you selected 80-100")
        elif(y.get()=="101-125"):
                file=open("shruti.txt","a")
                file.write("SUGAR LEVEL: ELEVATED(medium)\n")
                file.close()
                
                print("you selected between 101-125")
        elif(y.get()=="126-above"):
                file=open("shruti.txt","a")
                file.write("SUGAR LEVEL: HIGH\n")
                file.close()
                print("you selected  126 and above")
def que9(y):
        
        file=open("shruti.txt","a")
        file.write("***SUGAR TEST***\n")
        file.write("(After Eating)\n")
        file.close()
        if(y.get()=="170-200"):
                file=open("shruti.txt","a")
                file.write("SUGAR LEVEL: LOW\n")
                file.close()
                print("you selected 170-200")
        elif(y.get()=="190-230"):
                file=open("shruti.txt","a")
                file.write("SUGAR LEVEL : ELEVATED(medium)\n")
                file.write("following  are the precautions for you \n1)lose weight\n 2)Eat health diet\n 3)Do physical exercise\n 4)take regular oppointment")
                file.close()
                print("you selected between 190-230")
        elif(y.get()=="220-300"):
                file=open("shruti.txt","a")
                file.write("SUGAR LEVEL: HIGH\n")
                file.write("following are the precautions for you\n 1)keep your vaccine uptodate \n 2)pay attention to you feet\n 3)consider daily asprin\n 4)take care of your teeth")
                file.close()
                print("you selected  220 and above")
def funny():
        f21=Frame(root,bg="white")
        f21.pack(side="top")
        a=Label(text="Your Health Report Card  is stored in shruti.txt file in your file Manager.\n Thanks For Your Time.",font="TimesNewRoman 13 bold")
        a.pack(side="top")

def gender(hello,hii,yes):
        
       
        if(hello.get()=="no" and hii.get()=="no" and yes.get()=="no"):
                f=Frame(root,bg="white")
                f.pack(side="top")
                tx=Label(f,text="please choose any gender option to continue or proceed",font="TimesNewRoman 10 bold",fg="red")
                tx.pack(side="top")
        elif((hello.get()=="male" and hii.get()=="female") or  (yes.get()=="other" and hii.get()=="female")or (hello.get()=="male" and yes.get()=="other")):
                f=Frame(root,bg="white")
                f.pack(side="top")
                l=Label(f,text="please enter only one option for the given gender option",font="TimesNewRoman 10 bold",fg="red")
                l.pack(side="top")
        elif(hello.get()=="male" or hii.get()=="female"or yes.get()=="other"):
                root=Frame(x)
                x.create_window((0,0),window=root,anchor="nw")
                f=Frame(root,bg="white")
                f.pack(side="top")
                l1=Label(f,text="***please Give me a small test for Calculating your current health status***",font="TimesNewRoman 11 bold")
                l1.pack(side="top")
                #question 1
                l2=Label(f,text="1)what is your Blood pressure Range(systolic/Diatolic)(mm/kg)",fg="black",font="TimesNewRoman 10 bold")
                l2.pack(side="top")
                bp=StringVar()
                check1=Checkbutton(f,text="Below 90",onvalue="below90",offvalue="no",variable=bp,command=lambda:que1(bp))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f,text="90-140",onvalue="90-140",offvalue="no",variable=bp,command=lambda:que1(bp))
                check2.pack(side="left",padx="50")
                check2.deselect()
                check3=Checkbutton(f,text="140-190",onvalue="140-190",offvalue="no",variable=bp,command=lambda:que1(bp))
                check3.pack(side="left",padx="20")
                check3.deselect()
                #question 2
                f2=Frame(root,bg="white")
                f2.pack(side="top")
                l3=Label(f2,text="2)Do you have Rashes on Skin",fg="black",font="TimesNewRoman 10 bold")
                l3.pack(side="top")
                sk=StringVar()
                check1=Checkbutton(f2,text="yes",onvalue="yes",offvalue="no",variable=sk,command=lambda:que2(sk))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f2,text="No",onvalue="NO",offvalue="no",variable=sk,command=lambda:que2(sk))
                check2.pack(side="left",padx="50")
                check2.deselect()
                #question 3
                f3=Frame(root,bg="white")
                f3.pack(side="top")
                l4=Label(f3,text="3)Do you have Oily Skin",fg="black",font="TimesNewRoman 10 bold")
                l4.pack(side="top")
                oil=StringVar()
                check1=Checkbutton(f3,text="yes",onvalue="yes",offvalue="no",variable=oil,command=lambda:que3(oil))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f3,text="No",onvalue="NO",offvalue="no",variable=oil,command=lambda:que3(oil))
                check2.pack(side="left",padx="50")
                check2.deselect()
                #question 4
                f4=Frame(root,bg="white")
                f4.pack(side="top")
                l5=Label(f4,text="4)Do you Have spots on the skin(yes/no):",fg="black",font="TimesNewRoman 10 bold")
                l5.pack(side="top")
                spot=StringVar()
                check1=Checkbutton(f4,text="yes",onvalue="yes",offvalue="no",variable=spot,command=lambda:que4(spot))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f4,text="No",onvalue="NO",offvalue="no",variable=spot,command=lambda:que4(spot))
                check2.pack(side="left",padx="50")
                check2.deselect()
                #question 5
                f5=Frame(root,bg="white")
                f5.pack(side="top")
                l6=Label(f5,text="5)what is your cholestrol Range:",fg="black",font="TimesNewRoman 10 bold")
                l6.pack(side="top")
                choles=StringVar()
                check11=Checkbutton(f5,text="below-200",onvalue="below-200",offvalue="no",variable=choles,command=lambda:que5(choles))
                check11.pack(side="left",padx="70")
                check11.deselect()
                check21=Checkbutton(f5,text="200-239",onvalue="200-239",offvalue="no",variable=choles,command=lambda:que5(choles))
                check21.pack(side="left",padx="50")
                check21.deselect()
                check31=Checkbutton(f5,text="240-above",onvalue="240-above",offvalue="no",variable=choles,command=lambda:que5(choles))
                check31.pack(side="left",padx="50")
                check31.deselect()
                #question 6
                f6=Frame(root,bg="white")
                f6.pack(side="top")
                l7=Label(f6,text="6)How many times you bath a week",fg="black",font="TimesNewRoman 10 bold")
                l7.pack(side="top")
                bath=StringVar()
                check1=Checkbutton(f6,text="Regular Per Day",onvalue="regular",offvalue="no",variable=bath,command=lambda:que6(bath))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f6,text="two-three times",onvalue="2-3",offvalue="no",variable=bath,command=lambda:que6(bath))
                check2.pack(side="left",padx="50")
                check2.deselect()
                check3=Checkbutton(f6,text="Less than Two",onvalue="less 2",offvalue="no",variable=bath,command=lambda:que6(bath))
                check3.pack(side="left",padx="50")
                check3.deselect()
                #question 7
                f7=Frame(root,bg="white")
                f7.pack(side="top")
                li=Label(f7,text="7)Let us Calculate body mass index of yours",font="TimesNewRoman 10 bold",fg="blue")
                li.pack(side="top")
                f8=Frame(root,bg="white")
                f8.pack(side="top")
                l8=Label(f8,text="what is your weight(kg only)",fg="green")
                l8.pack(side="left")
                weight=DoubleVar()
                en=Entry(f8,textvariable=weight,bg="grey")
                en.pack(side="left")
                f9=Frame(root,bg="white")
                f9.pack(side="top")
                l8=Label(f9,text="what is your height(metre only)",fg="green")
                l8.pack(side="left")
                height=DoubleVar()
                en=Entry(f9,textvariable=height,bg="grey")
                en.pack(side="left")
                f10=Frame(root,bg="white")
                f10.pack(side="top")
                l111=Label(f10,text="Please Click on the result button to calculate your BMI",fg="red")
                l111.pack(side="top")
                bi=Button(f10,text="result",command=lambda:que7(weight,height))
                bi.pack(side="top")
                #question 8
                f10=Frame(root,bg="white")
                f10.pack(side="top")
                l9=Label(f10,text="8)please choose your sugar range (before eating)(mg/dl)",fg="black",font="TimesNewRoman 10 bold")
                l9.pack(side="top")
                besugar=StringVar()
                check1=Checkbutton(f10,text="80-100",onvalue="80-100",offvalue="no",variable=besugar,command=lambda:que8(besugar))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f10,text="101-125",onvalue="101-125",offvalue="no",variable=besugar,command=lambda:que8(besugar))
                check2.pack(side="left",padx="50")
                check2.deselect()
                check3=Checkbutton(f10,text="126-above",onvalue="126-above",offvalue="no",variable=besugar,command=lambda:que8(besugar))
                check3.pack(side="left",padx="50")
                check3.deselect()
                #question 9
                f11=Frame(root,bg="white")
                f11.pack(side="top")
                l10=Label(f11,text="9)please choose your sugar range (after eating)(mg/dl)",fg="black",font="TimesNewRoman 10 bold")
                l10.pack(side="top")
                afsugar=StringVar()
                check1=Checkbutton(f11,text="170-200",onvalue="170-200",offvalue="no",variable=afsugar,command=lambda:que9(afsugar))
                check1.pack(side="left",padx="70")
                check1.deselect()
                check2=Checkbutton(f11,text="190-230",onvalue="190-230",offvalue="no",variable=afsugar,command=lambda:que9(afsugar))
                check2.pack(side="left",padx="50")
                check2.deselect()
                check3=Checkbutton(f11,text="220-300",onvalue="220-300",offvalue="no",variable=afsugar,command=lambda:que9(afsugar))
                check3.pack(side="left",padx="50")
                check3.deselect()
                f28=Frame(root,bg="white")
                f28.pack(side="top")
                B1=Button(f28,text="Submit",command=funny)
                B1.pack(side="top")
                
                
                
def fun():
        file=open("shruti.txt","w")
        file.write("                                                                  Report card of Regular Health Checkup\n\n")
        file.close()
        var=var1.get()
        file=open("shruti.txt","a")
        file.write("\nName of the Person: "+ var)
        file.close()
        if(te.get("1.0","end-1c")==""):
                f11=Frame(root,bg="white")
                f11.pack(side="top")
                textt=Label(f11,text="please chhose any age the option to proceed",font="TimesNewRoman 7 bold",fg="red")
                textt.pack(side="top")
                
        elif(int(te.get("1.0","end-1c"))>30):
                file=open("shruti.txt","a")
                file.write("\n Age: Above 30")
                file.close()
                f3=Frame(root,bg="white")
                f3.pack(side="top")
                tex=Label(f3,text="please check your gender below:")
                tex.pack(side="top")
                f4=Frame(root,bg="white")
                f4.pack(side="top")
                genvar=StringVar()
                genvar1=StringVar()
                genvar2=StringVar()
                chk1=Checkbutton(f4,text="MALE",onvalue="male",offvalue="no",command=lambda:gender(genvar,genvar1,genvar2),variable=genvar)
                chk1.pack(side="left")
                chk1.deselect()
                chk2=Checkbutton(f4,text="FEMALE",onvalue="female",offvalue="no",command=lambda:gender(genvar,genvar1,genvar2),variable=genvar1)
                chk2.pack(side="left")
                chk2.deselect()
                chk3=Checkbutton(f4,text="OTHER",onvalue="other",offvalue="no",command=lambda:gender(genvar,genvar1,genvar2),variable=genvar2)
                chk3.pack(side="left")
                chk3.deselect()
        elif(int(te.get("1.0","end-1c"))<=30):
                file=open("shruti.txt","a")
                file.write("\nAge: Below 30 ")
                file.write("\n                                                              sorry you are not eligible for the regular checkup ")
                file.write("\n                                                                           Unable to save data")
                file.close()
                f5=Frame(root,bg="white")
                f5.pack(side="top")
                la=Label(f5,text="Your age should be greater than 30 to check your health",font="TimesNewRoman 12 bold",fg="red")
                la.pack(side="top")



headline=Label(text="PROGRAM TO CHECK THE REGULAR CHECKUP OF PERSON",font="TimesNewRoman 14 bold")
headline.pack()
page.geometry("1000x800")
page.minsize(1000,800)
page.maxsize(1000,800)
#file=open("shruti.txt","w")
#file.write("                                                      Report card of Regular Health Checkup\n\n")
#file.close()
page.title("HealthReportCard")
x=scroll_screen(page)
global root
root=Frame(x)
x.create_window((0,0),window=root,anchor="nw")
f1=Frame(root,bg="white")
f1.pack(side="top",padx=300)
text2=Label(f1,text="please enter your name : ")
text2.pack(side="left")
var1=StringVar()
input1=Entry(f1,textvariable=var1)
input1.pack(side="left")
f2=Frame(root,bg="white")
f2.pack(side="top",pady=20)
text3=Label(f2,text="what is your age  :" )
text3.pack(side="top")
te=Text(f2,height=1,width=20,fg="black",relief=SUNKEN)
te.pack(side="top")
bu=Button(f2,command=fun,text="proceed to next",)
bu.pack(side="top",pady=10)
root.mainloop()
