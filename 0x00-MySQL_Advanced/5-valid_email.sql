-- This trigger is executed after an update operation on the 'users' table.
-- It checks if the 'email' field has been changed.
-- If the 'email' field is updated, it sets the 'valid_email' field to 0.
-- Drop the trigger if it already exists
DELIMITER $$ ;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;$$
delimiter ;
