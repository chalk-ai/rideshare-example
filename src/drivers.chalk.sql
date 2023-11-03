-- This resolver maps our `drivers` table from our PostgreSQL
-- database to our Chalk feature type, called `Driver`.
--
-- When you go to deploy this resolver, Chalk checks that the
-- `Driver` feature class exists, and that it has the fields
-- `id`, `name`, and `dob` (lining up with the columns returned
-- by the query below).
--
-- Any comment here appears in the Chalk Dashboard.
--
-- resolves: Driver
-- source: postgresql
SELECT 
  id,
  name,
  dob
FROM drivers
