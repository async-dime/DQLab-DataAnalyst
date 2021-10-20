/*
Fungsi Aggregate COUNT()

Syntax: 

SELECT COUNT(ColumnName)  
FROM TableName; 
*/


SELECT COUNT(FirstName) as Total_Student
From students;


/*
output:

+---------------+
| Total_Student |
+---------------+
|             5 |
+---------------+
*/