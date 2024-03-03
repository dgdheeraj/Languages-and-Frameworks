# Relational Databases

SQL: Structured Query Leanguage used to interact with relational db.

## SQL Commands
- Data Definition Language (eg: for creating database structure)
- Data Manipulation Language (to update data)
- Data Query Language (to retreive data)
- Data Control Language (to grant/revoke access)

## Index
An index is a schema object. It is used by the server to speed up the retrieval of rows by using a pointer. It can reduce disk I/O(input/output) by using a rapid path access method to locate data quickly.

An index helps to speed up select queries and where clauses, but it slows down data input, with the update and the insert statements. Indexes can be created or dropped with no effect on the data

```
CREATE INDEX index
ON TABLE column;

CREATE INDEX index
ON TABLE (column1, column2,…..);

CREATE UNIQUE INDEX index
ON TABLE column;
```

### Index
An index is a data structure that improves the speed of data retrieval operations on a database table.
It consists of a set of keys (values) and pointers to the corresponding rows in the table.

#### Use Cases
- Improve the speed of SELECT, WHERE, and JOIN operations.
- Can be created on columns with duplicate values.

### Unique Index
A unique index is a type of index that enforces the uniqueness of values in one or more columns. It behaves like a regular index but with the added constraint that the indexed columns must have unique values across all rows in the table.

#### Use Cases
- Enforce uniqueness in one or more columns.
- Automatically created when defining a primary key or a unique constraint.


<br>
<br>
Indexes store data in a serial fashion which speedup search from O(N) to O(logN) by employing binary search instead of linear search
Internally Indexes are stored using data structures like B Trees, Hash Tables, etc.
<br>
<br>

### Questions
1) Why do indexes slow down UPDATE AND INSERT?
- Index Maintainence: When a row is inserted or updated, the corresponding indexes must be updated to reflect the changes. For insert operations, new index entries need to be created. For update operations, existing index entries may need to be deleted and new ones added. This additional work for maintaining indexes during updates and inserts can contribute to increased processing time.
- Additional I/O Operations due to updation of index
- When performing bulk updates or inserts, the overhead of index maintenance can become more noticeable.

### Links: 
- [Understand more on Multi Column Indexes](https://www.atlassian.com/data/sql/multicolumn-indexes)
- [How DB Indexing Works](https://stackoverflow.com/questions/1108/how-does-database-indexing-work)

## Transaction
Grouping operations into a single unit
- Atomicity: All or nothing
- Consistency: Transcations maintain integrity by moving db from one valid state to another
- Isolation: Concurrent Transcations isolated from each other
- Durability: Once transcation is committed, its modifications remain in effect even in case of a system failure.

```
BEGIN TRANSACTION transaction_name ;
SET TRANSACTION [ READ WRITE | READ ONLY ];
COMMIT;
COMMIT;
ROLLBACK;
SAVEPOINT SAVEPOINT_NAME;
ROLLBACK TO SAVEPOINT_NAME;
RELEASE SAVEPOINT SAVEPOINT_NAME;
```

### Questions
1) What happens if two different connections to a Postgres server have two transcations running concurrently, what is the output seen?
Postgres has multiple isolation levels for such scenarios.
- <b>Read Committed</b>: Default isolation level. Transactions can only see changes that have been committed. It avoids dirty reads but may still allow non-repeatable reads and phantom reads.
- <b>Serializable</b>: This is the highest isolation level. Ensures complete isolation from other transactions. Prevents dirty reads, non-repeatable reads, and phantom reads. It achieves this by placing locks on the accessed data, potentially leading to increased contention and blocking.

### Definitions
- Dirty Reads: When one transaction reads uncommitted data of another transcation
- Non-Repeatable Read: Occurs when a transaction reads the same data multiple times within its own transaction, and the data changes between those reads due to another committed transaction.
- Phantom Read: Occurs when a transaction reads a set of rows that satisfy a certain condition, but another transaction inserts, updates, or deletes rows that also satisfy the condition before the first transaction completes.