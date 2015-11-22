select *
from (
	select row_doc, col_doc, sum(x.value) simvalue
	from (
		select 
			a.docid row_doc, 
			b.docid col_doc,
			a.count * b.count value
		from v_h a, v_h b
		where a.term = b.term 
	) x
	group by x.row_doc, x.col_doc
) y
where 
(row_doc = 'q' or col_doc = 'q')
order by simvalue asc;