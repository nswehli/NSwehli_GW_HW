CREATE TABLE "employees" (
    "emp_no" varchar  PRIMARY KEY,
    "birth_date" Date   NOT NULL,
    "first_name" varchar   NOT NULL,
    "last_name" varchar   NOT NULL,
    "gender" varchar   NOT NULL,
    "hire_date" Date   NOT NULL
);

CREATE TABLE "departments" (
    "dept_no" varchar   Primary Key ,
    "dept_name" varchar   NOT NULL
);


CREATE TABLE "titles" (
    "emp_no" varchar   PRIMARY KEY,
    "title" varchar   NOT NULL,
    "from_date" Date   NOT NULL,
    "to_date" Date   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
	)
;

CREATE TABLE "salaries" (
    "emp_no" varchar  PRIMARY KEY,
    "salary" int   NOT NULL,
    "from_date" Date   NOT NULL,
    "to_date" Date   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);


CREATE TABLE "dept_manager" (
    "dept_no" varchar   NOT NULL,
    "emp_no" varchar  NOT NULL,
    "from_date" Date   NOT NULL,
    "to_date" Date   NOT NULL,
	PRIMARY KEY (dept_no, emp_no),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);

CREATE TABLE "dept_emp" (
    "emp_no" varchar  NOT NULL,
    "dept_no" varchar  NOT NULL,
    "from_date" Date   NOT NULL,
    "to_date" Date   NOT NULL,
	PRIMARY KEY (dept_no, emp_no),
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);

