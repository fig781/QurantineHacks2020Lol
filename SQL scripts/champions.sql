CREATE TABLE IF NOT EXISTS champions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    game_id bigINT,
    champion_id smallint,
    team_id tinyint,
    damage_dealt mediumint,
    assists tinyint,
    kills tinyint,
    total_healing mediumint,
    total_minions_killed smallint,
    win boolean,
    first_blood_kill boolean,
    first_tower_kill boolean,
    vision_score tinyint
)  ENGINE=INNODB;