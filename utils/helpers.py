import mysql.connector
from mysql.connector import Error
from openai import OpenAI
from dotenv import load_dotenv
import os

# بارگذاری کلید API از فایل .env
load_dotenv()
api_key = os.getenv('DEEPSEEK_API_KEY')
if not api_key:
    raise ValueError("API Key برای DeepSeek پیدا نشد! لطفاً فایل .env رو چک کن، نازنینم! 😊")

# تنظیم کلاینت DeepSeek
client = OpenAI(
    api_key=api_key,  # کلید OpenRouter
    base_url="https://openrouter.ai/api/v1"
)

# تنظیمات دیتابیس (همون قبلی)
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'medical'
}

def get_profile_data(user_id):
    """گرفتن سن و جنسیت از جدول profiles با پروسیجر select."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # ف پروسیجر select_profile 
        cursor.callproc('select_profile', [user_id]) 
        
        profile_data = None
        for result in cursor.stored_results():
            profile_data = result.fetchone()
        
        if profile_data:
            return {'age': profile_data[4], 'gender': profile_data[3]}  # age, gender
        return None
        
    except Error as e:
        print(f"خطا در گرفتن پروفایل: {str(e)}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_diagnosis(profile, symptom_data):
    """ساخت پرامپت زیبا و فراخوانی DeepSeek برای تشخیص مختصر."""
    age = profile.get('age', 'نامشخص')
    gender = profile.get('gender', 'نامشخص')
    status = symptom_data.get('status', 'هیچ پیش‌زمینه‌ای ذکر نشده')
    symptoms = symptom_data.get('symptoms', 'هیچ علائمی ذکر نشده')
    
    # ساخت پرامپت زیبا و مختصر (انگلیسی برای DeepSeek بهتره)
    prompt = f"""You are a kind and caring and helpful medical assistant. 
    Patient: {gender} aged {age} years.
    Background/Pre-existing conditions or recent meds: {status}
    Current symptoms: {symptoms}
    
    With a warm and empathetic tone, Provide a brief analysis: What might this indicate based on history? Possible conditions? Include more than 2 real, practical recommendations (e.g., drink water, rest, monitor symptoms and more you know). Keep it concise and useful (under 200 words). Advise consulting a doctor.
    """
    
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3.1:free",
            messages=[
                {"role": "system", "content": "You are a kind, concise and empathetic medical AI. Respond in Persian with a warm, caring tone, and be accurate."},
                {"role": "user", "content": prompt}
            ],
            stream=False,
            max_tokens=300  # برای مختصر نگه داشتن
        )
        diagnosis = response.choices[0].message.content
        
        return {'diagnosis': diagnosis, 'prompt': prompt}
        
    except Exception as e:
        print(f"خطای کامل DeepSeek: {e}")
    return {'diagnosis': 'متأسفانه خطایی رخ داد. با پزشک مشورت کنید.', 'prompt': prompt}
