-- Chalk SQL resolvers can also run more complex queries
-- than just mapping in a single table. This query
-- calculates the average number of rides per driver
-- and returns it as a single value.
--
-- This query may take a while to execute, so we'll add
-- a max-staleness of 48 hours to this feature, and
-- re-compute it every 24 hours.
--
-- resolves: Averages
-- source: postgresql
-- cron: 24h
select avg(num_rides) as num_total_rides from (
    SELECT count(*) as num_rides
    FROM reviews
    GROUP BY driver_id
) ride_counts