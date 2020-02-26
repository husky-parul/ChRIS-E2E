
// pipeline {
// 	agent any
// 	triggers {
// 		cron('*/30 * * * *')
// 	}

// 	stages {
// 		stage('test') {
// 			steps {
// 				// sh 'python3.6 -u moc-health-check/automate.py'
// 				sh 'pwd'
// 				sh 'ls -la'
// 				sh '/Python-3.7.3/python --version'
// 				sh '/Python-3.7.3/python -u moc-health-check/automate.py'
// 			}

// 			post {
// 				failure {
// 					load "env.groovy"
// 					echo "${env.DB_URL}"
// 					emailext attachmentsPattern: 'moc-health-check/error.log', body: "${env.DB_URL}", subject: 'test', to: 'parsingh@redhat.com'
// 				}
// 			}
// 		}
// 	}
// }

//  Above is working on image singhp11/jenkins-py

// declaring aent and env variables
pipeline {
    agent {
      node {label 'python'}
    }
	environment {
    APPLICATION_NAME = 'ChRIS-E2E'
    GIT_REPO="https://github.com/husky-parul/ChRIS-E2E"
    GIT_BRANCH="jenkins"
    STAGE_TAG = "promoteToQA"
    DEV_PROJECT = "dev"
    STAGE_PROJECT = "stage"
    TEMPLATE_NAME = "python-nginx"
    ARTIFACT_FOLDER = "target"
    PORT = 8081;
	}
	stages{
		stage("Get the latest code from branch"){
			steps{
				sh 'pwd'
				git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
			}
			
		}
		stage("Install dependencies"){
			steps{
				sh '''
				pip install virtualenv
				virtualenv --no-site-packages .app
        		source bin/activate
        		pip install -r moc-health-check/requirements.txt
        		deactivate
        		'''
			}
		}
		stage("Test"){
			steps{
				sh '''
				pwd
				source bin/activate
				ls -la
				python -V
				'''
				
			}
		}
	}
}


