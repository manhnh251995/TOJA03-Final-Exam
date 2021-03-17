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
      agent { lable 'master'}
      steps{
        sh'''
        echo "Manhnh"
        '''
      }
    }
  }
}
