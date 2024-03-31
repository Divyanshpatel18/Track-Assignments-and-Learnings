SELECT * FROM sqlpractice.emp1;
SELECT * FROM sqlpractice.emp1;
select emp3.*,(select max(salary) from emp3) from emp3;
select emp3.*,max(salary) over() from emp3;
select empid,name,department, max(salary) over (partition by department) from emp3 ;
select * , row_number() over(partition by deptid )  from emp1 order by deptid;
-- top 2 employee
select *  from (select *, row_number() over(partition by deptid order by empid) R
from emp1)as subquery  where R<=2;
-- NTH  HIGHEST SALARY USING WINDOW FUNC
select distinct salary from (
select e.*, dense_rank() over(order by salary desc)R from emp1 e) as subquery
where R=5;
-- TOP 2 HIGHEST PAID EMPLOYEE IN THE DEPARTMENT
select * from (
select e.*,dense_rank() over(partition by deptid order by salary desc)R from emp1 e) as subquery
where R<=2;

-- PRINT PREVIOUS EMPLOYEE SALARY INFRONT OF EACH EMPLOYEE
select e.* ,lag(salary,1,0) over(order by salary)"prev_emp_salary" from emp1 e;

-- --COMP WITH PREVIOUS SALARY AND PRINT HIGHER LOW AND EQUAL
select *,
case when salary>prev_salary then 'higher'
     when salary<prev_salary then 'lower'
     else 'equal'
end as salarycomp
from(
select * ,lag(salary,1,0) over(order by empid)'prev_salary' from emp1 e) as subquery;

-- case in sql
select empid,
case
  when city="mumbai" then "metrocity"
  when city="pune" then "non metro"
  else "don't know"
end as is_metro
from emp1;
