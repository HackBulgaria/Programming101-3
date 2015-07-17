# Database relationships

In the relational database world, relations are a key concept that helps us model our data.

**The idea is to define how two tables are connected in terms of their data.**

Lets have the following example:

* We want to have a databases, holding users in our blog system. We will have the following schemas:

```sql
CREATE TABLE Users(
  user_id INTEGER PRIMARY KEY,
  user_name TEXT,
  user_email TEXT
)

CREATE TABLE Posts(
  post_id INTEGER PRIMARY KEY,
  post_title TEXT,
  post_content TEXT,
  author INTEGER
)
```

The interesting part is the connection between a post and his author.

Should we keep the author's name? Or his email? Or should we use the fact that PK will always give us a unique row from `Users`.

Then, what happens if we keep in the `author` column, the `user_id` of the given user, that wrote the post?

We can have data like that:

| user_id | user_name | user_email                |
|---------|-----------|---------------------------|
| 1       | RadoRado  | radorado@hackbulgaria.com |
| 2       | Ivo       | ivaylo@hackbulgaria.com   |
| 3       | Tony      | tony@hackbulgaria.com     |

and

| post_id | post_title  | post_content            | author |
|---------|-------------|-------------------------|--------|
| 1       | Hello World | The first blog post     | 1      |
| 2       | New courses | Something interesting.. | 3      |


Then the `author` column holds the `user_id` of the given user. We have now built a relationship!

* **Such relationship is called 1:N or one-to-many!**
* The `author` column is called a **foreign key**, because it holds values that are values of a primary key column elsewhere!

## 1:N relationship

The one-to-many relationship can be described as follows:

* One user can have many articles
* One article has only 1 author (user)

This means that we can have repating values in the `author` column in `Posts`.

**1:N relationships are build using Foreign keys.**

## N:M relationship

This is called **many-to-many** relationship.

Lets have the following example:

* We want to have students
* We want to have courses
* One student can go to multiple courses
* One course can be attented by mutiple students

How do we model such relationship in our database?

For many-to-many relations, we always need something, that is called a **junction table!**

Our tables would look like that:

**Students:**

| student_id | student_name |
|------------|--------------|
| 1          | Ivo          |
| 2          | Maria        |
| 3          | Tony         |
| 4          | Rado         |
| 5          | Rosi         |
| 6          | Ani          |

and **Courses:** 

| course_id | course_name   |
|-----------|---------------|
| 1         | 101           |
| 2         | Java          |
| 3         | JS            |
| 4         | Ruby on Rails |
| 5         | NodeJS        |
| 6         | Algorithms    |

and the **junction table**:

| student_id | course_id |
|------------|-----------|
| 1          | 1         |
| 2          | 1         |
| 3          | 1         |
| 4          | 2         |
| 5          | 2         |
| 6          | 6         |


As you can see, each row in the junction table tells us which student is attending which course! This is our relation.

**In the junction table, both columns are foreign keys to the tables in the many-to-many relation!**


## Foreign Keys

We have two type of keys - Primary (PK) and Foreign (FK).

If a column is a PK for the table, it can hold only unique values. And one value from that column should be able to "identify" the entire row. If we search in the `WHERE` clause with a PK, we should always get 1 value.

FK are different. They are used to express relations between two tables.

In the previous examples, the `author` column was a FK column. `student_id` and `course_id` in the junction table are FKs too.

Here is the deal with the FK:

* This is a **constraint** over what values can be inserted in the column, defined as a foreign key.
* Usually, when you define your table, you say that a given column is going to be a FK to another table's PK column.

Lets see the SQL for that:


```sql
CREATE TABLE Users(
  user_id INTEGER PRIMARY KEY,
  user_name TEXT,
  user_email TEXT
)

CREATE TABLE Posts(
  post_id INTEGER PRIMARY KEY,
  post_title TEXT,
  post_content TEXT,
  author INTEGER,
  FOREIGN KEY(author) REFERENCES Users(user_id)
)
```

There is an additional `FOREIGN KEY` statement. This is the required thing.

Now if we run sqlite3:

```
sqlite> PRAGMA foreign_keys = ON;
sqlite> INSERT INTO Posts(post_title, post_content, author)
...     VALUES("Test", "Test", 1);
SQL error: foreign key constraint failed
```

**Here is the SQL for the Student-Courses tables:**

```sql
CREATE TABLE Students(
  student_id INTEGER PRIMARY KEY,
  student_name TEXT
)

CREATE TABLE Courses(
  course_id INTEGER PRIMARY KEY,
  course_name TEXT
)

CREATA TABLE Student_To_Course(
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY(student_id) REFERENCES Students(student_id),
  FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)
```

Now, when you have the general idea, you can read more about FK's here - https://www.sqlite.org/foreignkeys.html
