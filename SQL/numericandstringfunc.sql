-- numeric functions
select abs(-10) from dual;
select power(6,3) from dual;
select round(10.25,1) from dual;
select sqrt(25) from dual;
select exp(3) from dual;
select greatest(10,20,30,40) from dual;
select least (10,20,30,10) from dual;
select mod(7,2) from dual;
select floor(158.59) from dual;
select ceil(158.1) from dual;

-- string functions
select upper(empname)as name from emp1;
select lower(empname) as name from emp1;
-- select initcap(empname) as name from emp1;
select ascii('a') from dual;
select substr(empname,2) from emp1;
select instr('this is the is this','is') from dual;
select length('this is the is this') from dual;
select ltrim('    hello') from dual;
select rtrim('hello         ') from dual;
-- select trim('hello',2) from dual;
-- select vsize() from dual;
select lpad('hello',7,'*') from dual;
select rpad('hello',7,'#') from dual;
-- select translate('hello','e','m') from dual;
select replace('hello','e','m') from dual;
select concat(empname,'   id is-',empid) from emp1;







