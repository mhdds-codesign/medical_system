from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
from mysql.connector import Error
import mysql.connector
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

class Dashboard_Window(QWidget):
    def __init__(self, user_id, reminder=None):
        super().__init__()
        self.user_id = user_id
        self.reminder = reminder
        loadUi('views/ui/dashboard.ui', self)  # لود فایل UI
        self.setWindowTitle("سیستم مدیریت پزشکی - داشبورد")
        
        # به‌روزرسانی متن خوش‌آمدگویی
        username = self.get_username()
        self.welcome_label.setText(f"خوش آمدید، {username}!")
        
        # اتصال دکمه‌ها
        self.profile_btn.clicked.connect(self.manage_profile)
        self.symptoms_btn.clicked.connect(self.manage_symptoms)
        self.medicines_btn.clicked.connect(self.manage_medicines)
        self.logout_btn.clicked.connect(self.logout)

    def get_username(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            cursor.callproc('select_user', [self.user_id])
            
            username = "کاربر"
            for result in cursor.stored_results():
                user_data = result.fetchone()
                if user_data:
                    username = user_data[1]
            
            return username
            
        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            return "کاربر"
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def manage_profile(self):
        from models.account import Account_Window
        self.profile_window = Account_Window(self.user_id)
        self.profile_window.show()
        self.close()

    def manage_symptoms(self):
        from models.care import Care_Window
        self.symptoms_window = Care_Window(self.user_id)
        self.symptoms_window.show()
        self.close()

    def manage_medicines(self):
        from models.medicines import Medicines_Window
        self.medicines_window = Medicines_Window(self.user_id)
        self.medicines_window.show()
        self.close()

    def logout(self):
        from views.login import login_window
        if self.reminder:
            self.reminder.stop()
        self.login_window = login_window()
        self.login_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dashboard_Window(1)  # برای تست
    window.show()
    sys.exit(app.exec_())
