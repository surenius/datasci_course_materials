select row_num, col_num, sum(x.value) value
from (
	select 
		a.row_num row_num, 
		b.col_num col_num,
		a.value * b.value value
	from A a, B b
	where a.col_num = b.row_num 
) x
group by x.row_num, x.col_num;


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
