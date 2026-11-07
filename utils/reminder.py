from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

# تنظیمات اتصال به MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',  # پسورد MySQL خودت رو اینجا بذار
    'database': 'medical'
}

class Medicines_Reminder:
    def __init__(self, user_id):
        self.user_id = user_id
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_medicines)
        self.timer.start(60000)  # چک هر 60 ثانیه

    def check_medicines(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            # استفاده از stored procedure برای گرفتن داروها
            cursor.callproc('select_user_medicines', [self.user_id])
            
            meds = []
            for result in cursor.stored_results():
                meds = result.fetchall()
            
            now = datetime.now()

            for med in meds:
                mid, muser_id, medicine, dosage, duration, last_taken, next_dose_str = med
                try:
                    next_dose = datetime.strptime(next_dose_str, '%Y-%m-%d %H:%M')
                    if now >= next_dose:
                        self.show_notification(medicine, dosage)
                        new_last_taken = now.strftime('%Y-%m-%d %H:%M')
                        new_next_dose = (now + timedelta(hours=duration)).strftime('%Y-%m-%d %H:%M')
                        
                        # استفاده از stored procedure برای آپدیت زمان دارو
                        cursor.callproc('update_medicine', [
                            mid, medicine, dosage, duration, new_last_taken, new_next_dose
                        ])
                        
                except ValueError:
                    continue 

            conn.commit()

        except Error as e:
            QMessageBox.critical(None, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def show_notification(self, medicine, dosage):
        msg = QMessageBox()
        msg.setWindowTitle("⏰ یادآوری مصرف دارو")
        msg.setText(f'''
        <p style="font-size: 16px; text-align: center;">
        <b>زمان مصرف دارو فرا رسیده است:</b><br><br>
        دارو: {medicine}<br>
        دوز: {dosage}<br>
        </p>
        ''')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setStyleSheet("QMessageBox { background-color: #f0f8ff; } QLabel { color: #333; } QPushButton { background-color: #4CAF50; color: white; padding: 10px; }")
        msg.exec_()

    def stop(self):
        self.timer.stop()
