pipeline {
    agent any
    options {
        timestamps()
        timeout(time: 1, unit: 'MINUTES') 
    }
    environment {
        secret = credentials('TEST')
        VERSION = "latest"
    }
    parameters {
        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
    }
    stages {
        stage('Example') {
            steps {
               echo "Choice: ${params.CHOICE}"
            }
        }
    }
}
