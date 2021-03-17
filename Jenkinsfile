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
        choice(name: 'CHOICES', choices: ['nodejs', 'python', 'all'], description: 'Pick appication something')
    }
    stages {
      stage("build") {
        steps{
          sh'''
          echo "${params.CHOICES}"
          '''
        }
      }
    }
}
