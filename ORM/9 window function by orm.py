from database import session_factory
from models import Author, Genre, Book, Supply
from sqlalchemy import Integer, cast, func, select
from sqlalchemy.orm import aliased



#оконная функция

sql3 = '''
WITH t2 AS (
    SELECT *, round(CAST(float8  (price - avg_price) as numeric),2) as diff
        FROM (
        SELECT
            a.name_author,
            b.title,
            b.price,
            round(avg(b.price) over(PARTITION BY name_author)::numeric, 2) as avg_price
        FROM book b
        JOIN author a ON b.author_id = a.author_id) t1
)
SELECT * FROM t2
ORDER BY diff DESC;
'''




def window_function():
    with session_factory() as db:
        a = aliased(Author)
        b = aliased(Book)
        subq = (
            select(
              b,
              a,
              func.round(func.avg(b.price).over(partition_by=a.name_author)).label('avg_price'),  
            )
            .join(b, a.author_id == b.author_id).subquery("t1")
        )
        cte = (
            select(
                subq.c.title,
                subq.c.name_author,
                subq.c.price,
                subq.c.avg_price,
                func.round(subq.c.price - subq.c.avg_price).label('diff'),
        )
        .cte("t2")
    )
    query = (
        select(cte)
        .order_by(cte.c.diff.desc())
    )
    print(query.compile(compile_kwargs={"literal_binds": True}))
    print(*db.execute(query).all())

window_function()