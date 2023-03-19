import random
import smtplib
import tkinter as tk

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)

# Sender email credentials
sender_email = "sender_email@gmail.com"
sender_password = "sender_password"

# Send email with OTP to user
def send_otp_email(email):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Your OTP is {otp}. Please enter this code to verify your identity."
        server.sendmail(sender_email, email, message)
        print("OTP sent successfully.")
    except:
        print("Error sending OTP email.")
    finally:
        server.quit()

# Verify OTP and display result in GUI
def verify_otp():
    user_otp = otp_entry.get()
    if user_otp.isdigit() and len(user_otp) == 6:
        if int(user_otp) == otp:
            result_label.config(text="OTP verification successful.")
        else:
            result_label.config(text="OTP verification failed. Please try again.")
    else:
        result_label.config(text="Invalid OTP. Please enter a 6-digit code.")

# Create Tkinter GUI
root = tk.Tk()
root.title("OTP Verification")

# Add email input field
email_label = tk.Label(root, text="Enter your email address:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Add button to send OTP email
otp_button = tk.Button(root, text="Send OTP", command=lambda: send_otp_email(email_entry.get()))
otp_button.pack()

# Add OTP input field
otp_label = tk.Label(root, text="Enter the OTP sent to your email:")
otp_label.pack()
otp_entry = tk.Entry(root)
otp_entry.pack()

# Add button to verify OTP
verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

# Add label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
