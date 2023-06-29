from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return (jobs)

# *******************************************************************************
#  Practice code

# with engine.connect() as conn:
#   result = conn.execute(text("SELECT * FROM jobs"))
#   # print('type(result) : ', type(result))
#   # result_all = result.all()
#   # print('\n type of result_all : ', type(result_all))
#   # first = result_all[0]
#   # print('first type', type(first))
#   # print(first._asdict())
#   result_dicts = []

#   for row in result.all():
#     result_dicts.append(row._asdict())

#   print(result_dicts)
