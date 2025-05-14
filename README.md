# UÓR_Repositorio
Repositório UÓR

Esse projecto foi gerado usando Django Framework [versão 4.2.1 ] 


Para executar o projecto precisa seguir os passos abaixo:

## 1º Passo:

Instalar a ultima versão do Python

vai ao site oficial: `https://www.python.org/downloads`

## 2º Passo:

# Instalar a ultima versão da Framework Django

 - Verificar se python e pip estão instalados ( Abrir o terminal e digitar os comandos abaixo )

```bash
python --version
pip --version
```

-  Criar um ambiente virtual para evitar conflitos entre projectos

  ```bash
python -m venv repositorio-env

```

-  Activar o ambiente virtual

  ```bash
source repositorio/bin/activate

```

-  Instalar a Framework Django

  ```bash
pip install django
django-admin --version

```  

## 3º Passo:

# Executar o projecto no servidor local:

  ```bash
cd \repositorio_UOR\repositorio
python manage.py runserver

```  




Once the server is running, open your browser and navigate to `http://localhost:4200/`. The application will automatically reload whenever you modify any of the source files.

## Code scaffolding

Angular CLI includes powerful code scaffolding tools. To generate a new component, run:

```bash
ng generate component component-name
```

For a complete list of available schematics (such as `components`, `directives`, or `pipes`), run:

```bash
ng generate --help
```

## Building

To build the project run:

```bash
ng build
```

This will compile your project and store the build artifacts in the `dist/` directory. By default, the production build optimizes your application for performance and speed.

## Running unit tests

To execute unit tests with the [Karma](https://karma-runner.github.io) test runner, use the following command:

```bash
ng test
```

## Running end-to-end tests

For end-to-end (e2e) testing, run:

```bash
ng e2e
```

Angular CLI does not come with an end-to-end testing framework by default. You can choose one that suits your needs.

## Additional Resources

For more information on using the Angular CLI, including detailed command references, visit the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.
