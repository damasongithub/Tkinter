# first we import tkinter
import tkinter
from tkinter import ttk # this is a collection of themed widgets that help to creat modern application using tkinter( things like the cobobox)
from tkinter import messagebox # this gives us a pop up message


#adding functionality to the interface
# we diffine a function
def enter_data():
    accepted=accept_var.get()

    if accepted=="Accepted":
        #user infor
        firstname=first_name_entry.get()
        lastname= last_name_entry.get()

        if firstname and lastname:
            title =title_combobox.get()
            age = age_spinbox.get()

            #Course info
            numcourses =numcourses_spinbox.get()
            registration_status = reg_status_var.get()


            print("First name:", firstname, "Last name:", lastname)
            print("Title:", title, "Age:", age)
            print("comlete course:", numcourses)
            print("Registration status:", registration_status)
            print("-------------------------------------------") #a sepsreter
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and Last name are required.")    
    else:
        tkinter.messagebox.showwarning(title= "Error", message= "you have not accepted the terms and conditions" )


window = tkinter.Tk()  #this is the root window, which is the perent window for all the widgets we will great
# we give a title to our window
window.title("Data Entry Form")


frame = tkinter.Frame(window) # so we just say, this frame is like a boxs that is inside the big boxs which is the window(the perant box or the big boxs)
# we pack the frame inside the window using the .pack() function
frame.pack()

#FIRST LABEL FRAME

# saving user info
# now we ceate a LabelFrame, we can say, label frames a small boxes that we put inside the "Frame" box which is inside the parrent box which is the window
user_info_frame = tkinter.LabelFrame(frame, text="User Information" ) # so the parent frame for this one will be "frame" not "window" becouse it is contained in the frame box
user_info_frame.grid(row=0 , column=0, padx=20 ,pady=10) # with the .grid() function unlike the .pack() function, it places wedges in rows and columns
#and another thing the padx and pady on the grid agument of the user_info_frame grid function helps our work to look more neat and not squashed in.(you can try to remove then you will see how the interface will look)

# now we place labels inside the labelFrame of the user_info_frame
first_name_label= tkinter.Label(user_info_frame, text="First Name") #this is the first name label inside the labelFrame at row=0 & coln=0
first_name_label.grid(row=0 , column=0)

last_name =tkinter.Label(user_info_frame, text="Last Name") # this is the last name lable at row=0 & colum=1 (which will appear next to the first name label)
last_name.grid(row=0, column=1)

#now we put in the entrys below the first name and last name label
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry= tkinter.Entry(user_info_frame)
# without the .grid() fanction these entrys wont apper on the interface so we run the following .grid function for each of the
first_name_entry.grid(row=1 , column=0)
last_name_entry.grid(row=1, column=1)

# we add a title label
title_label = tkinter.Label(user_info_frame, text= "Title")
title_combobox = ttk.Combobox(user_info_frame, values=[ "" ,"Mr","Mrs","Dr" ]) #the combobox doesnt exist in tkinter thats why we use ttk.combobox() insteard of the tkinter.combobox() function.
#we now place this on the interface with the .grid() function
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

# we add a spinbox for the age
age_label= tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100) # note we use the from of "from_" and not this "from"
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)
# you can creat a combobox for nationality on your own time

# now the widgets are not nicely spaced in the user_info_frame so for that we use the padding in the following command
for wedget in user_info_frame.winfo_children():  # the .winfo_children() function returns all the wedgets which are chidren of the widgets
    wedget.grid_configure(padx=5, pady=5)

#SECOND LABEL FRAME

#saving course info
course_frame = tkinter.LabelFrame(frame) #the parent box for this frame as well is the "frame"
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10) # the sticky="news" attribute in the function makes you it to expand in the north,east,west,south (news)

#now we put in the labels in the course info labelFrame
registered_label= tkinter.Label(course_frame, text= "Registration status") #the parent for this label is the course_frame
# for registration lable we creat a check button for it
reg_status_var= tkinter.StringVar(value="Not Registered") # the .stringVar is a function that enables us to store the values of a check box
registration_check = tkinter.Checkbutton(course_frame, text = "Currently Registered", variable=reg_status_var, onvalue="Registered" , offvalue="Not Registered" )
registered_label.grid(row=0, column= 0)
registration_check.grid(row= 1, column=0)

# number of completed courses spinbox
numcourses_label= tkinter.Label(course_frame, text="# completed courses")
numcourses_spinbox= tkinter.Spinbox(course_frame, from_= 0, to= 'infinity')
# we add them to the grid
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)
# you can add another colunmn of the spinbox

#now we space them
for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady= 5)

#THIRD LABEL FRAME 

#Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Condition")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var = tkinter.StringVar(value= "Not Accepted")
terms_check= tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#LASTLY THE ENTRY BUTTON
button = tkinter.Button(frame, text="Enter data", command= enter_data) # the "command= enter_data" attribute is a function that will allow us to "enter_data", enter_data is a function that we are going to diefine ourselves
button.grid(row=3, column=0, sticky="news", padx=20, pady=10 )



window.mainloop() #this is what will be running the application window every time you run the code








