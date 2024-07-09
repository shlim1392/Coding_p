with shortlist as (
SELECT category, max(price) as mx
from food_product
where category in ('과자','국','김치','식용유')
group by 1)

select category, price as max_price, product_name
from food_product
where (category,price) in (select category,mx from shortlist)
order by 2 desc;