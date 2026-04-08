--1 exercise
CREATE OR REPLACE FUNCTION search_contacts(pattern VARCHAR)
RETURNS TABLE (id INTEGER, name VARCHAR(225), phone VARCHAR(20))
AS $$
BEGIN 
    RETURN QUERY
    SELECT * FROM contacts 
    WHERE contacts.name ILIKE '%' || pattern || '%'
       OR contacts.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

--4 exercise
CREATE OR REPLACE FUNCTION get_contacts_page(page_limit INTEGER, page_offset INTEGER)
RETURNS TABLE (id INTEGER, name VARCHAR(225), phone VARCHAR(20))
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM contacts
    ORDER BY contacts.id
    LIMIT page_limit
    OFFSET page_offset;
END;
$$ LANGUAGE plpgsql;