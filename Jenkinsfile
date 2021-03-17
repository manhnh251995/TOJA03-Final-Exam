pipeline {
  agent none
  environment {
  IMAGE = "toja03"
  PASSWORD = credentials("docker-registry-pass")
  }
  options {
        timeout(time: 1, unit: 'MINUTES') 
    }
  stages{
    stage("Build"){
      steps{
        sh'''
        echo "Manhnh"
        '''
      }
    }
  }
}
