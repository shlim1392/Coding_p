-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC;

'''
이 쿼리는 ONLINE_SALE 테이블에서 USER_ID와 PRODUCT_ID로 그룹을 지어 중복된 조합을 찾은 후,
HAVING COUNT(*) > 1 조건을 통해 해당 그룹이 두 번 이상 등장한 경우만 선택합니다. 
'''
