SELECT I.ANIMAL_ID,
       I.ANIMAL_TYPE,
       I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O USING (ANIMAL_ID)
WHERE SEX_UPON_INTAKE LIKE "Intact%" AND SEX_UPON_OUTCOME NOT LIKE "Intact%"
ORDER BY ANIMAL_ID;