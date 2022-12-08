-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all film languages.
-- select * from language

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
-- select f.title, f.description, l.name 
-- from film as f
-- join language as l
-- on l.language_id = f.language_id
-- order by f.title

-- Get all films, even if they don’t have languages.
-- select title from film

-- Get all languages, even if there are no films in those languages.
-- select name from language


-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
-- Delete a film that has a review from the new_film table, what happens to the customer_review table?

-- create table new_film (
-- id serial primary key,
-- name varchar(50))

-- create table customer_review(
-- review_id int primary key not null,
-- film_id int references new_film (id) on delete cascade,
-- language_id int references language (language_id),
-- title varchar(50),
-- review_text text,
-- last_update date
-- )

-- insert into new_film values
-- (default, 'LotR: Fellowship of the Ring'),
-- (default, 'LotR: Two Towers'),
-- (default, 'LotR: Return of the King'),
-- (default, 'Star Wars Episode I'),
-- (default, 'Star Wars Episode II'),
-- (default, 'Star Wars Episode III'),
-- (default, 'Star Wars Episode IV'),
-- (default, 'Star Wars Episode V'),
-- (default, 'Star Wars Episode VI')

-- insert into customer_review values
-- (1, (SELECT id FROM new_film where name ilike '%fellowship%'),
-- (select language_id from language where name ilike '%english%'), 'Amazing film',
-- '100% will watch again', '2010-10-10')

-- insert into customer_review values
-- (3, 
--  (select id from new_film where name ilike '%Star Wars Episode VI%'),
-- (select language_id from language where name ilike '%german%'),
--  'Terrible',
-- 'Will never watch again', 
--  '2008-10-10')

-- delete from new_film where name = 'Star Wars Episode VI'
--This will delete a whole row with the referenced ID from the child table 

-- select * from customer_review


-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- update  film
-- set  language_id = 2 where film_id > 10 and film_id < 21
-- update  film
-- set  language_id = 3 where film_id > 20 and film_id < 31
-- update  film
-- set  language_id = 4 where film_id > 30 and film_id < 41

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--address_id is the foreign key referencing the address_id from the address table.

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- drop table customer_review

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- select count(*) from rental where return_date is null

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
-- select r.inventory_id, i.film_id, f.title, f.rental_rate
-- from (inventory as i join rental as r on i.inventory_id = r.inventory_id)
-- join film as f on i.film_id = f.film_id 
-- order by f.rental_rate desc
-- limit 30



-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names.
-- Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- select f.title, f.film_id, a.first_name, a.last_name, a.actor_id 
-- from (actor as a join film_actor as fa on a.actor_id = fa.actor_id)
-- join film as f on fa.film_id = f.film_id
-- where a.first_name = 'Penelope' and a.last_name = 'Monroe' and f.description ilike '%sumo wrestler%'


-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- select f.title, f.length, f.rating, c.name from (category as c join film_category as fc on c.category_id = fc.category_id)
-- join film as f on fc.film_id = f.film_id
-- where c.name = 'Documentary' and f.length < 60 and f.rating = 'R'

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- select f.title
-- from(customer as c join payment as p on c.customer_id = p.customer_id)
-- join rental as r on p.rental_id = r.rental_id
-- join inventory as i on r.inventory_id = i.inventory_id
-- join film as f on i.film_id = f.film_id
-- where c.first_name = 'Matthew' and c.last_name = 'Mahan' and p.amount > 4 and  '2005-07-28' < r.return_date and  r.return_date < '2005-08-01'  


-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

