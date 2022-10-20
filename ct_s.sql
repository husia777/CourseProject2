CREATE TABLE IF NOT EXISTS "suppliers" (
                                        suppliers_id integer PRIMARY KEY,
                                        company_name varchar NOT NULL,
                                        contact_name varchar,
                                        post varchar,
                                        country varchar DEFAULT 'NULL',
                                        state_ varchar DEFAULT 'NULL',
                                        postal_code varchar DEFAULT 'NULL',
                                        city varchar DEFAULT 'NULL',
                                        mailbox varchar DEFAULT 'NULL',
                                        phone varchar DEFAULT 'NULL',
                                        fax varchar DEFAULT 'NULL',
                                        homepage varchar DEFAULT 'NULL');