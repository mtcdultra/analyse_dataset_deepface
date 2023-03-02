CREATE TABLE emotion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emotion CHAR (20)
);

DROP TABLE emotion_record;

CREATE TABLE emotion_record (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_name TEXT,
    total_frames INTEGER,
    fps  FLOAT,
    original_emotion TEXT,
    emotion_captured INTEGER,
    duration    FLOAT,
    qty_emotion_captured INT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(emotion_captured) REFERENCES emotion(id)
);

CREATE TABLE emotion_analysed_mead_dataset (
    file_name TEXT,
    emotion TEXT,
    classification INTEGER
);

CREATE TABLE dataset_name (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset CHAR (20)
);


--Alter table [sua tabela] add [sua_coluna] as CASE WHEN CIDADE = 'RIO DE JANEIRO' AND MÊS = 'JANEIRO' THEN Valor ELSE 0 END


ALTER TABLE emotion_record
  ADD emotion_captured_name TEXT;

ALTER TABLE emotion_record
  ADD dataset TEXT;

select * from emotion_analysed_mead_dataset order by file_name
select * from emotion_analysed_mead_dataset where equivalent_emotion_from_df IS NULL

select * from emotion_analysed_mead_dataset where file_name LIKE "CK%"

select * from emotion

select * from emotion_record
where file_name not like %Contempt%"
and original_emotion is null


-- ########################################################################

update emotion_record
set original_emotion = "sad"
where file_name LIKE "%Sadness%";

update emotion_record
set original_emotion = "anger"
where file_name LIKE "%Anger%";

update emotion_record
set original_emotion = "happy"
where file_name LIKE "%Joy%";

update emotion_record
set original_emotion = "disgust"
where file_name LIKE "%Disgu%";

update emotion_record
set original_emotion = "neutral"
where file_name LIKE "%Neutra%";

update emotion_record
set original_emotion = "fear"
where file_name LIKE "%Fear%";

update emotion_record
set original_emotion = "surprise"
where file_name LIKE "%Surprise%";



-- ########################################################################

update emotion_record
set dataset = "ADFES-BIV"
where file_name LIKE "ADFES%";

update emotion_record
set dataset = "CKPLUS"
where file_name LIKE "ckpl%";

update emotion_record
set dataset = "MEAD"
where file_name LIKE "W0%";

update emotion_record
set dataset = "MEAD"
where file_name LIKE "M0%";

update emotion_record
set dataset = "FER-2013"
where file_name LIKE "fer%";

update emotion_record
set dataset = "LFW"
where file_name LIKE "lfw%";

ADFES-BIV_practice_F06-Embarrass
ADFES-BIV_practice_F06-Pride


INSERT INTO dataset_name (dataset) VALUES ('MEAD');
INSERT INTO dataset_name (dataset) VALUES ('FEAR-2013');
INSERT INTO dataset_name (dataset) VALUES ('ADFES-BIV');
INSERT INTO dataset_name (dataset) VALUES ('lfw-deepfunneled');
INSERT INTO dataset_name (dataset) VALUES ('ckplus');


INSERT INTO emotion(emotion) VALUES('sad');
INSERT INTO emotion(emotion) VALUES('angry');
INSERT INTO emotion(emotion) VALUES('surprise');
INSERT INTO emotion(emotion) VALUES('fear');
INSERT INTO emotion(emotion) VALUES('happy');
INSERT INTO emotion(emotion) VALUES('disgust');
INSERT INTO emotion(emotion) VALUES('neutral');
INSERT INTO emotion(emotion) VALUES('non');
