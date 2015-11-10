SELECT docid, s FROM (SELECT docid, SUM(count) AS s FROM Frequency GROUP BY docid) WHERE s>300;
