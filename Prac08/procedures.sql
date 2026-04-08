--2 exercise
CREATE OR REPLACE PROCEDURE upsert_contacts(
    p_name VARCHAR,
    p_phone VARCHAR
)
AS $$
BEGIN 
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone 
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

--3 exercise
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names VARCHAR[],
    phones VARCHAR[]
)
AS $$
DECLARE
    i INSERT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\+\d{1}\s\d{3}\s\d{3}\s\d{4}$' THEN
            INSERT INTO contacts(name, phone)
            VALUES (names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: % for %', phones[i], names[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

--5 exercise
CREATE OR REPLACE PROCEDURE delete_by_name(name_to_delete VARCHAR)
AS
$$
BEGIN 
    DELETE FROM contacts WHERE contacts.name = name_to_delete;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE delete_by_phone(phone_to_delete VARCHAR)
AS
$$
BEGIN 
    DELETE FROM contacts WHERE contacts.phone = phone_to_delete;
END;
$$
LANGUAGE plpgsql;