SELECT f1.docid FROM Frequency AS f1 JOIN Frequency AS f2 ON f1.docid=f2.docid WHERE f1.term='transactions' AND f2.term='world';
