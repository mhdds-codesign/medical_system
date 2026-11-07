from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
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

class Account_Window(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/account/account.ui', self)
        self.setWindowTitle("سیستم مدیریت پزشکی - مدیریت پروفایل")
        
        self.personal_btn.clicked.connect(self.open_edit_profile)
        self.account_btn.clicked.connect(self.open_Edit_Userdata)
        self.delete_btn.clicked.connect(self.delete_account)
        self.back_btn.clicked.connect(self.back_to_dashboard)

    def open_edit_profile(self):
        self.personal_window = Edit_Profile(self.user_id)
        self.personal_window.show()
        self.close()

    def open_Edit_Userdata(self):
        self.account_window = Edit_Userdata(self.user_id)
        self.account_window.show()
        self.close()

    def delete_account(self):
        reply = QMessageBox.question(self, "تأیید حذف", "آیا مطمئن هستید که می‌خواهید حساب کاربری خود را حذف کنید؟",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()
                
                cursor.callproc('delete_profile', [self.user_id])
                cursor.callproc('delete_user', [self.user_id])
                conn.commit()
                QMessageBox.information(self, "موفق", "حساب کاربری شما با موفقیت حذف شد!<br>جهت استفاده از امکانات برنامه ثبت نام کنید.")
                self.back_to_login()

            except Error as e:
                if e.errno == 1644:
                    error_message = str(e)
                    if "پروفایل" in error_message:
                        QMessageBox.warning(self, "خطا", "پروفایل کاربر یافت نشد!")
                    elif "کاربر" in error_message:
                        QMessageBox.warning(self, "خطا", "کاربر یافت نشد!")
                    else:
                        QMessageBox.warning(self, "خطا", error_message)
                else:
                    QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def back_to_dashboard(self):
        from views.dashboard import Dashboard_Window
        self.dashboard = Dashboard_Window(self.user_id)
        self.dashboard.show()
        self.close()

    def back_to_login(self):
        from views.login import login_window
        self.login_window = login_window()
        self.login_window.show()
        self.close()

class Edit_Profile(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/account/edit_profile.ui', self)
        self.setWindowTitle("ویرایش اطلاعات شخصی")
        
        self.save_btn.clicked.connect(self.save_profile)
        self.back_btn.clicked.connect(self.back_to_account_window)
        self.load_profile()

    def load_profile(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            cursor.callproc('select_profile', [self.user_id])
            
            profile = None
            for result in cursor.stored_results():
                profile = result.fetchone()
            
            if profile:
                self.national_id_input.setText(profile[1])
                self.name_input.setText(profile[2])
                self.gender_input.setCurrentText(profile[3])
                self.age_input.setText(str(profile[4]))
                self.tel_input.setText(profile[5])
            else:
                QMessageBox.warning(self, "خطا", "اطلاعات شخصی یافت نشد!")

        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def validate_profile(self):
        national_id = self.national_id_input.text().strip()
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()
        tel = self.tel_input.text().strip()

        if not all([national_id,name, age, tel]):
            return False, "لطفاً تمام فیلدها را پر کنید"

        if not re.match(r'^\d{10}$', national_id):
            return False, "کد ملی باید 10 رقم باشد"
        
        try:
            age = int(age)
            if age <= 0 or age > 120:
                return False, "سن باید بین 1 تا 120 باشد"
        except ValueError:
            return False, "سن باید یک عدد معتبر باشد"

        if not re.match(r'^09\d{9}$', tel):
            return False, "شماره تلفن باید 11 رقم باشد و با 09 شروع شود"

        return True, ""

    def save_profile(self):
        is_valid, error_message = self.validate_profile()
        if not is_valid:
            QMessageBox.warning(self, "خطا", error_message)
            return

        national_id = self.national_id_input.text().strip()
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()
        tel = self.tel_input.text().strip()
        gender = self.gender_input.currentText()

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            cursor.callproc('update_profile', [
                self.user_id, national_id, name, gender, int(age), tel
            ])
            
            conn.commit()
            QMessageBox.information(self, "موفق", "تغییرات شخصی با موفقیت ذخیره شد!")
            self.back_to_account_window()

        except Error as e:
            if e.errno == 1644:
                QMessageBox.warning(self, "خطا", str(e))
            else:
                QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def back_to_account_window(self):
        self.account_window = Account_Window(self.user_id)
        self.account_window.show()
        self.close()

class Edit_Userdata(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/account/edit_userdata.ui', self)
        self.setWindowTitle("ویرایش اطلاعات کاربری")
        
        self.save_btn.clicked.connect(self.save_account)
        self.back_btn.clicked.connect(self.back_to_account_window)

    def validate_account(self):
        old_username = self.old_username_input.text().strip()
        old_password = self.old_password_input.text().strip()
        new_username = self.new_username_input.text().strip()
        new_password = self.new_password_input.text().strip()
        confirm_new_password = self.confirm_new_password_input.text().strip()

        if not all([old_username, old_password, new_username, new_password, confirm_new_password]):
            return False, "لطفاً تمام فیلدها را پر کنید"

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            cursor.callproc('select_check_user', [old_username, old_password])
            
            for result in cursor.stored_results():
                user = result.fetchone()
                if not user:
                    return False, "نام کاربری یا رمز عبور فعلی اشتباه است"

        except Error as e:
            return False, f"خطای دیتابیس: {str(e)}"
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        if new_password != confirm_new_password:
            return False, "رمز عبور جدید و تکرار آن مطابقت ندارند"

        return True, ""

    def save_account(self):
        is_valid, error_message = self.validate_account()
        if not is_valid:
            QMessageBox.warning(self, "خطا", error_message)
            return

        new_username = self.new_username_input.text().strip()
        new_password = self.new_password_input.text().strip()

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            cursor.callproc('update_user', [
                self.user_id, new_username, new_password
            ])
            
            conn.commit()
            QMessageBox.information(self, "موفق", "تغییرات کاربری با موفقیت ذخیره شد!<br>لطفاً دوباره وارد سیستم شوید.")
            self.back_to_login()

        except Error as e:
            if e.errno == 1644:
                QMessageBox.warning(self, "خطا", str(e))
            else:
                QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def back_to_account_window(self):
        self.account_window = Account_Window(self.user_id)
        self.account_window.show()
        self.close()

    def back_to_login(self):
        from views.login import login_window
        self.login_window = login_window()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Account_Window(1)
    window.show()
    sys.exit(app.exec_())
