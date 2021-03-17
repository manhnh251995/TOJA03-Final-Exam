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
            agent { lable 'master'}
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
            agent { lable 'master'}
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
            agent { lable 'master'}
            when {
            expression { params.CHOICE == 'all' }
            }
            steps {
                sh'''
                echo "hello All"
                sh buildNodeJS.sh && sh buildPython.sh
                '''
            }
        }
    }    
}
