# olimpiada_api

# Sobre o projeto

A finalidade deste desafio é testar as suas habilidades e conhecimento com Python 3 e Django Rest Framework. O seu objetivo será criar uma API rest para servir os dados do dataset “120 years of Olympic history: athletes and results” presente no Kaggle:


## Diagrama relacional da base de dados
![Web 1](https://github.com/MatheusSaraiva/olimpiada_api/blob/main/diagrama.png)

# Tecnologias utilizadas
## Back end
- Python
- Django Rest Framework
- SQLite

# Como executar o projeto

Pré-requisitos: Python 3

```bash
# clonar repositório
$ git clone -b main https://github.com/MatheusSaraiva/olimpiada_api.git

# Para instalar as dependências "requirements.txt"
$ pip install -r requirements.txt

# executar o projeto
$ python manage.py runserver

# abrir o projeto
http://127.0.0.1:8000/
ou 
para usar documentação swagger
http://127.0.0.1:8000/swagger/ 

```

# Como popular os dados do dataset no projeto
```bash
# Você poderá baixar o dataset no link
https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv

# Execultar o script para popular no banco de dados
$ python popular_db.py
```
### Hospegem da API no servidor Heroku
https://olimpiada-api.herokuapp.com/swagger/


# Autor

Matheus Saraiva

https://www.linkedin.com/in/matheus-saraiva-37568520b/

