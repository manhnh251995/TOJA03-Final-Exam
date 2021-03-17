pipeline {
  agent none
  environment {
  IMAGE = "toja03"
  PASSWORD = credentials("docker-registry-pass")
  }
  options {
        timeout(time: 1, unit: 'MINUTES') 
    }
  parameters { choice(name: 'CHOICES', choices: ['nodejs','python','all'],descrition: 'Enter your app you want deploy')}
  stages {
    stage("Build Image) {
      steps {
        sh'''
        echo "A Bau"
        ''
      }
    }
  }
 }
