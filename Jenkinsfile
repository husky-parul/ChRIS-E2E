pipeline {
	agent any
	triggers {
		cron('*/360 * * * *')
	}
	environment { 
        TO = 'parsingh@redhat.com'
		CC = 'maybeam@gmail.com'
    }

	stages {
		stage('test') {
			steps {
				sh '''
					pwd
					ls -la ./moc-health-check/
					python3 -u moc-health-check/automate.py
				'''
			}

			post {
				failure {
					load "env.groovy"
					echo "${env.DB_URL}"
					echo "this is env. to ${env.TO}"
					
					echo "Downloading build console output"
					sh "cat ${JENKINS_HOME}/jobs/${JOB_NAME}/builds/${BUILD_NUMBER}/log >> log.txt"
					sh "pwd"
					sh "ls -la"
					sh "cat log.txt"
					// mail bcc: 'maybeam@gmail.com', 
					// body: "Project: ${JOB_NAME} Build Number: ${BUILD_NUMBER}", 
					// subject: "ERROR CI: ${JOB_NAME}", 
					// to: "maybeam@gmail.com";
					emailext attachmentsPattern: 'log.txt', 
					body: "Something is wrong with pipeline: ${currentBuild.fullDisplayName}",
					subject: "Failed Pipeline: ${currentBuild.fullDisplayName}", 
					to: "maybeam@gmail.com"
					// mail to: "${env.TO}",
             		// subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             		// body: "Something is wrong with pipeline: ${currentBuild.fullDisplayName}""
				}
			}
		}
	}
}