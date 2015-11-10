SELECT docid, SUM(count) AS s FROM Frequency WHERE term in ('washington', 'taxes', 'treasury') GROUP BY docid ORDER BY s ASC;
