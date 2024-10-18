-- 
-- This trigger, named 'store_decrement', is executed after a new row is inserted into the 'orders' table.
-- It updates the 'items' table by decrementing the 'quantity' of the item specified in the new order.
-- The 'quantity' is reduced by the number of items ordered, as indicated by the 'NEW.number' value.
-- The 'name' column in the 'items' table is matched with the 'item_name' from the new order to identify the correct item to update.
CREATE TRIGGER store_decrement AFTER INSERT ON orders FOR EACH ROW
UPDATE items
SET
    quantity = quantity - NEW.number
WHERE
    name = NEW.item_name;
