-- 1. Upsert (Вставить или Обновить)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;$$;

-- 2. Удаление по имени или телефону
CREATE OR REPLACE PROCEDURE delete_contact(p_search TEXT)
LANGUAGE plpgsql AS $$BEGIN
    DELETE FROM contacts 
    WHERE name = p_search OR phone = p_search;
END;$$;

-- 3. Массовая вставка с валидацией (например, номер должен быть из 11 цифр)
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(names VARCHAR[], phones VARCHAR[])
LANGUAGE plpgsql AS $$DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_upper(names, 1) LOOP
        -- Простая валидация: длина номера 11 символов
        IF length(phones[i]) = 11 THEN
            INSERT INTO contacts(name, phone) 
            VALUES (names[i], phones[i])
            ON CONFLICT (name) DO UPDATE SET phone = EXCLUDED.phone;
        ELSE
            RAISE NOTICE 'Invalid phone format for user %: %', names[i], phones[i];
        END IF;
    END LOOP;
END;$$;