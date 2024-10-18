-- This SQL query retrieves the band names and their lifespans for bands that play Glam rock.
-- The lifespan is calculated as the difference between the year the band was formed and the year they split.
-- If the band has not split, the lifespan is calculated up to the year 2022.
-- The results are ordered by lifespan in descending order.
SELECT band_name, 
CASE
    WHEN split IS NULL THEN 2022 - formed
    ELSE split - formed
END AS lifespan 
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;