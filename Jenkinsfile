// pipeline {
//     agent {
//         docker { image 'node:7-alpine' }
//     }
//     stages {
//         stage('Test') {
//             steps {
//                 sh 'node --version'
//             }
//         }
//     }
// }

pipeline {
	agent any
	triggers {
		cron('*/360 * * * *')
	}

	stages {
		stage('test') {
			steps {
				// sh 'python3.6 -u moc-health-check/automate.py'
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
					emailext attachmentsPattern: 'moc-health-check/error.log', body: "${env.DB_URL}", subject: 'test', to: 'parsingh@redhat.com'
				}
			}
		}
	}
}