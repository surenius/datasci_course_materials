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
