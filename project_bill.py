from tkinter import*
import math, random
from tkinter import messagebox
import os
class Bill_Page:
        def __init__(self, root):
               self.root = root
               self.root.geometry('1350x800')
               self.root.title('Billing Page')
               bg_color='black'
               title = Label(self.root, text = 'Billing Page', bd=12, relief = GROOVE,bg =bg_color,fg = 'white',font = ('times new roman', 30, 'bold'), pady=2).pack(fill=X)

         #---------------Variables-----------------------------------
         #-------------cosmetics---------------------------
               self.soap=IntVar()
               self.face_cream=IntVar()
               self.face_wash=IntVar()
               self.spray=IntVar()
               self.gell=IntVar()
               self.loshan=IntVar()

         #----------------grocery----------------------------
               self.rice=IntVar()
               self.food_oil=IntVar()
               self.daal=IntVar()
               self.wheat=IntVar()
               self.sugar=IntVar()
               self.tea=IntVar()

         #-----------------Cold Drinks-------------------
               self.maza=IntVar()
               self.coke=IntVar()
               self.frooti=IntVar()
               self.thumbsup=IntVar()
               self.limca=IntVar()
               self.sprite=IntVar()

         #-------------Total Product Price and Tax Variable-------
               self.cosmetics_price=StringVar()
               self.grocery_price=StringVar()
               self.cold_drink_price=StringVar()

               self.cosmetics_tax=StringVar()
               self.grocery_tax=StringVar()
               self.cold_drink_tax=StringVar()

         #--------------customer-------------------------
               self.c_name=StringVar()
               self.c_phon=StringVar()

               self.bill_no=StringVar()
               x=random.randint(1000,9999)
               self.bill_no.set(str(x))

               self.search_bill=StringVar()

         #-------------------Customer Detail Frame--------------------
               F1=LabelFrame(self.root,bd=10,relief=GROOVE,text='Customer Details', font=('times new roman',15,'bold'),fg='gold',bg=bg_color)
               F1.place(x=0,y=75,relwidth=1)

               cname_lbl=Label(F1,text='Customer Name',bg=bg_color,fg='white',font=('times new roman',18,'bold')).grid(row=0,column=0,padx=20,pady=5)
               cname_txt=Entry(F1,width=15,textvariable=self.c_name,font='arial 15',bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

               cphn_lbl=Label(F1,text='Phone No.',bg=bg_color,fg='white',font=('times new roman',18,'bold')).grid(row=0,column=2,padx=20,pady=5)
               cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font='arial 15',bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

               c_bill_lbl=Label(F1,text='Bill Number',bg=bg_color,fg='white',font=('times new roman',18,'bold')).grid(row=0,column=4,padx=20,pady=5)
               c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font='arial 15',bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)        

               bill_btn=Button(F1,text='Search',command=self.find_bill,width=10,bd=7,font='arial 12 bold').grid(row=0,column=6, pady=10,padx=10)
         #-----------------Cosmetics Frame--------------------
               F2=LabelFrame(self.root,bd=10,relief=GROOVE,text='Cosmetics',font=('times new roman', 18,'bold'),fg='gold',bg=bg_color)
               F2.place(x=5,y=175,width=325,height=475)

               bath_lbl=Label(F2,text='Bath Soap\nRs.40',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='W')
               bath_txt=Entry(F2,width=10,textvariable=self.soap,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

               Face_cream_lbl=Label(F2,text='Face Cream\nRs.120',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky='W')
               Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

               Face_w_lbl=Label(F2,text='Face Wash\nRs.60',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky='W')
               Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

               Hair_s_lbl=Label(F2,text='Hair Spray\nRs.180',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky='W')
               Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

               Hair_g_lbl=Label(F2,text='Hair Gel\nRs.140',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky='W')
               Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

               Body_lbl=Label(F2,text='Body Loshan\nRs.180',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky='W')
               Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #-----------------Grocery Products--------------------
               F3=LabelFrame(self.root,bd=10,relief=GROOVE,text='Grocery',font=('times new roman', 18,'bold'),fg='gold',bg=bg_color)
               F3.place(x=340,y=175,width=325,height=475)

               g1_lbl=Label(F3,text='Rice\nRs.80/Kg',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='W')
               g1_txt=Entry(F3,width=10,textvariable=self.rice,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

               g2_lbl=Label(F3,text='Food Oil\nRs.120/ltr',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky='W')
               g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

               g3_lbl=Label(F3,text='Daal\nRs.45/Kg',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky='W')
               g3_txt=Entry(F3,width=10,textvariable=self.daal,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

               g4_lbl=Label(F3,text='Wheat\nRs.60/kg',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky='W')
               g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

               g5_lbl=Label(F3,text='Sugar\nRs.46/kg',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky='W')
               g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

               g6_lbl=Label(F3,text='Tea\nRs.190/kg',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky='W')
               g6_txt=Entry(F3,width=10,textvariable=self.tea,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


         #---------------Cold Drink Frame--------------------
               F4=LabelFrame(self.root,bd=10,relief=GROOVE,text='Cold Drinks',font=('times new roman', 18,'bold'),fg='gold',bg=bg_color)
               F4.place(x=670,y=175,width=325,height=475)

               c1_lbl=Label(F4,text='Maza\nRs.30',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky='W')
               c1_txt=Entry(F4,width=10,textvariable=self.maza,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

               c2_lbl=Label(F4,text='Coke\nRs.30',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky='W')
               c2_txt=Entry(F4,width=10,textvariable=self.coke,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

               c3_lbl=Label(F4,text='Frooti\nRs.20',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky='W')
               c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

               c4_lbl=Label(F4,text='Thumbs Up\nRs.30',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky='W')
               c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

               c5_lbl=Label(F4,text='Limca\nRs.60',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky='W')
               c5_txt=Entry(F4,width=10,textvariable=self.limca,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
 
               c6_lbl=Label(F4,text='Sprite\nRs.60',font=('times new roman',16,'bold'),bg=bg_color,fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky='W')
               c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=('times new roman',16,'bold'),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #-------------Bill Area Frame---------------------
               F5=Frame(self.root,bd=10,relief=GROOVE)
               F5.place(x=1005,y=175,width=350,height=475)

               bill_title=Label(F5,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
               scrol_y=Scrollbar(F5,orient=VERTICAL)
               self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
               scrol_y.pack(side=RIGHT,fill=Y)
               scrol_y.config(command=self.txtarea.yview)
               self.txtarea.pack(fill=BOTH, expand=1)


         #------------------------Button frame-------------------------
               F6=LabelFrame(self.root,bd=10,relief=GROOVE,text='Bill Menu',font=('times new roman', 18,'bold'),fg='gold',bg=bg_color)
               F6.place(x=0,y=650,relwidth=1,height=140)
               m1_lbl=Label(F6,text='Total Cosmetics Price',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='W')
               m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

               m2_lbl=Label(F6,text='Total Grocery Price',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='W')
               m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

               m3_lbl=Label(F6,text='Total Cold Drinks Price',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='W')
               m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

               c1_lbl=Label(F6,text='Cosmetics Tax',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='W')
               c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

               c2_lbl=Label(F6,text='Grocery Tax',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='W')
               c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

               c3_lbl=Label(F6,text='Cold Drinks Tax',bg=bg_color,fg='white',font=('times new roman',14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='W')
               c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
 
               btn_f=Frame(F6,bd=7,relief=GROOVE)
               btn_f.place(x=750,width=580,height=105)

               total_btn=Button(btn_f,command=self.total,text='Total',bg='cadetblue',fg='white',width=10,font='arial 15 bold',pady=15,bd=2).grid(row=0,column=0,padx=5,pady=5)
               GBill_btn=Button(btn_f,command=self.bill_area,text='Generate Bill',bg='cadetblue',fg='white',width=10,font='arial 15 bold',pady=15,bd=2).grid(row=0,column=1,padx=5,pady=5)
               Clear_btn=Button(btn_f,text='Clear',command=self.clear_data,bg='cadetblue',fg='white',width=10,font='arial 15 bold',pady=15,bd=2).grid(row=0,column=2,padx=5,pady=5)
               Exit_btn=Button(btn_f,text='Exit',command=self.Exit_Page,bg='cadetblue',fg='white',width=10,font='arial 15 bold',pady=15,bd=2).grid(row=0,column=3,padx=5,pady=5)
               self.welcome_bill()

        def total(self):
               self.c_s_p=self.soap.get()*40
               self.c_fc_p=self.face_cream.get()*120
               self.c_fw_p=self.face_wash.get()*60
               self.c_sp_p=self.spray.get()*180
               self.c_g_p=self.gell.get()*140
               self.c_l_p=self.loshan.get()*180
               self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_sp_p+
                                    self.c_g_p+
                                    self.c_l_p
                                    )  
               self.cosmetics_price.set('Rs. '+str(self.total_cosmetic_price))
               self.c_tax=round((self.total_cosmetic_price*0.05),2)
               self.cosmetics_tax.set('Rs. '+str(self.c_tax))

               self.g_r_p=self.rice.get()*80
               self.g_f_p=self.food_oil.get()*120
               self.g_d_p=self.daal.get()*45
               self.g_w_p=self.wheat.get()*60
               self.g_s_p=self.sugar.get()*46
               self.g_t_p=self.tea.get()*190
               self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )  
               self.grocery_price.set('Rs. '+str(self.total_grocery_price))
               self.g_tax=round((self.total_grocery_price*0.1),2)
               self.grocery_tax.set('Rs. '+str(self.g_tax))

               self.d_m_p=self.maza.get()*30
               self.d_c_p=self.coke.get()*30
               self.d_f_p=self.frooti.get()*20
               self.d_t_p=self.thumbsup.get()*30
               self.d_l_p=self.limca.get()*60
               self.d_s_p=self.sprite.get()*60
               self.total_drink_price=float(
                                    self.d_m_p+
                                    self.d_c_p+
                                    self.d_f_p+
                                    self.d_t_p+
                                    self.d_l_p+
                                    self.d_s_p
                                    )  
               self.cold_drink_price.set('Rs. '+str(self.total_drink_price))
               self.d_tax=round((self.total_drink_price*0.05),2)
               self.cold_drink_tax.set('Rs. '+str(self.d_tax))

               self.Total_bill=float(self.total_cosmetic_price+
                                     self.total_grocery_price+
                                     self.total_drink_price+
                                     self.c_tax+
                                     self.g_tax+
                                     self.d_tax
                                     )
        def welcome_bill(self):
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\tWelcome\n')
                self.txtarea.insert(END,f'\n Bill Number : {self.bill_no.get()}')
                self.txtarea.insert(END,f'\n Customer name : {self.c_name.get()}')
                self.txtarea.insert(END,f'\n Phone Number : {self.c_phon.get()}')
                self.txtarea.insert(END,'\n======================================')
                self.txtarea.insert(END,'\n Products\t\tQTY\t\tPrice')
                self.txtarea.insert(END,'\n======================================')
        def bill_area(self):
                self.length=len(self.c_phon.get())
                if self.c_name.get()=='' or self.c_phon.get()=='':
                        messagebox.showerror('Error','Customer details are must')
                elif self.c_name.get()=='' or self.length!=10:
                        messagebox.showerror('Error','Enter correct phone no.')
                elif self.cosmetics_price.get()=='Rs. 0.0' and self.grocery_price.get()=='Rs. 0.0' and self.cold_drink_price.get()=='Rs. 0.0':
                        messagebox.showerror('Error','No product purchased')
                else:
                        self.welcome_bill()
                        #-----cosmetics-----------
                        if self.soap.get()!=0:
                                self.txtarea.insert(END,f'\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}')
                        if self.face_cream.get()!=0:
                                self.txtarea.insert(END,f'\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}')
                        if self.face_wash.get()!=0:
                                self.txtarea.insert(END,f'\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}')
                        if self.spray.get()!=0:
                                self.txtarea.insert(END,f'\n Spray\t\t{self.spray.get()}\t\t{self.c_s_p}')
                        if self.gell.get()!=0:
                                self.txtarea.insert(END,f'\n Hair Gel\t\t{self.gell.get()}\t\t{self.c_g_p}')
                        if self.loshan.get()!=0:
                                self.txtarea.insert(END,f'\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_l_p}')
                        
                        #----------grocery------------
                        if self.rice.get()!=0:
                                self.txtarea.insert(END,f'\n Rice\t\t{(self.rice.get())}Kg\t\t{self.g_r_p}')
                        if self.food_oil.get()!=0:
                                self.txtarea.insert(END,f'\n Food Oil\t\t{self.food_oil.get()}Ltr\t\t{self.g_f_p}')
                        if self.daal.get()!=0:
                                self.txtarea.insert(END,f'\n Daal\t\t{self.daal.get()}Kg\t\t{self.g_d_p}')
                        if self.wheat.get()!=0:
                                self.txtarea.insert(END,f'\n Wheat\t\t{self.wheat.get()}Kg\t\t{self.g_w_p}')
                        if self.sugar.get()!=0:
                                self.txtarea.insert(END,f'\n Sugar\t\t{self.sugar.get()}Kg\t\t{self.g_s_p}')
                        if self.tea.get()!=0:
                                self.txtarea.insert(END,f'\n Tea\t\t{self.tea.get()}Kg\t\t{self.g_t_p}')

                        #----------cold drinks-------
                        if self.maza.get()!=0:
                                self.txtarea.insert(END,f'\n Mazaa\t\t{self.maza.get()}\t\t{self.d_m_p}')
                        if self.coke.get()!=0:
                                self.txtarea.insert(END,f'\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}')
                        if self.frooti.get()!=0:
                                self.txtarea.insert(END,f'\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}')
                        if self.thumbsup.get()!=0:
                                self.txtarea.insert(END,f'\n Thumbsup\t\t{self.thumbsup.get()}\t\t{self.d_t_p}')
                        if self.limca.get()!=0:
                                self.txtarea.insert(END,f'\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}')
                        if self.sprite.get()!=0:
                                self.txtarea.insert(END,f'\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}')

                        self.txtarea.insert(END,'\n--------------------------------------')
                        if self.cosmetics_tax.get()!='Rs. 0.0':
                                self.txtarea.insert(END,f'\n Cosmetics Tax\t\t\t{self.cosmetics_tax.get()}')
                        if self.grocery_tax.get()!='Rs. 0.0':
                                self.txtarea.insert(END,f'\n Grocery Tax\t\t\t{self.grocery_tax.get()}')
                        if self.cold_drink_tax.get()!='Rs. 0.0':
                                self.txtarea.insert(END,f'\n Cold Drink Tax\t\t\t{self.cold_drink_tax.get()}')
                        
                        self.txtarea.insert(END,f'\n Total Bill :\t\t\tRs. {str(self.Total_bill)}')
                        self.txtarea.insert(END,'\n--------------------------------------')
                        self.save_bil()

        def save_bil(self):
                op=messagebox.askyesno('Save Bill','You want to save bill')
                if op>0:
                        self.bill_data=self.txtarea.get('1.0', END)   
                        f1=open('bills/'+str(self.bill_no.get())+'.txt','w')
                        f1.write(self.bill_data)
                        f1.close()   
                        messagebox.showinfo('Saved',f'Bill {self.bill_no.get()} save sucessfully')
                else:
                        return 

        def find_bill(self):
                present='no'
                for i in os.listdir('bills/'):
                        if i.split('.')[0]==self.search_bill.get():
                                f1=open(f'bills/{i}','r')
                                self.txtarea.delete('1.0',END)
                                for d in f1:
                                        self.txtarea.insert(END,d)
                                f1.close()
                                present='yes'
                if present=='no':
                        messagebox.showerror('Error','Invalid Bill no.')
                        
        def clear_data(self):
                op=messagebox.askyesno('Clear','Do you really want to clear data')
                if op>0:
                        #-------------cosmetics---------------------------
                        self.soap.set(0)
                        self.face_cream.set(0)
                        self.face_wash.set(0)
                        self.spray.set(0)
                        self.gell.set(0)
                        self.loshan.set(0)

                        #----------------grocery----------------------------
                        self.rice.set(0)
                        self.food_oil.set(0)
                        self.daal.set(0)
                        self.wheat.set(0)
                        self.sugar.set(0)
                        self.tea.set(0)

                        #-----------------Cold Drinks-------------------
                        self.maza.set(0)
                        self.coke.set(0)
                        self.frooti.set(0)
                        self.thumbsup.set(0)
                        self.limca.set(0)
                        self.sprite.set(0)

                        #-------------Total Product Price and Tax Variable-------
                        self.cosmetics_price.set('')
                        self.grocery_price.set('')
                        self.cold_drink_price.set('')

                        self.cosmetics_tax.set('')
                        self.grocery_tax.set('')
                        self.cold_drink_tax.set('')

                        #--------------customer-------------------------
                        self.c_name.set('')
                        self.c_phon.set('')

                        self.bill_no.set('')
                        x=random.randint(1000,9999)
                        self.bill_no.set(str(x))

                        self.search_bill.set('')  
                        self.welcome_bill()

        def Exit_Page(self):
                op=messagebox.askyesno('Exit','Do you really want to exit')
                if op>0:
                        self.root.destroy()
                
                                
root = Tk()
obj = Bill_Page(root)
root.mainloop()
