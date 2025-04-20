pipeline {
  agent any

  environment {
    IMAGE_NAME = 'flipify'
    CONTAINER_NAME = 'flipify_app'
    APP_PORT = '8081'
  }

  stages {

    stage('Check Commit Message') {
      steps {
        script {
          def commitMessage = sh(script: "git log -1 --pretty=%B", returnStdout: true).trim()
          if (!commitMessage.startsWith("Deploy")) {
            currentBuild.result = 'ABORTED'
            error("Not a deployment commit. Skipping...")
          }
        }
      }
    }

    stage('Git Pull') {
      steps {
        git credentialsId: 'github-user', url: 'https://github.com/geezera/flipify.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $IMAGE_NAME .'
      }
    }

    stage('Stop & Remove Old Container') {
      steps {
        script {
          sh "docker rm -f $CONTAINER_NAME || true"
        }
      }
    }

    stage('Run New Container') {
      steps {
        sh """
          docker run -d --name $CONTAINER_NAME -p $APP_PORT:$APP_PORT $IMAGE_NAME
        """
      }
    }
  }

  post {
    success {
      echo '🎉 Deployment successful!'
    }
    failure {
      echo '❌ Deployment failed.'
    }
  }
}
