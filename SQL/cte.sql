with my_cte as(
select * from dept1 where deptid in( select deptid from emp1 group by deptid having count(*)>2)
) 
select deptname from my_cte;