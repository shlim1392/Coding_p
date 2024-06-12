SELECT COUNT(*) FISH_COUNT, NI.FISH_NAME
FROM FISH_INFO I
JOIN FISH_NAME_INFO NI ON I.FISH_TYPE = NI.FISH_TYPE
GROUP BY NI.FISH_NAME
ORDER BY FISH_COUNT DESC;