from PyQt5.QtWidgets import (QWidget, QTableWidgetItem, QDialog, QApplication, QMessageBox, QHBoxLayout, QPushButton,QFileDialog)
from PyQt5.QtCore import Qt, QDate
from PyQt5.uic import loadUi
from mysql.connector import Error
import mysql.connector
from datetime import datetime
from utils.helpers import get_profile_data, get_diagnosis
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

class Care_Window(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/care/care.ui', self)
        self.setWindowTitle("سیستم مدیریت پزشکی - سلامت بیمار")
        
        self.bmi_btn.clicked.connect(self.open_bmi_manager)
        self.symptoms_btn.clicked.connect(self.open_symptoms_manager)
        self.back_btn.clicked.connect(self.back_to_dashboard)

    def open_bmi_manager(self):
        self.bmi_window = BMI_Window(self.user_id)
        self.bmi_window.show()
        self.close()
    
    def open_symptoms_manager(self):
        self.symptoms_window = Symptoms_Window(self.user_id)
        self.symptoms_window.show()
        self.close()
    
    def back_to_dashboard(self):
        from views.dashboard import Dashboard_Window
        self.dashboard = Dashboard_Window(self.user_id)
        self.dashboard.show()
        self.close()

class BMI_Window(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/care/bmi.ui', self)
        self.setWindowTitle("BMI سیستم مدیریت پزشکی - مدیریت")
        
        self.search_date.setDate(QDate.currentDate())
        self.search_btn.clicked.connect(self.search_bmies)
        self.clear_btn.clicked.connect(self.clear_search)
        self.add_btn.clicked.connect(self.open_add_bmi)
        self.chart_button.clicked.connect(self.generate_bmi_charts)
        self.back_btn.clicked.connect(self.back_to_care)
        self.load_bmies()

    def load_bmies(self, search_date=None):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            if search_date:
                cursor.callproc('select_bmi_date', [self.user_id, search_date])
            else:
                cursor.callproc('select_user_bmies', [self.user_id])
            
            records = []
            for result in cursor.stored_results():
                records = result.fetchall()
            
            self.bmi_table.setRowCount(len(records))
            for row_idx, record in enumerate(records):
                self.bmi_table.setItem(row_idx, 0, QTableWidgetItem(str(record[0])))
                self.bmi_table.setItem(row_idx, 1, QTableWidgetItem(record[2]))
                self.bmi_table.setItem(row_idx, 2, QTableWidgetItem(str(record[5])))
                
                btn_layout = QHBoxLayout()
                edit_btn = QPushButton("ویرایش")
                delete_btn = QPushButton("حذف")
                edit_btn.setStyleSheet("QPushButton { border: 1px solid #7F908F; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
                delete_btn.setStyleSheet("QPushButton { background-color: #EEB9A8; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
                edit_btn.clicked.connect(lambda _, bid=record[0]: self.open_edit_bmi(bid))
                delete_btn.clicked.connect(lambda _, bid=record[0]: self.delete_bmi(bid))
                
                btn_widget = QWidget()
                btn_widget.setLayout(btn_layout)
                btn_layout.addWidget(edit_btn)
                btn_layout.addWidget(delete_btn)
                self.bmi_table.setCellWidget(row_idx, 3, btn_widget)
                
        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def search_bmies(self):
        search_date = self.search_date.date().toString("yyyy-MM-dd")
        self.load_bmies(search_date)

    def clear_search(self):
        self.search_date.setDate(QDate.currentDate())
        self.load_bmies()
        
    def open_add_bmi(self):
        dialog = BMI_Form(self.user_id)
        if dialog.exec_():
            self.load_bmies()
    
    def generate_bmi_charts(self):
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        try:
            # کال کردن پروسیجر با user_id
            cursor.callproc('select_bmi_info', [self.user_id])
            
            # گرفتن نتایج
            results = []
            for result in cursor.stored_results():
                results = result.fetchall()
            
            if not results:
                QMessageBox.information(self, "پیام", "هیچ داده BMI برای خروجی وجود نداره!")
                return

            # تبدیل به DataFrame
            df = pd.DataFrame(results, columns=["bid", "date_time", "height", "weight", "bmi"])
            df['date_time'] = pd.to_datetime(df['date_time'])  # تبدیل تاریخ به datetime

            # کشیدن نمودارها
            fig, axs = plt.subplots(3, 1, figsize=(10, 15))  # سه subplot عمودی

            # نمودار قد
            axs[0].plot(df['date_time'], df['height'], marker='o', color='blue')
            axs[0].set_title('تغییرات قد در طول زمان')
            axs[0].set_xlabel('تاریخ')
            axs[0].set_ylabel('قد (cm)')
            axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            axs[0].tick_params(axis='x', rotation=45)

            # نمودار وزن
            axs[1].plot(df['date_time'], df['weight'], marker='o', color='green')
            axs[1].set_title('تغییرات وزن در طول زمان')
            axs[1].set_xlabel('تاریخ')
            axs[1].set_ylabel('وزن (kg)')
            axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            axs[1].tick_params(axis='x', rotation=45)

            # نمودار BMI
            axs[2].plot(df['date_time'], df['bmi'], marker='o', color='red')
            axs[2].set_title('تغییرات BMI در طول زمان')
            axs[2].set_xlabel('تاریخ')
            axs[2].set_ylabel('BMI')
            axs[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            axs[2].tick_params(axis='x', rotation=45)

            plt.tight_layout()  # مرتب کردن فضاها

            # انتخاب مسیر فایل
            file_path, _ = QFileDialog.getSaveFileName(self, "ذخیره نمودارها", "", "PNG Files (*.png);;PDF Files (*.pdf);;JPG Files (*.jpg)")
            if not file_path:
                return

            # ذخیره فایل
            plt.savefig(file_path)
            plt.close()  # بستن figure

            QMessageBox.information(self, "موفقیت","نمودارها با موفقیت ذخیره شدند!")

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "خطا", f"مشکل در دیتابیس: {err} ")
        except Exception as e:
            QMessageBox.warning(self, "خطا", f"یه مشکل پیش اومد: {e} ")
        finally:
            cursor.close()

    def open_edit_bmi(self, bid):
        dialog = BMI_Form(self.user_id, bid)
        if dialog.exec_():
            self.load_bmies()

    def delete_bmi(self, bid):
        reply = QMessageBox.question(self, "تأیید حذف", "آیا مطمئن هستید که می‌خواهید این رکورد BMI را حذف کنید؟",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()
                
                cursor.callproc('delete_bmi', [bid])
                
                conn.commit()
                QMessageBox.information(self, "موفق", "رکورد BMI با موفقیت حذف شد!")
                self.load_bmies()
                
            except Error as e:
                if e.errno == 1644:
                    QMessageBox.warning(self, "خطا", str(e))
                else:
                    QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def back_to_care(self):
        self.health_window = Care_Window(self.user_id)
        self.health_window.show()
        self.close()

class BMI_Form(QDialog):
    def __init__(self, user_id, bid=None):
        super().__init__()
        self.user_id = user_id
        self.bid = bid
        loadUi('models/ui/care/bmi_form.ui', self)
        self.setWindowTitle("جدید BMI ثبت" if bid is None else "BMI ویرایش")
        
        self.title_label.setText("ثبت BMI جدید" if self.bid is None else "ویرایش BMI")
        self.calculate_btn.clicked.connect(self.calculate_save_bmi)
        self.cancel_btn.clicked.connect(self.reject)
        if bid:
            self.load_bmi_data()

    def load_bmi_data(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            cursor.callproc('select_bmi', [self.bid])
            
            bmi_data = None
            for result in cursor.stored_results():
                bmi_data = result.fetchone()
            
            if bmi_data:
                self.height_input.setText(str(bmi_data[3]))
                self.weight_input.setText(str(bmi_data[4]))
            else:
                QMessageBox.warning(self, "خطا", "رکورد BMI یافت نشد!")
                self.reject()

        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            self.reject()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def calculate_save_bmi(self):
        try:
            height = float(self.height_input.text().strip())
            weight = float(self.weight_input.text().strip())
            
            if height <= 0 or weight <= 0:
                QMessageBox.warning(self, "خطا", "قد و وزن باید اعداد مثبت باشند")
                return
            
            bmi = weight / ((height / 100) ** 2)
            bmi = round(bmi, 1)
            
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            if self.bid is None:
                cursor.callproc('insert_bmi', [
                    self.user_id, current_time, height, weight, bmi
                ])
            else:
                cursor.callproc('update_bmi', [
                    self.bid, height, weight, bmi
                ])
                
            conn.commit()
            
            self.show_result(bmi, current_time)
            
        except ValueError:
            QMessageBox.warning(self, "خطا", "لطفاً مقادیر عددی معتبر وارد کنید")
        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def show_result(self, bmi, date_time):
        self.result_dialog = QDialog(self)
        loadUi('models/ui/care/bmi_result.ui', self.result_dialog)
        self.result_dialog.setWindowTitle("BMI نتیجه محاسبه")
        
        self.result_dialog.result_label.setText(f"BMI شما: {bmi}")
        self.result_dialog.date_label.setText(f"تاریخ: {date_time}")
        
        if bmi < 18.5:
            status = "کم‌وزن"
            color = "orange"
        elif 18.5 <= bmi < 25:
            status = "وزن طبیعی"
            color = "green"
        elif 25 <= bmi < 30:
            status = "اضافه وزن"
            color = "orange"
        else:
            status = "چاقی"
            color = "red"
        
        self.result_dialog.status_label.setText(f"وضعیت: {status}")
        self.result_dialog.status_label.setStyleSheet(f"color: {color};")
        
        self.result_dialog.back_btn.clicked.connect(self.back_to_bmi_window)
        self.result_dialog.exec_()

    def back_to_bmi_window(self):
        self.result_dialog.accept()
        self.accept()

class Symptoms_Window(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        loadUi('models/ui/care/symptoms.ui', self)
        self.setWindowTitle("سیستم مدیریت پزشکی - ثبت علائم بیمار")

        self.search_date.setDate(QDate.currentDate())
        self.search_btn.clicked.connect(self.search_symptoms)
        self.clear_btn.clicked.connect(self.clear_search)
        self.add_btn.clicked.connect(self.open_add_symptoms)
        self.export_button.clicked.connect(self.export_symptoms_to_excel)
        self.back_btn.clicked.connect(self.back_to_care)
        self.load_symptoms()

    def load_symptoms(self, search_date=None):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            if search_date:
                cursor.callproc('select_symptoms_date', [self.user_id, search_date])
            else:
                cursor.callproc('select_user_symptoms', [self.user_id])
            
            records = []
            for result in cursor.stored_results():
                records = result.fetchall()
            
            self.symptoms_table.setRowCount(len(records))
            for row_idx, record in enumerate(records):
                self.symptoms_table.setItem(row_idx, 0, QTableWidgetItem(str(record[0])))
                self.symptoms_table.setItem(row_idx, 1, QTableWidgetItem(record[2]))
                
                btn_layout = QHBoxLayout()
                edit_btn = QPushButton("ویرایش")
                delete_btn = QPushButton("حذف")
                edit_btn.setStyleSheet("QPushButton { border: 1px solid #7F908F; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #7F908F; }")
                delete_btn.setStyleSheet("QPushButton { background-color: #EEB9A8; padding: 5px; border-radius: 5px;} QPushButton:hover { background-color: #DF817A; }")
                edit_btn.clicked.connect(lambda _, sid=record[0]: self.open_edit_symptoms(sid))
                delete_btn.clicked.connect(lambda _, sid=record[0]: self.delete_symptoms(sid))
                
                btn_widget = QWidget()
                btn_widget.setLayout(btn_layout)
                btn_layout.addWidget(edit_btn)
                btn_layout.addWidget(delete_btn)
                self.symptoms_table.setCellWidget(row_idx, 2, btn_widget)
                
        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def search_symptoms(self):
        search_date = self.search_date.date().toString("yyyy-MM-dd")
        self.load_symptoms(search_date)

    def clear_search(self):
        self.search_date.setDate(QDate.currentDate())
        self.load_symptoms()
        
    def open_add_symptoms(self):
        dialog = Symptoms_Form(self.user_id)
        if dialog.exec_():
            self.load_symptoms()
    
    def export_symptoms_to_excel(self):
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        try:
            # کال کردن پروسیجر
            cursor.callproc('select_symptoms_info')
            
            # گرفتن نتایج
            results = []
            for result in cursor.stored_results():
                results = result.fetchall()
            
            if not results:
                QMessageBox.information(self, "پیام", "هیچ علائمی برای خروجی وجود نداره!")
                return

            # تبدیل به DataFrame با pandas
            df = pd.DataFrame(results, columns=["شناسه", "تاریخ", "وضعیت", "علائم"])

            # انتخاب مسیر فایل
            file_path, _ = QFileDialog.getSaveFileName(self, "ذخیره فایل Excel", "", "Excel Files (*.xlsx)")
            if not file_path:
                return  # اگر کاربر کنسل کرد

            # ذخیره در Excel
            df.to_excel(file_path, index=False, engine='openpyxl')
            QMessageBox.information(self, "موفقیت", "فایل Excel با موفقیت ذخیره شد!")

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "خطا", f"مشکل در دیتابیس: {err} ")
        except Exception as e:
            QMessageBox.warning(self, "خطا", f"یه مشکل پیش اومد: {e} ")
        finally:
            cursor.close()

    def open_edit_symptoms(self, sid):
        dialog = Symptoms_Form(self.user_id, sid)
        if dialog.exec_():
            self.load_symptoms()

    def delete_symptoms(self, sid):
        reply = QMessageBox.question(self, "تأیید حذف", "آیا مطمئن هستید که می‌خواهید این رکورد علائم را حذف کنید؟",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()
                
                cursor.callproc('delete_symptom', [sid])
                
                conn.commit()
                QMessageBox.information(self, "موفق", "رکورد علائم با موفقیت حذف شد!")
                self.load_symptoms()
                
            except Error as e:
                if e.errno == 1644:
                    QMessageBox.warning(self, "خطا", str(e))
                else:
                    QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()

    def back_to_care(self):
        self.health_window = Care_Window(self.user_id)
        self.health_window.show()
        self.close()

class Symptoms_Form(QDialog):
    def __init__(self, user_id, sid=None):
        super().__init__()
        self.user_id = user_id
        self.sid = sid
        loadUi('models/ui/care/symptoms_form.ui', self)
        self.setWindowTitle("ثبت علائم جدید" if sid is None else "ویرایش علائم")
        self.title_label.setText("ثبت علائم جدید" if self.sid is None else "ویرایش علائم")
        self.save_only_btn.clicked.connect(self.save_symptoms)  # دکمه جدید فقط ذخیره
        self.save_btn.clicked.connect(self.save_and_analyze_symptoms)
        self.cancel_btn.clicked.connect(self.reject)
        if sid:
            self.load_symptoms_data()

    def load_symptoms_data(self):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            cursor.callproc('select_symptom', [self.sid])
            
            symptoms_data = None
            for result in cursor.stored_results():
                symptoms_data = result.fetchone()
            
            if symptoms_data:
                self.status_input.setPlainText(symptoms_data[3] or "")
                self.symptoms_input.setPlainText(symptoms_data[4] or "")
            else:
                QMessageBox.warning(self, "خطا", "رکورد علائم یافت نشد!")
                self.reject()

        except Error as e:
            QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
            self.reject()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def save_symptoms(self):
        status = self.status_input.toPlainText().strip()
        symptoms = self.symptoms_input.toPlainText().strip()
        
        if not symptoms:
            QMessageBox.warning(self, "خطا", "لطفاً علائم را وارد کنید!")
            return False
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            if self.sid is None:
                cursor.callproc('insert_symptom', [
                    self.user_id, current_time, status, symptoms
                ])
            else:
                cursor.callproc('update_symptom', [
                    self.sid, status, symptoms
                ])
            
            conn.commit()
            QMessageBox.information(self, "موفقیت", "علائم با موفقیت ذخیره شد!")
            self.accept()

            return True
            
        except Error as e:
            if e.errno == 1644:
                QMessageBox.warning(self, "خطا", str(e))
            else:
                QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)} ")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def save_and_analyze_symptoms(self):
        status = self.status_input.toPlainText().strip()
        symptoms = self.symptoms_input.toPlainText().strip()
        
        if not symptoms:
            QMessageBox.warning(self, "خطا", "لطفاً علائم را وارد کنید")
            return
        
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            if self.sid is None:
                cursor.callproc('insert_symptom', [
                    self.user_id, current_time, status, symptoms
                ])
            else:
                cursor.callproc('update_symptom', [
                    self.sid, status, symptoms
                ])
            
            conn.commit()
            
            profile = get_profile_data(self.user_id)
            if not profile:
                QMessageBox.warning(self, "خطا", "پروفایل بیمار یافت نشد!")
                return
            
            symptom_data = {'status': status, 'symptoms': symptoms}
            result = get_diagnosis(profile, symptom_data)
            diagnosis = result['diagnosis']
            prompt = result['prompt']
            
            self.show_result(diagnosis, current_time, prompt)
            
        except Error as e:
            if e.errno == 1644:
                QMessageBox.warning(self, "خطا", str(e))
            else:
                QMessageBox.critical(self, "خطای دیتابیس", f"خطا: {str(e)}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def show_result(self, diagnosis, date_time, prompt):
        self.result_dialog = QDialog(self)
        loadUi('models/ui/care/symptoms_result.ui', self.result_dialog)
        self.result_dialog.setWindowTitle("نتیجه تحلیل علائم")
        
        self.result_dialog.prompt_text.setPlainText(prompt)
        self.result_dialog.diagnosis_text.setPlainText(diagnosis or "بدون پاسخ از مدل")
        self.result_dialog.date_label.setText(f"تاریخ : {date_time}")
        
            # ذخیره پرامپت و تشخیص تو فایل داخل فولدر utils
        try:
            import os
            log_path = os.path.join('database', 'diagnosis_log.txt')  # مسیر به utils/diagnosis_log.txt
            os.makedirs('database', exist_ok=True)  # اگه فولدر utils نباشه، می‌سازه
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f"Date: {date_time}\nPrompt: {prompt}\nDiagnosis: {diagnosis}\n{'-'*50}\n")
        except Exception as e:
            print(f"خطا در ذخیره فایل: {str(e)}")

        self.result_dialog.back_btn.clicked.connect(self.back_to_symptoms_window)
        self.result_dialog.exec_()

    def back_to_symptoms_window(self):
        self.result_dialog.accept()
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Care_Window(1)
    window.show()
    sys.exit(app.exec_())
