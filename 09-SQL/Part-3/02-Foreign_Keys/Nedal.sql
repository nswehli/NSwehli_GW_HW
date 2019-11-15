create table employees (
employee_ID INT Primary Key
	,first_name Varchar
	,last_name Varchar
	,department_id Int
	)
	;
create table departments (
id int Primary Key
	,dept_name varchar
)
;

select * from departments

SELECT * FROM employees e
  JOIN departments d
  ON (e.department_id = d.id)
  WHERE e.department_id = 45;

  