--List the following details of each employee: employee number, last name, first name, gender, and salary.
CREATE VIEW TotalEmployeesSalary AS
SELECT e.emp_no as "Employee Number", e.last_name as "Last Name", e.first_name as "First Name", e.gender as "Gender", s.salary as "Salary"
FROM employees e
Inner JOIN salaries s
ON (e.emp_no = s.emp_no)
;
--List employees who were hired in 1986.
CREATE VIEW YR1986_employees AS
select * from employees
where hire_date between '1986-1-1' AND '1986-12-31'
order by hire_date asc

---List the manager of each department with the following information: 
---department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
-- creating a view for hisory of manager
CREATE VIEW Managers AS
SELECT d.dept_no as "Department No."
					,d.dept_name as "Department Name"
					,e.emp_no as "Employee No."
					,e.last_name as " Last Name"
					, e.first_name as "First Name"
					, dm.from_date as " From Date"
					, dm.to_date as " To Date"
FROM employees e
Inner JOIN dept_manager dm
ON (e.emp_no = dm.emp_no)
inner join departments d
on (dm.dept_no=d.dept_no)
-- view only current manager
CREATE VIEW CurrentManagers AS
select * from Managers
where " To Date"='9999-01-01'
;

select * from dept_emp
select * from departments
select * from employees

--List the department of each employee with the following information: employee number, last name, first name, and department name.
CREATE VIEW EmployeesDepartment AS
SELECT e.emp_no as "Employee Number", e.last_name as " Last Name", e.first_name as "First Name",d.dept_name as "Department Name" 
FROM employees e
Inner JOIN dept_emp de
ON (e.emp_no = de.emp_no)
inner join departments d
on (de.dept_no=d.dept_no)
;
select * from EmployeesDepartment

--List all employees whose first name is "Hercules" and last names begin with "B."
select * from employees
where first_name= 'Hercules' and last_name like 'B%'

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
select * from EmployeesDepartment
where "Department Name" ='Sales'

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select * from EmployeesDepartment
where "Department Name" ='Sales' or "Department Name" ='Development'

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name as " Last Name", COUNT (last_name)as "Last Name Count" from employees
group by last_name
order by "Last Name Count" desc

--END


