from pathlib import Path
import sqlite3
import pandas as pd

Path('./db.sqlite3').touch()


conn = sqlite3.connect('./db.sqlite3')
c = conn.cursor()

athlete_events = pd.read_csv('./athlete_events.csv')

noc_team = athlete_events.drop_duplicates(subset = "NOC")[['Team', 'NOC']]

atletas = athlete_events.drop_duplicates(subset = "ID")[['ID', 'Name', 'Sex', 'NOC', 'Sport']]
atletas = atletas.rename(columns={'NOC': 'noc_team_id'})

eventos = athlete_events[['ID', 'Age', 'Height', 'Weight', 'Games', 'Year', 'Season', 'City','Event', 'Medal']]
eventos = eventos.rename(columns={'ID': 'atleta_id'})

noc_team.to_sql('jogos_olimpicos_noc_team', conn, if_exists='append', index = False)
atletas.to_sql('jogos_olimpicos_atleta', conn, if_exists='append', index = False)
eventos.to_sql('jogos_olimpicos_evento', conn, if_exists='append', index = False)






