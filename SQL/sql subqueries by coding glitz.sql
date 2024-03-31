SELECT * FROM sqlpractice.emp2;
-- codeglitz subquery in sql
-- salary of emp greater than managers
select e.name,e.salary,m.name,m.salary from emp2 e inner join emp2 m  on e.managerId=m.empId where e.salary>m.salary;
-- in below query we can not fetch manager details
select e.name,e.salary from emp2 e where e.salary>(select m.salary from emp2 m where e.managerId=m.empId);
-- for manager as well as emp
select e.name,e.salary,m.name,m.salary from  emp2 e 
inner join
(select * from emp2 e where empid in (select managerId from emp2))m
on e.managerId=m.empId and e.salary>m.salary;
-- emp and their manager name
select e.name,(select m.name from emp2 m where e.managerId=m.empId) from emp2 e;
-- nth highest salary
select distinct salary from emp2 order by salary desc limit 1,1;
select distinct salary from (
select salary,
   dense_rank() over (order by salary desc)R
   from emp2) as subquery
   where R=2;
