from tkinter import *
from tkinter import messagebox
import random
import smtplib
from twilio.rest import Client
import sms1
def send_otp_email():
  r=random.randrange(100,500)
  def otpmail():
     m=str(r)
     receiver_email=email_id.get()
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     sender_mail="Enter your email id"
     password="Enter account password"
     server.login(sender_mail,password)
     server.sendmail(sender_mail,receiver_email,m)
  def verifyotp():
      otp_1=otp.get()  
      if(otp_1==str(r)):
        messagebox.showinfo("show info", "login successful")
      else:
        messagebox.showerror("Error","OTP verifcation failed")
  def resendotp():
      otp_email.destroy()
      send_otp_email()
  otp_email=Toplevel()
  otp_email.geometry("500x400")
  otp_email.resizable(False,False)
  otp_email.title("w2")
  design1=Canvas(otp_email,bg="white",width=400,height=300)
  design1.place(x=50,y=70)
  title4=Label(otp_email,text="OTP Verification",font="30,bold")
  title4.place(x=175,y=25)
  title1=Label(otp_email,text="Email Id",font="40,bold",bg="white")
  title1.place(x=210,y=90)
  email_id=Entry(otp_email,font=("Calibri",15,"bold"),width=30,bd=4)
  email_id.place(x=100,y=130)
  sendotp=PhotoImage(file="sendotp.png")
  button1=Button(otp_email,image=sendotp,command=otpmail,border=0)
  button1.place(x=180,y=180)
  title2=Label(otp_email,text="OTP",font="30,bold",bg="white")
  title2.place(x=225,y=230)
  otp=Entry(otp_email,font=("Calibri",15,"bold"),width=20,bd=4)
  otp.place(x=146,y=270)
  verify=PhotoImage(file="verify.png")
  verfication=Button(otp_email,image=verify,command=verifyotp,border=0)
  verfication.place(x=170,y=320)
  resend_otp=PhotoImage(file="resendotp.png")
  resend=Button(otp_email,image=resend_otp, command=resendotp,border=0)
  resend.place(x=240,y=320)
  otp_email.mainloop()
def send_otp_phonenumber():
  r=random.randrange(100,500)
  def otp_phonenumber():
    d=number.get()
    m=str(r)
    client= Client(sms1.account_sid,sms1.auth_token)
    message=client.messages.create(
    body=m,
    from_=sms1.twilio_number,
    to=d
    )
  def verif_otp():
    otp_2=otp1.get()  
    if(otp_2==str(r)):
        messagebox.showinfo("show info", "login successful")
    else:
        messagebox.showerror("Error","OTP verifcation failed")
  def resendotp():
      otp_phon.destroy()
      send_otp_phonenumber()
  otp_phon=Toplevel()
  otp_phon.geometry("500x400")
  otp_phon.resizable(False,False)
  otp_phon.title("w2")
  design2=Canvas(otp_phon,bg="white",width=400,height=300)
  design2.place(x=50,y=70)
  title5=Label(otp_phon,text="OTP Verification",font="30,bold")
  title5.place(x=175,y=25)
  title2=Label(otp_phon,text="Enter the phone number",font="40",bg="white")
  title2.place(x=150,y=90)
  number=Entry(otp_phon,font=("Calibri",15,"bold"),width=30,bd=4)
  number.place(x=100,y=130)
  im=PhotoImage(file="sendotp.png")
  button2=Button(otp_phon,image=im,command=otp_phonenumber,border=0)
  button2.place(x=180,y=180)
  title3=Label(otp_phon,text="OTP",font="30,bold",bg="white")
  title3.place(x=225,y=230)
  otp1=Entry(otp_phon,font=("Calibri",15,"bold"),width=20,bd=4)
  otp1.place(x=146,y=270)
  ver1=PhotoImage(file="verify.png")
  verfication1=Button(otp_phon,image=ver1,command=verif_otp,border=0)
  verfication1.place(x=170,y=320)
  r1=PhotoImage(file="resendotp.png")
  resend1=Button(otp_phon,image=r1,command=resendotp,border=0)
  resend1.place(x=240,y=320)
  otp_phon.mainloop()
otp_option=Tk()
otp_option.geometry("400x400")
otp_option.resizable(False, False)
otp_option.title("w1")
design=Canvas(otp_option,bg="white",width=300,height=270)
design.place(x=50,y=80)
tt=Label(otp_option,text="Login Details",font="bold,40")
tt.place(x=140,y=40)
title=Label(otp_option,text="User Id",font="bold,100",bg="white")
title.place(x=160,y=100)
userid=Entry(otp_option,font=("Calibri",15,"bold"),width=25,bd=4)
userid.place(x=72,y=140)
em=PhotoImage(file="receivemail.png")
otp_email_button=Button(otp_option,image=em,border=0,command=send_otp_email)
otp_email_button.place(x=109,y=200)
ph=PhotoImage(file="receivephone.png")
otp_phone_button=Button(otp_option,image=ph,command=send_otp_phonenumber,border=0)
otp_phone_button.place(x=85,y=260)
otp_option.mainloop()