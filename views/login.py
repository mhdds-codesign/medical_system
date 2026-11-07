from PyQt5.QtWidgets import QWidget,QDialog, QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from mysql.connector import Error
import mysql.connector
import re
import sys

# فعال کردن پشتیبانی از High DPI
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

# تنظیمات اتصال به MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'medical'
}

class signup_window(QDialog):
    def __init__(self):
        super().__init__()
        # لود فایل UI
        loadUi('views/ui/signup.ui', self)  # مسیر درست فایل
        self.setWindowTitle("ثبت‌نام در سیستم")
        
        # اتصال دکمه‌ها
        self.submit_btn.clicked.connect(self.save_data)
        self.cancel_btn.clicked.connect(self.reject)

    def validate_data(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        confirm_password = self.confirm_password_input.text().strip()
        national_id = self.national_id_input.text().strip()
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()
        tel = self.tel_input.text().strip()

        # اعتبارسنجی فیلدهای خالی
        if not all([username, password, confirm_password, national_id, name, age, tel]):
            return False, "لطفاً تمام فیلدها را پر کنید"

        # اعتبارسنجی رمز عبور
        if password != confirm_password:
            return False, "رمز عبور و تکرار آن مطابقت ندارند"

        # اعتبارسنجی کد ملی (10 رقم)
        if not re.match(r'^\d{10}$', national_id):
            return False, "کد ملی باید 10 رقم باشد"

        # اعتبارسنجی سن
        try:
            age = int(age)
            if age <= 0 or age > 120:
                return False, "سن باید بین 1 تا 120 باشد"
        except ValueError:
            return False, "سن باید یک عدد معتبر باشد"

        # اعتبارسنجی تلفن (11 رقم و شروع با 09)
        if not re.match(r'^09\d{9}$', tel):
            return False, "شماره تلفن باید 11 رقم باشد و با 09 شروع شود"


        return True, ""

    def save_data(self):
        is_valid, error_message = self.validate_data()
        if not is_valid:
            QMessageBox.warning(self, "خطا", error_message)
            return

        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        national_id = self.national_id_input.text().strip()
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()
        tel = self.tel_input.text().strip()
        gender = self.gender_input.currentText()

        try:
            # اتصال به MySQL
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            # استفاده از stored procedure برای ثبت کاربر
            cursor.callproc('insert_user', [username, password])
            
            # گرفتن user_id از نتیجه
            user_id = None
            for result in cursor.stored_results():
                user_id = result.fetchone()[0]
            
            if user_id:
                # استفاده از stored procedure برای ثبت پروفایل
                cursor.callproc('insert_profile', [
                    user_id, national_id, name, gender, int(age), tel
                ])
                
                conn.commit()
                QMessageBox.information(self, "موفق", "ثبت‌نام با موفقیت انجام شد!<br>لطفاً با نام کاربری و رمز عبور خود وارد سیستم شوید.")
                self.accept()
            else:
                QMessageBox.warning(self, "خطا", "خطا در ثبت کاربر")

        except mysql.connector.Error as e:
            if e.errno == 1644:  # خطای custom از stored procedure
                QMessageBox.warning(self, "خطا", str(e))
            else:
                QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

class login_window(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('views/ui/login.ui', self)  # مسیر فایل login.ui
        self.setWindowTitle("سیستم مدیریت پزشکی - ورود")
        
        self.login_btn.clicked.connect(self.login)
        self.signup_btn.clicked.connect(self.show_signup_window)
    
    def show_signup_window(self):
        dialog = signup_window()
        if dialog.exec_():
            self.username_input.clear()
            self.password_input.clear()
    
    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, "خطا", "لطفاً تمام فیلدها را پر کنید")
            return
        
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            cursor.callproc('select_check_user', [username, password])
            
            user_id = None
            for result in cursor.stored_results():
                user = result.fetchone()
                if user:
                    user_id = user[0]
                    QMessageBox.information(self, "موفق", "ورود موفقیت‌آمیز بود!")
                    self.open_dashboard(user_id)
                else:
                    QMessageBox.warning(self, "خطا", "نام کاربری یا رمز عبور اشتباه است<br>چنانچه حسابی ندارید، ثبت‌نام کنید")
        
        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    
    def open_dashboard(self, user_id):
        from views.dashboard import Dashboard_Window
        from utils.reminder import Medicines_Reminder
        self.reminder = Medicines_Reminder(user_id)
        self.dashboard = Dashboard_Window(user_id, self.reminder)
        self.dashboard.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = login_window()  # ایجاد نمونه از کلاس
    window.show()
    sys.exit(app.exec_)
