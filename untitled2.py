#CourseProject

#test 3
#CourseProject

#DynamicsProblem

#Given:Coefficient of restitution(e), Velocity A1, Velocity B1, Mass 1, Mass 2, Angle A1, Angle B1

#Equations: e=(vB2-vA2)/(vA1-vB1), mAvA1i +mBvB1i = mAvA2i +mBvB2i
	      
#Find: Velocity A2 & B2 , Angle A2 & B2

#use GUI to ask user for the givens
#create window

import tkinter as tk
import math as m

def cal():
    M1 = float(m1.get())
    M2 = float(m2.get())
    v1 = float(V1.get())
    v2 = float(V2.get())
    A1 = float(a1.get())
    A2 = float(a2.get())
    E1 = float(e.get())
    
    va1x = v1*m.cos(A1)
    va1y = v1*m.sin(A1)
    vb1x = v2*m.cos(A2)
    vb1y = v2*m.sin(A2)
    
    va2x = (M1*va1x + M2*vb1x - M2*E1*(va1x-vb1x))/(M1+M2)
    vb2x = va2x + E1*(va1x-vb1x)
    
    va2y = va1y
    vb2y = vb1y
    
    va2 = m.sqrt(va2x**2 + va2y**2)
    vb2 = m.sqrt(vb2x**2 + vb2y**2)
    
    angle1 = m.atan(va2x/va2y)
    angle2 = m.atan(vb2x/vb2y)
    
    va2 = str(va2)
    vb2 = str(vb2)
    angle1 = str(angle1)
    angle2 = str(angle2)
    
    lbl8['text'] = 'Final Velocity 1: ' + va2
    lbl9['text'] = 'Final Velocity 2: ' + vb2
    lbl10['text'] = 'Final Angle 1: ' + angle1
    lbl11['text'] = 'Final Angle 2: ' + angle2


window = tk.Tk()
window.title('Collision Calculator')
window.geometry('500x300')
#create label 1 (Mass 1)
lbl1 = tk.Label(window,text='Mass 1: ')
lbl1.grid(row=0, column=0)
m1 = tk.Entry(window, width=15)
m1.grid(row=0, column=1)


#create label 2 (Mass 2)
lbl2 = tk.Label(window,text='Mass 2: ')
lbl2.grid(row=1, column=0)
m2 = tk.Entry(window, width=15)
m2.grid(row=1, column=1)


#create label 3 (Velocity 1)
lbl3 = tk.Label(window,text='Velocity 1: ')
lbl3.grid(row=2, column=0)
V1 = tk.Entry(window, width=15)
V1.grid(row=2, column=1)


#create label 4 (Velocity 2)
lbl4 = tk.Label(window,text='Velocity 2: ')
lbl4.grid(row=3, column=0)
V2 = tk.Entry(window, width=15)
V2.grid(row=3, column=1)


#create label 5 (Angle 1)
lbl5 = tk.Label(window,text='Angle 1: ')
lbl5.grid(row=4, column=0)
a1 = tk.Entry(window, width=15)
a1.grid(row=4, column=1)


#create label 6 (Angle 2)
lbl6 = tk.Label(window,text='Angle 2: ')
lbl6.grid(row=5, column=0)
a2 = tk.Entry(window, width=15)
a2.grid(row=5, column=1)

#create label 7 (coeiffecent of restituation)
lbl7 = tk.Label(window,text='Coeiffecent of restituation ')
lbl7.grid(row=6, column=0)
e = tk.Entry(window, width=15)
e.grid(row=6, column=1)

#create label 8 (Final Velocity 1)
lbl8 = tk.Label(window,text='Final Velocity 1: ')
lbl8.grid(row=8, column=0)

#create label 9 (Final Velocity 2)
lbl9 = tk.Label(window,text='Final Velocity 2: ')
lbl9.grid(row=9, column=0)

#create label 10 (Final Angle 1)
lbl10 = tk.Label(window,text='Final Angle 1: ')
lbl10.grid(row=10, column=0)

#create label 11 (Final Angle 2)
lbl11 = tk.Label(window,text='Final Angle 2: ')
lbl11.grid(row=11, column=0)

#create button to generate answers
btn = tk.Button(window, text='Calculate')
btn.grid(row=7,column=1)

#display GUI
window.mainloop()
