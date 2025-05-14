# UÓR_Repositorio
Repositório UÓR

Esse projecto foi gerado usando Django Framework [versão 4.2.1 ] 


Para executar o projecto precisa seguir os passos abaixo:

## 1º Passo:

- Download do projecto
  
```bash
clone https://github.com/airesfutre7/uor_repositorio.git
```
  
## 2º Passo:

# Instalar a ultima versão da Framework Django

 - Instalar a ultima versão do Python

vai ao site oficial: `https://www.python.org/downloads`

 - Verificar se python e pip estão instalados ( Abrir o terminal e digitar os comandos abaixo )

```bash
python --version
pip --version
```

-  Criar um ambiente virtual para evitar conflitos entre projectos

  ```bash
cd \uor_repositorio\
python -m venv repositorio-env

```

-  Activar o ambiente virtual

  ```bash
source repositorio-env/bin/activate

```

-  Instalar a Framework Django

  ```bash
pip install django
django-admin --version

```  

## 3º Passo:

# Executar o projecto no servidor local:

  ```bash
cd \uor_repositorio\
python manage.py runserver

```

-  Para acessar o projecto precisa ir ao navegador (Google Chrome, Firefox ) e colocar o endereço URL: `127.0.0.1:8000` 

