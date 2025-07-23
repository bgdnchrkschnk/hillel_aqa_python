pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Використання облікових даних для клонування репозиторію
                git 'https://github.com/bgdnchrkschnk/hillel_aqa_python.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest -m TestFlaskContent'
            }
        }
    }
}