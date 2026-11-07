from PyQt5.QtWidgets import (QWidget, QTableWidgetItem, QDialog, QApplication, QMessageBox, QHBoxLayout, QPushButton)
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.uic import loadUi
from mysql.connector import Error
import mysql.connector
from datetime import datetime, timedelta
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

class Medicines_Window(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/medicines/medicines.ui', self)
        self.setWindowTitle("سیستم مدیریت پزشکی - مدیریت داروها")
        
        self.search_btn.clicked.connect(self.search_medicines)
        self.clear_btn.clicked.connect(self.clear_search)
        self.search_input.returnPressed.connect(self.search_medicines)
        self.add_btn.clicked.connect(self.open_add_medicine)
        self.back_btn.clicked.connect(self.back_to_dashboard)
        self.load_medicines()

    def load_medicines(self, name_searched=None):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            if name_searched:
                cursor.callproc('select_medicine_name', [self.user_id, name_searched])
            else:
                cursor.callproc('select_user_medicines', [self.user_id])
            
            medicines = []
            for result in cursor.stored_results():
                medicines = result.fetchall()
            
            self.medicine_table.setRowCount(len(medicines))
            for row_idx, medicine in enumerate(medicines):
                self.medicine_table.setItem(row_idx, 0, QTableWidgetItem(str(medicine[0])))
                self.medicine_table.setItem(row_idx, 1, QTableWidgetItem(medicine[2]))
                
                btn_layout = QHBoxLayout()
                edit_btn = QPushButton("ویرایش")
                delete_btn = QPushButton("حذف")
                edit_btn.setStyleSheet("QPushButton { border: 1px solid #7F908F; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
                delete_btn.setStyleSheet("QPushButton { background-color: #EEB9A8; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
                edit_btn.clicked.connect(lambda _, mid=medicine[0]: self.open_edit_medicine(mid))
                delete_btn.clicked.connect(lambda _, mid=medicine[0]: self.delete_medicine(mid))
                
                btn_widget = QWidget()
                btn_widget.setLayout(btn_layout)
                btn_layout.addWidget(edit_btn)
                btn_layout.addWidget(delete_btn)
                self.medicine_table.setCellWidget(row_idx, 2, btn_widget)

        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def search_medicines(self):
        name_searched = self.search_input.text().strip()
        if name_searched:
            self.load_medicines(name_searched)
        else:
            self.load_medicines()

    def clear_search(self):
        self.search_input.clear()
        self.load_medicines()

    def open_add_medicine(self):
        dialog = Medicine_Form(self.user_id)
        if dialog.exec_():
            self.load_medicines()

    def open_edit_medicine(self, mid):
        dialog = Medicine_Form(self.user_id, mid)
        if dialog.exec_():
            self.load_medicines()

    def delete_medicine(self, mid):
        reply = QMessageBox.question(self, "تأیید حذف", "آیا مطمئن هستید که می‌خواهید این دارو را حذف کنید؟",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()
                
                cursor.callproc('delete_medicine', [mid])
                
                conn.commit()
                QMessageBox.information(self, "موفق", "دارو با موفقیت حذف شد!")
                self.load_medicines()
                
            except Error as e:
                if e.errno == 1644:
                    QMessageBox.warning(self, "خطا", str(e))
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

class Medicine_Form(QDialog):
    def __init__(self, user_id, mid=None):
        super().__init__()
        self.user_id = user_id
        self.mid = mid
        loadUi('models/ui/medicines/medicine_form.ui', self)
        self.setWindowTitle("ثبت داروی جدید" if mid is None else "ویرایش دارو")
                
         #تنظیم عنوان داینامیک
        self.title_label.setText("ثبت داروی جدید" if self.mid is None else "ویرایش دارو")
        
        # تنظیم تاریخ‌های پیش‌فرض
        if self.mid is None:
            self.last_taken_input.setDateTime(QDateTime.currentDateTime())
            self.next_dose_input.setDateTime(QDateTime.currentDateTime())

        self.save_btn.clicked.connect(self.save_medicine)
        self.cancel_btn.clicked.connect(self.reject)
        self.duration_input.textChanged.connect(self.set_next_dose)
        self.last_taken_input.dateTimeChanged.connect(self.set_next_dose)
        if mid:
            self.load_medicine()

    def set_next_dose(self):
        try:
            duration = self.duration_input.text().strip()
            last_taken = self.last_taken_input.dateTime().toString('yyyy-MM-dd HH:mm')
            if duration and last_taken:
                duration = int(duration)
                if duration <= 0:
                    return
                last_taken_cul = datetime.strptime(last_taken, '%Y-%m-%d %H:%M')
                next_dose_cul = last_taken_cul + timedelta(hours=duration)
                self.next_dose_input.setDateTime(QDateTime.fromString(next_dose_cul.strftime('%Y-%m-%d %H:%M'), 'yyyy-MM-dd HH:mm'))
        except (ValueError, TypeError):
            self.next_dose_input.setDateTime(QDateTime.currentDateTime())

    def load_medicine(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            cursor.callproc('select_medicine', [self.mid])
            
            medicine = None
            for result in cursor.stored_results():
                medicine = result.fetchone()
            
            if medicine:
                self.medicine_input.setText(medicine[2])
                self.dosage_input.setText(medicine[3])
                self.duration_input.setText(str(medicine[4]))
                
                last_taken_str = medicine[5]
                next_dose_str = medicine[6]
                
                last_taken_dt = datetime.strptime(last_taken_str, '%Y-%m-%d %H:%M')
                next_dose_dt = datetime.strptime(next_dose_str, '%Y-%m-%d %H:%M')
                
                self.last_taken_input.setDateTime(QDateTime.fromString(last_taken_dt.strftime('%Y-%m-%d %H:%M'), 'yyyy-MM-dd HH:mm'))
                self.next_dose_input.setDateTime(QDateTime.fromString(next_dose_dt.strftime('%Y-%m-%d %H:%M'), 'yyyy-MM-dd HH:mm'))
            else:
                QMessageBox.warning(self, "خطا", "دارو یافت نشد!")
                self.reject()

        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            self.reject()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def validate_inputs(self):
        medicine = self.medicine_input.text().strip()
        dosage = self.dosage_input.text().strip()
        duration = self.duration_input.text().strip()
        last_taken = self.last_taken_input.dateTime().toString('yyyy-MM-dd HH:mm')
        next_dose = self.next_dose_input.dateTime().toString('yyyy-MM-dd HH:mm')

        if not all([medicine, dosage, duration, last_taken, next_dose]):
            return False, "لطفاً فیلدهای ضروری را پر کنید (نام، دوز، مدت، آخرین دوز، دوز بعدی)"

        try:
            duration = int(duration)
            if duration <= 0:
                return False, "مدت مصرف باید یک عدد مثبت باشد"
        except ValueError:
            return False, "مدت مصرف باید یک عدد معتبر باشد"

        try:
            last_taken_dt = datetime.strptime(last_taken, '%Y-%m-%d %H:%M')
            current_time = datetime.now()
            if last_taken_dt > current_time:
                return False, "زمان آخرین دوز نمی‌تواند در آینده باشد."
        except ValueError:
            return False, "زمان آخرین دوز نامعتبر است"

        try:
            last_taken_dt = datetime.strptime(last_taken, '%Y-%m-%d %H:%M')
            next_dose_dt = datetime.strptime(next_dose, '%Y-%m-%d %H:%M')
            if next_dose_dt <= last_taken_dt:
                return False, "زمان دوز بعدی باید حتماً بعد از آخرین دوز باشد."
        except ValueError:
            return False, "زمان دوز بعدی نامعتبر است"

        return True, ""

    def save_medicine(self):
        is_valid, error_message = self.validate_inputs()
        if not is_valid:
            QMessageBox.warning(self, "خطا", error_message)
            return

        medicine = self.medicine_input.text().strip()
        dosage = self.dosage_input.text().strip()
        duration = int(self.duration_input.text().strip())
        last_taken = self.last_taken_input.dateTime().toString('yyyy-MM-dd HH:mm')
        next_dose = self.next_dose_input.dateTime().toString('yyyy-MM-dd HH:mm')

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            if self.mid is None:
                cursor.callproc('insert_medicine', [
                    self.user_id, medicine, dosage, duration, last_taken, next_dose
                ])
            else:
                cursor.callproc('update_medicine', [
                    self.mid, medicine, dosage, duration, last_taken, next_dose
                ])
            
            conn.commit()
            QMessageBox.information(self, "موفق", f"دارو با موفقیت {'اضافه' if self.mid is None else 'ویرایش'} شد!")
            self.accept()

        except Error as e:
            if e.errno == 1644:
                QMessageBox.warning(self, "خطا", str(e))
            else:
                QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Medicines_Window(1)
    window.show()
    sys.exit(app.exec_())
