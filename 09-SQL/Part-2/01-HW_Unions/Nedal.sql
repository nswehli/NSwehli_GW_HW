drop view all_parties if exists
create view all_parties as
select 'Actor' as "Type",first_name as "First Name" , last_name as "Last Name"
from actor 
union all
select 'Customer'as "Type",first_name as "First Name" , last_name as "Last Name"
from customer
union all
select 'Staff'as "Type", first_name as "First Name" , last_name as "Last Name" from
staff

--the ID of all customers who live in the city of London
select customer_id from customer where customer_id in 
										(select id from customer_list
										where city='London')

--displaying more details of customers living in London
select * from customer where customer_id in 
										(select id from customer_list
										where city='London')


