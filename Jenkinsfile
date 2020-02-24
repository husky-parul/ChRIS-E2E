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
	agent { node { label 'python3' } }
	triggers {
		cron('*/10 * * * *')
	}

	stages {
		stage('test') {
			steps {
				sh 'pwd'
				sh 'ls -la'
				sh 'python3 --version'
				sh 'python3 -u moc-health-check/automate.py'
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