#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "guest" <<-EOSQL
    CREATE DATABASE monitoring_system;
    \c monitoring_system;
    CREATE TYPE status_type AS ENUM('pending', 'failed', 'success');
    CREATE TABLE tasks (
    id serial PRIMARY KEY,
    name VARCHAR ( 255 ) unique NOT NULL,
    content VARCHAR ( 255 ) unique NOT NULL,
    status status_type DEFAULT 'pending',
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
EOSQL