'''

'''

#--------------Import--------------
# Getting current date from import date function from datetime module
from datetime import date
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



# ____________   FUNCTIONS ________________
def find_perimeter(l,w,):
    # find the perimeter ( Total of all lengths )
    perimeter = lengths.width((lengths.width)<(l,w))
    return perimeter
def display_calc_perimeter(perimeter):
  tbox_perimeter.config(state='normal')

   # gets the three entries
  l=int(input("Length : "))
w=int(input("Width : "))
area=l*w
perimeter=2*(l+w)
print("Area of Rectangle : ",area)
print("Perimeter of Rectangle : ",perimeter)

  # find the perimeter ( total of dimensions ) perimeter = lengths.width<(l,w))
tbox_age.config(state='normal')
   #perimeter calculated is inserted into the text box after clearing the previous info in the textbox. 
tbox_perimeter.delete('1.0', tk.END)
tbox_perimeter.insert(tk.END,perimeter)
tbox_age.config(state='disabled')



def validation():
  # gets the three entries
  l = e_lenght.get()
  w = e_width.current()
  
  msg = ''

# ____________   MAIN  ________________
 # Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="Area and Perimeter calculator!",font=("Arial", 20),fg="black",bg="#F7DC6F")
lb_subheading = tk.Label(window,font=("Arial",12),text="Enter your dimensions which includes the width and length.",fg="black",bg="#F7DC6F")
 
  
 
  # Labels for date, month and year
lb_date = tk.Label(window,text = "width: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F"
lb_month = tk.Label(window,text = "length:",font= ("Arial",12,"bold"),fg="darkgreen",bg="#F7DC6F)
lb_year = tk.Label(window,text = "perimeter: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
tbox_perimeter.tk.Label()