CREATE TABLE champions_processed_data (
  champion_id smallint primary key,
  win_percentage decimal(4,2),
  win_percentage_blue decimal(4,2),
  win_percentage_red decimal(4,2),
  avg_kills tinyint,
  avg_assists tinyint,
  avg_total_damage_dealt mediumint,
  avg_total_healing mediumint,
  avg_minions_killed smallint,
  avg_vision_score decimal(4,2),
  avg_game_duration smallint,
  first_blood_win_percent decimal(4,2),
  first_dragon_win_percent decimal(4,2),
  first_tower_win_percent decimal(4,2)
)  ENGINE=INNODB;