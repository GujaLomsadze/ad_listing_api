CREATE TABLE ads (
    entry_id SERIAL PRIMARY KEY,
    company VARCHAR(255),
    ad_name VARCHAR(255),
    manager VARCHAR(255),
    ad_start_date DATE,
    ad_end_date DATE,
    comments TEXT,
    view_count INT
);
