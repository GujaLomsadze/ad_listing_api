CREATE TABLE ad_and_manager (
    ad_id INT,
    manager_id INT,
    PRIMARY KEY (ad_id, manager_id),
    FOREIGN KEY (ad_id) REFERENCES ads(entry_id),
    FOREIGN KEY (manager_id) REFERENCES managers(entry_id)
);
