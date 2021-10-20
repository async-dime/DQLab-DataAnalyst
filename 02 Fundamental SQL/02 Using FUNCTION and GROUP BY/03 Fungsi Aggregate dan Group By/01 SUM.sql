/*
Fungsi Aggregate SUM()

Syntax: 

SELECT SUM(ColumnName)  
FROM TableName; 
*/


SELECT SUM(Semester1) as Total_1, SUM(Semester2) as Total_2
FROM students;


/*
output:

+---------+---------+
| Total_1 | Total_2 |
+---------+---------+
|   361.7 |  356.35 |
+---------+---------+
*/