-- Part I

-- 1. Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)

-- create table customer(
-- id serial primary key,
-- first_name varchar(50),
-- last_name varchar(50) not null)

-- create table customer_profile(
-- id serial,
-- isLoggedIn boolean default false,
-- customer_id integer primary key,
-- constraint fk_customer_id foreign key (customer_id) references customer (id)
-- )

-- 2. Insert those customers

-- John, Doe
-- Jerome, Lalu
-- Lea, Rive

-- insert into customer values
-- (default, 'John', 'Doe'),
-- (default, 'Jerome', 'Lalu'),
-- (default, 'Lea', 'Rive')

-- 3. Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in

-- insert into customer_profile values
-- (default, true, (select id from customer where first_name = 'John' and last_name = 'Doe') ),
-- (default, default, (select id from customer where first_name = 'Jerome' and last_name = 'Lalu'))

-- 4. Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- The number of customers that are not LoggedIn

-- select c.first_name from customer_profile as cf join customer as c on cf.customer_id = c.id where cf.isLoggedIn = True
-- select c.first_name, cf.isLoggedIn from customer as c left join customer_profile as cf on cf.customer_id = c.id
-- select count(*) from customer as c left join customer_profile as cf on cf.customer_id = c.id where cf.isLoggedIn is not false



-- Part II:

-- 1. Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

-- create table book(
-- book_id serial primary key,
-- title text not null,
-- author text not null)

-- 2. Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee

-- insert into book values
-- (default, 'Alice In Wonderland', 'Lewis Caroll'),
-- (default, 'Harry Potter', 'J.K Rowling'),
-- (default, 'To Kill A Mockingbird', 'Harper Lee')

-- 3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age.
-- Make sure that the age is never bigger than 15 (Find an SQL method);

-- create table student(
-- student_id serial primary key,
-- name text not null unique,
-- age smallint,
-- check (age between 0 and 16))

-- 4. Insert those students:
-- John, 12
-- Lera, 11
-- Patrick, 10
-- Bob, 14

-- insert into student values
-- (default, 'John', 12),
-- (default, 'Lera', 11),
-- (default, 'Patrick', 10),
-- (default, 'Bob', 14)

-- 5. Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

-- create table library(
-- book_fk_id int not null,
-- student_id int not null,
-- borrowed_date date,
-- primary key (book_fk_id, student_id),
-- foreign key (book_fk_id) references book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- foreign key (student_id) references student (student_id) ON DELETE CASCADE ON UPDATE CASCADE)


-- 6. Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021

-- insert into library values
-- ((select book_id from book where title ilike '%wonderland%'), (select student_id from student where name = 'John'), '2022-02-15'),
-- ((select book_id from book where title ilike '%kill%'), (select student_id from student where name = 'Bob'), '2021-03-03'),
-- ((select book_id from book where title ilike '%wonderland%'), (select student_id from student where name = 'Lera'), '2021-05-23'),
-- ((select book_id from book where title ilike '%Potter%'), (select student_id from student where name = 'Bob'), '2021-08-12')


-- 7. Display the data
-- Select all the columns from the junction table
-- Select the name of the student and the title of the borrowed books
-- Select the average age of the children, that borrowed the book Alice in Wonderland
-- Delete a student from the Student table, what happened in the junction table ?

-- select * from library

-- select s.name, b.title from (student as s join library as l on s.student_id = l.student_id)
-- join book as b on l.book_fk_id = b.book_id

-- select avg(s.age) from (book as b join library as l on b.book_id = l.book_fk_id)
-- join student as s on l.student_id=s.student_id
-- where b.title ilike '%wonderland%'

-- delete from student where name = 'Patrick'
--nothing happened because I selected a student that didnt borrow any books. If I selected any other it would have wiped all rows
--with that student from the junction table because we included ON DELETE CASCADE ON UPDATE CASCADE.