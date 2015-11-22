select *
from (
	select row_doc, col_doc, sum(x.value) simvalue
	from (
		select 
			a.docid row_doc, 
			b.docid col_doc,
			a.count * b.count value
		from Frequency a, Frequency b
		where a.term = b.term 
		and a.docid < b.docid
	) x
	group by x.row_doc, x.col_doc
) y
where 
(row_doc = '10080_txt_crude' and col_doc = '17035_txt_earn')
or
(row_doc = '17035_txt_earn' and col_doc = '10080_txt_crude');
