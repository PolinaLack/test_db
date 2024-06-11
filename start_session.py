from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    url=settings.postgres_url,
    echo=False,
    pool_size=5,
    max_overflow=10,
    )

Session = sessionmaker(bind=engine)
curr_session = Session()