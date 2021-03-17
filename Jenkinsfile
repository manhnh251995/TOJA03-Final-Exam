pipeline {
    agent any 
    options {
        timestamps()
    }
    environment {
        secret = credentials('TEST')
        SCLC = "TEST2"
    }
    parameters {
        choice(name: 'CHOICE', choices: ['One', 'Two', 'Three'], description: 'Pick something')
    }
    stages {
      stage("build") {
        steps{
          sh'''
          echo $(date)
          '''
        }
      }
    }
}
