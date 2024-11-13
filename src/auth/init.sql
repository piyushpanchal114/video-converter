-- CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123';

-- GRANT ALL PRIVILEGES ON DATABASE micro1 TO 'auth_user'@'localhost';

-- USE micro1;


-- CREATE TABLE user (
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     email VARCHAR(255) NOT NULL,
--     password VARCHAR(255) NOT NULL
-- )

-- INSERT INTO user (email, password) VALUES ("admin@admin.com", "admin")


CREATE TABLE public.user (
    id serial not null primary key,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO public.user (email, password) VALUES ('admin@admin.com', 'admin');

