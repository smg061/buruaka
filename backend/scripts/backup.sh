#!bin/sh -e
docker exec -i app_db /bin/bash -c "PGPASSWORD=app  pg_dump --username app postgres --data-only --column-inserts --exclude-table alembic_version" > ./alembic/dump.sqloy