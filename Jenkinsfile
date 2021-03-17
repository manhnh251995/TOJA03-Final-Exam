pipeline {
    agent any
    options {
        timestamps()
        timeout(time: 1, unit: 'MINUTES') 
    }
    environment {
        PASSWORD_DOCKER_HUB = credentials('docker-registry-pass')
        VERSION = "latest"
    }
    parameters {
        choice(name: 'CHOICE', choices: ['NodeJS', 'Python', 'all'], description: 'Pick something')
    }
    stages {
        //STEP Build application
        stage('build NodeJS'){
            when {
            expression { params.CHOICE == 'NodeJS' }
            }
            steps {
                sh'''
                echo "hello nodeJS"
                sh buildNodeJS.sh
                '''
            }
        }
        stage('build Python'){
            when {
            expression { params.CHOICE == 'Python' }
            }
            steps {
                sh'''
                echo "hello Python"
                sh buildPython.sh
                '''
            }
        }
        stage('build ALL'){
            when {
            expression { params.CHOICE == 'all' }
            }
            steps {
                echo "hello All"
            }
        }
    }    
}
