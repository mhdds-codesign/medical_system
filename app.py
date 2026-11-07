import sys
from PyQt5.QtWidgets import QApplication
from views.login import login_window

def main():
    
    # ایجاد برنامه
    app = QApplication(sys.argv)
    
    # نمایش صفحه ورود
    window = login_window()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()