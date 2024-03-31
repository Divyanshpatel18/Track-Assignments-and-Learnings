SELECT * FROM sqlpractice.emp1;
select deptname from dept1 where deptid in( select deptid from emp1 group by deptid having count(*)>2);
select deptname from dept1 d inner join emp1 e on d.deptid=e.deptid group by deptname having count(*) >2;