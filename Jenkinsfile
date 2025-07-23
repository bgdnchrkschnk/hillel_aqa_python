pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Використання облікових даних для клонування репозиторію
                git branch: 'main', url: 'https://github.com/bgdnchrkschnk/hillel_aqa_python.git'
            }
        }
        stage('Setting up environment dependencies') {
            steps {
                sh '''apt-get update
                apt-get install -y python3 python3-dev
                apt install -y python3-pip
                rm -rf venv
                apt install -y python3.11-venv'''
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv .venv
                source .venv/bin/activate
                pip install -r requirements.txt'''
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest -m TestFlaskContent'
            }
        }
    }
}