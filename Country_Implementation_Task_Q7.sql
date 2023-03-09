-- This task was not finished.
-- Hence the table was updated with zeros instead of medians.
-- Filling the daily_vaccinations column with 0s.
UPDATE country_vaccination_stats
SET daily_vaccinations = COALESCE(daily_vaccinations, 0)

SELECT country,date,daily_vaccinations,vaccines from country_vaccination_stats
