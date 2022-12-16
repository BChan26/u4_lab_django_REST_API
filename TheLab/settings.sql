CREATE DATABASE teamsrosters;
CREATE USER sportuser WITH PASSWORD 'sportpassword';
GRANT ALL PRIVILEGES ON DATABASE teamsrosters TO sportuser;
GRANT postgres TO sportuser;
