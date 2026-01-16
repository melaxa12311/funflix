pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out automatically by Jenkins'
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                sh 'docker build -t funflix-backend ./backend'
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                sh 'docker build -t funflix-frontend ./frontend'
            }
        }
    }

    post {
        success {
            echo '✅ Docker images built successfully!'
        }
        failure {
            echo '❌ Build failed'
        }
    }
}

