CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(8)
    );
INSERT INTO users VALUES(1,'m','m');
INSERT INTO users VALUES(2,'n','n');
CREATE TABLE profiles (
        user_id INTEGER UNIQUE,
        national_id VARCHAR(10) PRIMARY KEY,
        name VARCHAR(50),
        gender ENUM('زن','مرد'),
        age INTEGER,
        tel VARCHAR(11),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
INSERT INTO profiles VALUES(1,'9874567454','m','زن',3,'09874568876');
INSERT INTO profiles VALUES(2,'4534565432','v','مرد',3,'09675436678');    
CREATE TABLE bmies (
        bid INTEGER PRIMARY KEY AUTO_INCREMENT,
        suser_id INTEGER,
        date_time VARCHAR(50) UNIQUE,
        height INT,
        weight INT,
        bmi float,  
        FOREIGN KEY (suser_id) REFERENCES users(id)
    );
INSERT INTO bmies VALUES(3,1,'2025-09-06 21:50:07',120,10,6.9);
INSERT INTO bmies VALUES(4,1,'2025-09-06 22:57:08',180,120,37);
CREATE TABLE symptoms (
        sid INTEGER PRIMARY KEY AUTO_INCREMENT,
        suser_id INTEGER,
        date_time VARCHAR(50) UNIQUE,
        statue LONGTEXT,
        symptoms LONGTEXT,  
        FOREIGN KEY (suser_id) REFERENCES users(id)
    );
CREATE TABLE medicines (
        mid INTEGER PRIMARY KEY AUTO_INCREMENT,
        muser_id INTEGER,
        medicine VARCHAR(50),
        dosage VARCHAR(50),
        duration INTEGER,
        last_taken VARCHAR(50),
        next_dose VARCHAR(50),
        FOREIGN KEY (muser_id) REFERENCES users(id)
    );
COMMIT;
