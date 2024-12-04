from database import engine, session_factory
from models import Worker


def create_table_worker():
    Worker.metadata.create_all(engine)
    

# create_table_worker()


def insert_worker():
    volk = Worker(username="volk")
    with session_factory() as s:
        s.add(volk)
        s.commit()


# insert_worker()


def update_worker():
    with session_factory() as s:
        user = s.query(Worker).filter_by(username="volk").first()
        user.username = "XXXXX"
        s.commit()

# update_worker()


def del_worker():
    with session_factory() as s:
        user = s.query(Worker).filter(Worker.worker_id==2).first()
        s.delete(user)
        s.commit()
    
del_worker()
    