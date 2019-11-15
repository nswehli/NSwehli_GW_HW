drop view If exists title_count 

Create View title_count AS 
SELECT f.title, count(i.inventory_id) as "Number of Copies" 
FROM inventory i
Inner JOIN film f ON i.film_id=f.film_id
GROUP BY title
order by "Number of Copies" desc
;

select * from title_count
where "Number of Copies"=7
order by title
;

