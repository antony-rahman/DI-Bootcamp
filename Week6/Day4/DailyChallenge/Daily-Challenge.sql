-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.

-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

-- Create a function that returns the total price for a given order.

-- Bonus :
-- Create a table called users.
-- There should be a one to many relationship between the users table and the product_orders table.
-- Create a function that returns the total price for a given order of a given user.
-- create table users(
-- id serial primary key,
-- name varchar (100) not null); 

-- create table product_orders(
-- id serial primary key,
-- order_date date not null,
-- user_id int not null,
-- foreign key (user_id) references users(id));



-- create table items(
-- id serial primary key,
-- name varchar (100),
-- price float not null,
-- order_id int,
-- foreign key (order_id) references product_orders (id)
-- );

-- insert into users values
-- (default, 'Biggus Dickus'),
-- (default, 'Dorth Trader'),
-- (default, '420BillXXX'),
-- (default, 'Brandon69')

-- insert into product_orders values
-- (default, '1999-05-05', (select id from users where name = 'Brandon69')),
-- (default, '1999-05-05', (select id from users where name = 'Brandon69')),
-- (default, '2000-05-05', (select id from users where name = 'Brandon69')),
-- (default, '2006-05-05', (select id from users where name = '420BillXXX')),
-- (default, '2002-05-05', (select id from users where name = '420BillXXX')),
-- (default, '2003-05-05', (select id from users where name = 'Dorth Trader')),
-- (default, '2003-05-05', (select id from users where name = 'Dorth Trader'))

-- insert into items values
-- (default, 'AC', 4000, (select id from product_orders where id = 1)),
-- (default, 'TV', 4500, (select id from product_orders where id = 2)),
-- (default, 'Pen', 10, (select id from product_orders where id = 3)),
-- (default, 'Laptop', 2000, (select id from product_orders where id = 4)),
-- (default, 'Dog', 10000, (select id from product_orders where id = 5)),
-- (default, 'Plant', 250, (select id from product_orders where id = 6)),
-- (default, 'Pencil', 9, (select id from product_orders where id = 7))

-- create or replace function total_price (oi int)
-- returns float AS $$
-- declare
--     total sum float;
-- begin
--     total := ;
-- end;
-- $$ language plpgsql;

select id, sum(price) from (select i.name, i.price, po.id from items as i
inner join product_orders as po on i.order_id = po.id) as t
group by id
order by sum(price);