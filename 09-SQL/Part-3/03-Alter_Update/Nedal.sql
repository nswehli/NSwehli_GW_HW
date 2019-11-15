--part 1
--Alter allows modifications to the structure of the table (add/delete columns, rename columns, change data type)
--Update allows changes to the records within the table

--part 2
create table employees (
employee_ID INT Primary Key
	,first_name Varchar
	,last_name Varchar
	,department_id Int
	)
	;

--Change the name of the column from `department_id` to `dept_id`.
alter table employees
RENAME department_id to dept_id

--Add a column named `annual_salary` to the table.
alter table employees
ADD COLUMN annual_salary int

select * from employees
