-- =============================================
-- فایل کامل ایجاد تمام Stored Procedures
-- =============================================

DELIMITER //

-- ==================== USERS TABLE ====================
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_user`(
    IN p_username VARCHAR(50),
    IN p_password VARCHAR(8)
)
BEGIN
    IF EXISTS (SELECT 1 FROM users WHERE username = p_username) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'نام کاربری تکراری است';
    ELSE
        INSERT INTO users (username, password) 
        VALUES (p_username, p_password);
        SELECT LAST_INSERT_ID() as new_user_id;
    END IF;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_user`(IN p_id INT)
BEGIN
    SELECT * FROM users WHERE id = p_id;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_user`(
    IN p_id INT,
    IN p_username VARCHAR(50),
    IN p_password VARCHAR(8)
)
BEGIN
    IF EXISTS (SELECT 1 FROM users WHERE id = p_id) THEN
        UPDATE users 
        SET username = p_username, password = p_password 
        WHERE id = p_id;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه کاربر وجود ندارد';
    END IF;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_user`(IN p_id INT)
BEGIN
    IF EXISTS (SELECT 1 FROM users WHERE id = p_id) THEN
        DELETE FROM users WHERE id = p_id;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه کاربر وجود ندارد';
    END IF;
END //

-- ==================== PROFILES TABLE ====================
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_profile`(
    IN p_user_id INT,
    IN p_national_id VARCHAR(15),
    IN p_name VARCHAR(50),
    IN p_gender ENUM('male', 'female'),
    IN p_age INT,
    IN p_tel VARCHAR(11)
)
BEGIN
    IF EXISTS (SELECT 1 FROM profiles WHERE user_id = p_user_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'پروفایل برای این کاربر قبلاً ایجاد شده است';
    ELSE
        INSERT INTO profiles (user_id, national_id, name, gender, age, tel) 
        VALUES (p_user_id, p_national_id, p_name, p_gender, p_age, p_tel);
    END IF;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_profile`(IN p_user_id INT)
BEGIN
    SELECT * FROM profiles WHERE user_id = p_user_id;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_profile`(
    IN p_user_id INT,
    IN p_national_id VARCHAR(15),
    IN p_name VARCHAR(50),
    IN p_gender ENUM('male', 'female'),
    IN p_age INT,
    IN p_tel VARCHAR(11)
)
BEGIN
    IF EXISTS (SELECT 1 FROM profiles WHERE user_id = p_user_id) THEN
        UPDATE profiles 
        SET national_id = p_national_id, 
            name = p_name, 
            gender = p_gender, 
            age = p_age, 
            tel = p_tel 
        WHERE user_id = p_user_id;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'پروفایل برای این کاربر وجود ندارد';
    END IF;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_profile`(IN p_user_id INT)
BEGIN
    IF EXISTS (SELECT 1 FROM profiles WHERE user_id = p_user_id) THEN
        DELETE FROM profiles WHERE user_id = p_user_id;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'پروفایل برای این کاربر وجود ندارد';
    END IF;
END //

-- ==================== SYMPTOMS TABLE ====================
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_symptom`(
    IN p_user_id INT,
    IN p_date_time VARCHAR(50),
    IN p_statue LONGTEXT,
    IN p_symptoms LONGTEXT
)
BEGIN
    INSERT INTO symptoms (suser_id, date_time, statue, symptoms) 
    VALUES (p_user_id, p_date_time, p_statue, p_symptoms);
    SELECT LAST_INSERT_ID() as new_symptom_id;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_symptom`(IN p_sid INT)
BEGIN
    SELECT * FROM symptoms WHERE sid = p_sid;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_user_symptoms`(IN p_user_id INT)
BEGIN
    SELECT * FROM symptoms WHERE suser_id = p_user_id 
    ORDER BY date_time DESC;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_symptom`(
    IN p_sid INT,
    IN p_date_time VARCHAR(50),
    IN p_statue LONGTEXT,
    IN p_symptoms LONGTEXT
)
BEGIN
    IF EXISTS (SELECT 1 FROM symptoms WHERE sid = p_sid) THEN
        UPDATE symptoms 
        SET date_time = p_date_time, 
            statue = p_statue, 
            symptoms = p_symptoms 
        WHERE sid = p_sid;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه علائم وجود ندارد';
    END IF;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_symptom`(IN p_sid INT)
BEGIN
    IF EXISTS (SELECT 1 FROM symptoms WHERE sid = p_sid) THEN
        DELETE FROM symptoms WHERE sid = p_sid;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه علائم وجود ندارد';
    END IF;
END //

-- ==================== MEDICINES TABLE ====================
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_medicine`(
    IN p_user_id INT,
    IN p_medicine VARCHAR(50),
    IN p_dosage VARCHAR(50),
    IN p_duration INT,
    IN p_last_taken VARCHAR(50),
    IN p_next_dose VARCHAR(50)
)
BEGIN
    INSERT INTO medicines (muser_id, medicine, dosage, duration, last_taken, next_dose) 
    VALUES (p_user_id, p_medicine, p_dosage, p_duration, p_last_taken, p_next_dose);
    SELECT LAST_INSERT_ID() as new_medicine_id;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_medicine`(IN p_mid INT)
BEGIN
    SELECT * FROM medicines WHERE mid = p_mid;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_user_medicines`(IN p_user_id INT)
BEGIN
    SELECT * FROM medicines WHERE muser_id = p_user_id 
    ORDER BY last_taken DESC;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_medicine`(
    IN p_mid INT,
    IN p_medicine VARCHAR(50),
    IN p_dosage VARCHAR(50),
    IN p_duration INT,
    IN p_last_taken VARCHAR(50),
    IN p_next_dose VARCHAR(50)
)
BEGIN
    IF EXISTS (SELECT 1 FROM medicines WHERE mid = p_mid) THEN
        UPDATE medicines 
        SET medicine = p_medicine, 
            dosage = p_dosage, 
            duration = p_duration, 
            last_taken = p_last_taken, 
            next_dose = p_next_dose 
        WHERE mid = p_mid;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه دارو وجود ندارد';
    END IF;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_medicine`(IN p_mid INT)
BEGIN
    IF EXISTS (SELECT 1 FROM medicines WHERE mid = p_mid) THEN
        DELETE FROM medicines WHERE mid = p_mid;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه دارو وجود ندارد';
    END IF;
END //

-- ==================== BMIES TABLE ====================
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_bmi`(
    IN p_user_id INT,
    IN p_date_time VARCHAR(50),
    IN p_height INT,
    IN p_weight INT,
    IN p_bmi FLOAT
)
BEGIN
    INSERT INTO bmies (suser_id, date_time, height, weight, bmi) 
    VALUES (p_user_id, p_date_time, p_height, p_weight, p_bmi);
    SELECT LAST_INSERT_ID() as new_bmi_id;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_bmi`(IN p_bid INT)
BEGIN
    SELECT * FROM bmies WHERE bid = p_bid;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `select_user_bmies`(IN p_user_id INT)
BEGIN
    SELECT * FROM bmies WHERE suser_id = p_user_id 
    ORDER BY date_time DESC;
END //

CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_bmi`(IN p_bid INT)
BEGIN
    IF EXISTS (SELECT 1 FROM bmies WHERE bid = p_bid) THEN
        DELETE FROM bmies WHERE bid = p_bid;
    ELSE
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'شناسه BMI وجود ندارد';
    END IF;
END //

DELIMITER ;