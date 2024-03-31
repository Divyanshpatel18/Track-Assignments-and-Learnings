with mycte as (
select e.name,e.salary,m.name as manager_name,m.salary as manager_salary from emp2 e inner join emp2 m on e.managerId=m.empId where e.salary>m.salary
)  
select name,salary from mycte;

select * from emp1;
select empid,deptid,
sum(salary) over(partition by deptid) as 'total salary',
avg(salary) over(partition by deptid) as 'avg salary',
count(salary) over(partition by deptid) as 'count salary',
max(salary) over(partition by deptid) as 'maximum salary',
min(salary) over(partition by deptid) as 'minimum salary'
from emp1;


select deptid,
row_number() over(order by deptid) as 'row',
rank() over(order by deptid) as 'rank',
dense_rank() over(order by deptid) as 'dense rank',
percent_rank() over(order by deptid) as 'percentrank'
from emp1;
