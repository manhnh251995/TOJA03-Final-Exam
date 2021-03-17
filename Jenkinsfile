pipeline{
  agent none
  options {
    timeout(time: 1, unit: 'MINUTES') 
  }
  environment {
    VERSION = "latest"
    PASSWORD = credentials("docker-registry-pass")
  }
  parameters { choice(name: 'CHOICES', choices: ['nodejs','python','all'],descrition: 'Enter your app you want deploy')}
  statges{
    state("Test"){
      steps {
        sh'''
          echo "Test"
        '''
      }
    }
  }
}
