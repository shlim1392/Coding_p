WITH TEMP AS (
    SELECT FISH_TYPE, AVG(CASE WHEN LENGTH < 10 THEN 10 ELSE LENGTH END) AS AVG_L
    FROM FISH_INFO
    GROUP BY FISH_TYPE
    HAVING AVG(CASE WHEN LENGTH < 10 THEN 10 ELSE LENGTH END) > 33
)

SELECT COUNT(ID) AS FISH_COUNT,
       MAX(LENGTH) AS MAX_LENGTH,
       FISH_TYPE
FROM FISH_INFO
WHERE FISH_TYPE IN (SELECT FISH_TYPE FROM TEMP)
GROUP BY FISH_TYPE
ORDER BY FISH_TYPE ASC;
