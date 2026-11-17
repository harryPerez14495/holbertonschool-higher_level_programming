-- List scores of at least 10, highest first.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
