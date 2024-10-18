-- This query retrieves the total number of fans for metal bands grouped by their origin.
-- It selects the origin and the sum of fans, aliases the sum as nb_fans.
-- The results are grouped by origin and ordered in descending order by the number of fans.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
