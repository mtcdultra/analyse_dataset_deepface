
select * from emotion_analysed_mead_dataset
where dataset LIKE 'ADFE%'

select * from emotion_record
where dataset LIKE 'ADFE%'

delete from emotion_analysed_mead_dataset
delete from emotion_record
where dataset LIKE 'ADFE%'


-- MAIN RESEARCH
SELECT eamd.file_name, 
        e.emotion as emotion_returned_from_df,
        --er.original_emotion as emotion_from_mead_ds,
        eamd.equivalent_emotion_from_df,
        er.total_frames,
        max(CASE WHEN eamd.emotion == "angry" THEN eamd.classification END) as angry,       
        max(CASE WHEN eamd.emotion == "disgust" THEN eamd.classification END) as disgust,
        max(CASE WHEN eamd.emotion == "fear" THEN eamd.classification END) as fear,
        max(CASE WHEN eamd.emotion == "neutral" THEN eamd.classification END) as neutral,
        max(CASE WHEN eamd.emotion == "sad" THEN eamd.classification END) as sad,
        max(CASE WHEN eamd.emotion == "surprise" THEN eamd.classification END) as surprise,
        max(CASE WHEN eamd.emotion == "happy" THEN eamd.classification END) as happy
FROM emotion_analysed_mead_dataset eamd
INNER JOIN emotion_record er ON er.file_name = eamd.file_name
INNER JOIN emotion e ON e.id = er.emotion_captured
--WHERE eamd.file_name LIKE "ADF%"
--WHERE er.file_name = "ADFES-BIV_F01-Fear%"
--WHERE er.dataset = "ADFxxx%"
GROUP BY eamd.file_name
--ORDER BY er.registration_date DESC, eamd.file_name;
order by eamd.file_name;


-- ########################################################################

-- MAIN RESEARCH
SELECT eamd.file_name, 
        e.emotion as emotion_returned_from_df,
        --er.original_emotion as emotion_from_mead_ds,
        eamd.equivalent_emotion_from_df,
        er.total_frames,
        max(CASE WHEN eamd.emotion == "angry" THEN eamd.classification END) as angry,       
        max(CASE WHEN eamd.emotion == "disgust" THEN eamd.classification END) as disgust,
        max(CASE WHEN eamd.emotion == "fear" THEN eamd.classification END) as fear,
        --max(CASE WHEN eamd.emotion == "neutral" THEN eamd.classification END) as neutral,
        max(CASE WHEN eamd.emotion == "sad" THEN eamd.classification END) as sad,
        max(CASE WHEN eamd.emotion == "surprise" THEN eamd.classification END) as surprise,
        max(CASE WHEN eamd.emotion == "happy" THEN eamd.classification END) as happy,
        eamd.dataset
FROM emotion_analysed_mead_dataset eamd
INNER JOIN emotion_record er ON er.file_name = eamd.file_name
INNER JOIN emotion e ON e.id = er.emotion_captured
--WHERE eamd.file_name LIKE "ADF%"
--WHERE er.file_name = "ADFES-BIV_F01-Fear%"
WHERE eamd.dataset = "ADFES-BIV"
and eamd.file_name NOT LIKE "%Contempt%"
GROUP BY eamd.file_name
ORDER BY er.registration_date DESC, eamd.file_name;

-- ########################################################################

-- MAIN RESEARCH
SELECT eamd.file_name, 
        e.emotion as emotion_returned_from_df,
        --er.original_emotion as emotion_from_mead_ds,
        eamd.equivalent_emotion_from_df,
        er.total_frames,
        max(CASE WHEN eamd.emotion == "angry" THEN eamd.classification END) as angry,       
        max(CASE WHEN eamd.emotion == "disgust" THEN eamd.classification END) as disgust,
        max(CASE WHEN eamd.emotion == "fear" THEN eamd.classification END) as fear,
        --max(CASE WHEN eamd.emotion == "neutral" THEN eamd.classification END) as neutral,
        max(CASE WHEN eamd.emotion == "sad" THEN eamd.classification END) as sad,
        max(CASE WHEN eamd.emotion == "surprise" THEN eamd.classification END) as surprise,
        max(CASE WHEN eamd.emotion == "happy" THEN eamd.classification END) as happy,
        eamd.dataset
