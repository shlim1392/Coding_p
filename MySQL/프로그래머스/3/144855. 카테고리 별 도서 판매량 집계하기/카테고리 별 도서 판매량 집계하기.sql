SELECT B.CATEGORY, SUM(BS.SALES) AS TOTAL_SALES
FROM BOOK_SALES BS
JOIN BOOK B ON B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY;