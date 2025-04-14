-- Nth highest salary
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select case when N >= 1 then
    (select DISTINCT E.salary from employee E
    order by E.salary desc
    offset N-1
    LIMIT 1) else NULL end
  );
END;
$$ LANGUAGE plpgsql;