FROM emotion_analysed_mead_dataset eamd
INNER JOIN emotion_record er ON er.file_name = eamd.file_name
INNER JOIN emotion e ON e.id = er.emotion_captured
--WHERE eamd.file_name LIKE "ADF%"
--WHERE er.file_name = "ADFES-BIV_F01-Fear%"
WHERE eamd.dataset = "MEAD"
and eamd.file_name NOT LIKE "%ontempt%"
GROUP BY eamd.file_name
ORDER BY er.registration_date DESC, eamd.file_name;

-- ########################################################################
        SELECT  *
        FROM    emotion_analysed_mead_dataset
        WHERE file_name NOT LIKE "%ontempt%"

        SELECT  file_name, original_emotion, emotion_captured_name, dataset
        FROM    emotion_record
        WHERE file_name NOT LIKE "%ontempt%"

select dataset from emotion_record group by dataset

SELECT  *
FROM    emotion_analysed_mead_dataset
where   dataset like "MEAD"
and file_name = "W024_video_front_fear_level_1_016"

SELECT  file_name, original_emotion, emotion_captured_name, dataset
FROM    emotion_record
--where dataset = "ADFES-BIV"
where dataset = "MEAD"

SELECT  *
FROM    emotion_record
where emotion_captured_name is null


SELECT  *
FROM    emotion_analysed_mead_dataset
where emotion_captured_name is null


where emotion_captured is null
--where   dataset like "MEAD"
--WHERE dataset = "ADFES-BIV"



id	emotion
1	sad
2	angry
3	surprise
4	fear
5	happy
6	disgust
7	neutral
8	non

-- ########################################################################

-- Counting number
--select count(file_name)
select * 
from emotion_analysed_mead_dataset 
--where file_name like "lfw%" 
--where file_name like "ck%" 
--where file_name like "fe%" 
--where file_name like "ad%"
order by file_name





select * from emotion
SELECT id FROM emotion WHERE emotion = 'sad'


--INSERT INTO emotion_record (emotion_captured, file_name) VALUES (1, 'M034/video/front/happy/level_3/008')
--delete from emotion_record where qty_emotion_captured is NULL

select * from emotion_record

select er.file_name, er.original_emotion, e.emotion as emotion_returned_from_df, er.total_frames AS total_frames_captured, er.qty_emotion_captured, er.registration_date 
from emotion_record er
inner join emotion e on er.emotion_captured = e.id
order by file_name

select * from emotion_analysed_mead_dataset



DELETE FROM emotion_record
WHERE id NOT IN (
    SELECT MIN(id)
    FROM emotion_record
    GROUP BY file_name
);


DELETE FROM emotion_record
WHERE id NOT IN (
    SELECT MIN(file_name, emotion)
    FROM emotion_analysed_mead_dataset
    --WHERE file_name = 'W024_video_front_fear_level_1_001'
    GROUP BY file_name, emotion
);




select * from emotion_record order by registration_date desc

--delete from emotion_record where id in (
select * from emotion_record where file_name LIKE "M011%" 
--)

--delete from emotion_analysed_mead_dataset where file_name in (
select file_name from emotion_analysed_mead_dataset where file_name LIKE "et_%" 
--)

SELECT *
FROM emotion_analysed_mead_dataset
group by file_name, classification, emotion
order by file_name, emotion
HAVING count(file_name) >1

-- APAGAR REGISTROS DUPLICADOS
delete from emotion_record
where id in (
SELECT id
FROM emotion_record
group by file_name
HAVING count(file_name) >1
)

select * FROM
emotion_record 
where file_name = 'W024_video_front_disgusted_level_3_002'



SELECT file_name from emotion_record WHERE file_name = 'W024_video_front_sad_level_3_037'