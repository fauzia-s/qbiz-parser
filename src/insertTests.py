
# insertTest1 = "INSERT INTO employee (id, name, dept, age, salary location) SELECT emp_id, emp_name, dept, age, salary, location FROM temp_employee;"
insertTest1 = "INSERT INTO employee (id, name, dept) SELECT emp_id, emp_name, dept FROM temp_employee;"
insertTest2 = "INSERT INTO employee SELECT * FROM temp_employee;"
insertTest3 = "INSERT INTO employee (id, name, dept, age, salary, location) VALUES (105, 'Srinath', 'Aeronautics', 27, 33000);"
insertTest4 = "INSERT INTO employee (id, name, dept) SELECT emp_id, emp_name, dept FROM (select * from temp_employee te join temp_manager tm ON tm.key = te.manager_key) x;"
insertTest5 = "INSERT INTO employee (id, name, dept) VALUES (106, 'Sam', 'IT', 33, 50000) ON DUPLICATE KEY UPDATE id=id+1;"
insertTest6 = "INSERT INTO employee (id, name, dept) SELECT emp_id, emp_name, dept FROM temp_employee t UNION SELECT emp_id, emp_name, dept FROM temp_manager e ON DUPLICATE KEY UPDATE id = id + t.id;"
insertTest7 = "INSERT INTO employee (id, name, dept) SELECT * FROM (SELECT emp_id, emp_name, dept FROM temp_employee t UNION SELECT emp_id, emp_name, dept FROM temp_manager e) t_emp ON DUPLICATE KEY UPDATE id = id + t.id;"

# creatTest1 = "CREATE TABLE temp_employee AS SELECT * FROM employee;"


# Build the parser
from sql_yacc import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()

result = parser.parse(insertTest1, debug=False)
assert result == ('employee', {'temp_employee'})
tables.clear()

result = parser.parse(insertTest2)
assert result ==  ('employee', {'temp_employee'})
tables.clear()

result = parser.parse(insertTest3, debug=False)
assert result == ('employee', None)
tables.clear()

result = parser.parse(insertTest4, debug=False)
assert result == ('employee', {'temp_employee', 'temp_manager'})
tables.clear()

result = parser.parse(insertTest5, debug=False)
assert result == ('employee', None)
tables.clear()

result = parser.parse(insertTest6, debug=False)
assert result == ('employee', {'temp_employee', 'temp_manager'})
tables.clear()

result = parser.parse(insertTest7, debug=False)
assert result == ('employee', {'temp_employee', 'temp_manager'})
tables.clear()


print("Pass")
