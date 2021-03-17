pipeline {
    agent none 
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
            agent { label 'master' }
            steps {
                sh'''
                echo "hello nodeJS"
                ./buildNodeJS.sh
                '''
            }
        }
        stage('build Python'){
            when {
            expression { params.CHOICE == 'Python' }
            }
            agent { label 'master' }
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
            agent { label 'master' }
            steps {
                sh'''
                echo "hello All"
                sh buildNodeJS.sh && sh buildPython.sh
                '''
            }
        }
    //Deploy Application
        stage('Deploy NodeJS'){
            when {
            expression { params.CHOICE == 'NodeJS' }
            }
            agent { label 'jenkin02' }
            steps {
                sh'''
                pwd
                sh DeployNodeJS.sh 
                '''
            }
        }
        stage('Deploy Python'){
            when {
            expression { params.CHOICE == 'Python' }
            }
            agent { label 'jenkin02' }
            steps {
                sh'''
                sh DeployPython.sh 
                '''
            }
        }
        stage('Deploy ALL'){
            when {
            expression { params.CHOICE == 'all' }
            }
            agent { label 'jenkin02' }
            steps {
                sh'''
                sh DeployNodeJS.sh && sh DeployPython.sh
                '''
            }
        }
    }    
}
