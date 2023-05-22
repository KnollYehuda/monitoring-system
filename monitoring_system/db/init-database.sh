#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "guest" <<-EOSQL
    CREATE DATABASE monitoring_system;
    \c monitoring_system;
    CREATE TABLE images (
    id serial PRIMARY KEY,
    name VARCHAR ( 255 ) unique NOT NULL,
    source VARCHAR ( 255 ) unique NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
EOSQL