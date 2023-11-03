-- This resolver maps our `rides` table from our PostgreSQL
-- database to our Chalk feature type, called `Ride`.
--
-- When you go to deploy this resolver, Chalk checks that the
-- `Ride` feature class exists, and that it has the fields
-- `id`, `name`, and `dob` (lining up with the columns returned
-- by the query below).
--
-- Any comment here appears in the Chalk Dashboard.
--
-- resolves: Ride
-- source: postgresql
SELECT 
  id,
  driver_id,
  vehicle_id
FROM rides
