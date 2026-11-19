
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando el proyecto...'
                sh 'python3 -m py_compile app.py'
                echo 'Build completado correctamente'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                sh 'python3 -m unittest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando en entorno de prueba...'
                sh 'mkdir -p deployment-test'
                sh 'cp app.py deployment-test/'
                sh 'cd deployment-test && python3 app.py'
                echo 'Deploy completado correctamente'
            }
        }
    }
}
