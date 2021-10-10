/*
Fungsi Text LENGTH()

Syntax: 

SELECT LENGTH(ColumnName)
FROM TableName; 
*/


SELECT StudentID, FirstName, LENGTH(FirstName) as Total_Char
FROM students;


/*
output:

+-----------+-----------+------------+
| StudentID | FirstName | Total_Char |
+-----------+-----------+------------+
|         1 | Jose      |          4 |
|         2 | Lala      |          4 |
|         3 | Sultan    |          6 |
|         4 | Jaya      |          4 |
|         5 | Anjali    |          6 |
+-----------+-----------+------------+
*/