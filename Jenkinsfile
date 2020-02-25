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
		cron('*/30 * * * *')
	}

	stages {
		stage('test') {
			steps {
				// sh 'python3.6 -u moc-health-check/automate.py'
				sh 'pwd'
				sh 'ls -la'
				sh '/Python-3.7.3/python --version'
				sh '/Python-3.7.3/python -u moc-health-check/automate.py'
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