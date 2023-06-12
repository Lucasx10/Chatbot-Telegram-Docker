SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS manutencao ( 
             id INTEGER PRIMARY KEY AUTO_INCREMENT, 
             cidade VARCHAR(50),
             local VARCHAR(100), 
             motivo VARCHAR(100),
             dia datetime);

INSERT INTO `manutencao` (`id`, `cidade`, `local`, `motivo`, `dia`) VALUES (
    NULL, 'Boa Vista', 'Jardim Floresta', 'Poste quebrado', '23-05-29 14:00:00'), 
    ( NULL, 'Caracaraí', 'Vicinal 03', 'Arvore caida', '23-05-31 13:00:00'),
    ( NULL, 'Boa Vista', 'Centenario', 'Poste quebrado ', '23-05-29 14:00:00'),
    ( NULL, 'São Luiz', 'Vicinal Macunaima', 'Obras no local', '23-05-29 14:00:00');  