pipeline {
    agent any 
    options {
        timestamps()
        timeout(time: 1, unit: 'MINUTES') 
    }
    environment {
        secret = credentials('TEST')
        SCLC = "TEST2"
    }
    parameters {
        choice(name: 'CHOICES', choices: ['nodejs', 'python', 'all'], description: 'Pick appication something')
    }
    stages {
      stage("build") {
        steps{
          sh'''
          echo "${params.PERSON}"
          '''
        }
      }
    }
}
