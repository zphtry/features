# Общие операции
* `CREATE USER <username> WITH PASSWORD 'password';`
* `CREATE DATABASE <db_name> OWNER <username>;`
* `ALTER USER <username> WITH ENCRYPTED PASSWORD '<password>';`

# Операции с таблицами
* `CREATE TABLE <table> (<col1> <type>, <col2> <type>);`
* `ALTER TABLE <table> ADD <col> <type>;`
* `ALTER TABLE <table> ADD CONSTRAINT <table>_id_pk PRIMARY KEY (<id_col>);`
* `ALTER TABLE <table> DROP <col>;`
* `DROP TABLE <table>;`

# Операции с записями

## INSERT
* `INSERT INTO <table> (<col1>, <col2>) VALUES ('<val1>', '<val2>');`

## SELECT
* `SELECT * FROM <table>;`
* `SELECT <col1>, <col2> FROM <table>;`

### DISTINCT
* `SELECT DISTINCT <col1> FROM <table>;`
* `SELECT DISTINCT ON (<expression_to_distinct>) * FROM <table>;`

### ORDER BY
* `SELECT * FROM <table> ORDER BY <col1> <ASC | DESC>, <col2> <ASC | DESC>;`

### WHERE
Операторы:
* `=, >, <, >=, <=, !=`
* `AND, OR, NOT`
* `IN ('val1', 'val2',...), BETWEEN <low> AND <high>`
* `LIKE 'p_ttern%', ILIKE` `_` - один любой символ, `%` - любая последовательность символов

Пример:
* `SELECT * FROM <table> WHERE <col1>='val1';`
* `SELECT * FROM <table> WHERE <col1> IN ('val1', 'val2');`

### LIMIT
* `SELECT * FROM <table> LIMIT 3;`
* `SELECT * FROM <table> LIMIT 3 OFFSET 2;`

### FETCH - какой-то очень странный аналог LIMIT
* `SELECT * FROM <table> FETCH FIRST 3 ROW ONLY`;
* `SELECT * FROM <table> OFFSET 2 ROW FETCH FIRST 3 ROW ONLY`;

### ALIAS (AS)
Объединение строк: `||`
* `SELECT <col1> || <col2> AS <alias_name> FROM <table> ORDER BY <alias_name>`;

### GROUP BY (HAVING)
Два агрегирующих оператора:
* `SUM` и `COUNT`

_Небольшое замечание: в колонки (после_ `SELECT`_) может выводиться либо название группы либо агрегирующая функция над параметром, которая соберёт много значений из группы в одно. Также и в условии_ `HAVING` _может использоваться одно из описанных значений._

Примеры:
* `SELECT <col1>, SUM(<col2>) FROM <table> GROUP BY <col1>;`
* `SELECT <col1>, SUM(<col2>) FROM <table> GROUP BY <col1> HAVING SUM(<col2>) > 10;`

### INNER JOIN
Симметричное соединение двух таблиц, в максимальном случае дающее m * n рядов. Каждому ряду из первой таблицы будут соответствовать все ряды из второй.  
Как правило, одна таблица является для другой внешним ключом и в условии записывается равенство внешнего ключа для первой таблицы и первичного ключа для второй.
* `SELECT * FROM <table1> INNER JOIN <table2> ON <condition>;`

### LEFT JOIN
Присоединение второй таблицы к первой. Число рядов в итоге равняется как минимум числу рядов в первой таблицы, как максимум `m * n`. Если ряд из второй таблицы не подходит по условию, он заполняется `null`.
* `SELECT * FROM <table1> LEFT JOIN <table2> ON <condition>;`

### FULL [OUTER] JOIN
Объединение `LEFT JOIN` и `RIGHT JOIN`

### CROSS JOIN
Простое произведение таблиц. `INNER JOIN` в предельном случае. Отличается от предыдущих, что здесь нет условия после `ON`.
* `SELECT * FROM <table1> CROSS JOIN <table2>;`

## UPDATE


## DELETE
* `DELETE FROM <table> WHERE <condition about column>;`