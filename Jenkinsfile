pipeline{
    agent{
        docker{
            image 'python:3.9-alpine3.15'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Build'
            }
        }
    }
}