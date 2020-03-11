pipeline {
	agent any
	triggers {
		cron('*/14400 * * * *')
	}
	stages {
		stage('test') {
			steps {
				sh '''
					python3 -u moc-health-check/automate.py
				'''
			}

			post {
				always{
					sh '''
						echo "Downloading build console output"
						cat ${JENKINS_HOME}/jobs/${JOB_NAME}/builds/${BUILD_NUMBER}/log >> log.txt
						ls -la
					'''
					script{
						load "env.groovy"
						if (env.EMAIL_WAITTIME < env.EMAIL_MAXTIME){
							echo "Inside first if"
							println env.EMAIL_WAITTIME.isInteger()
							println env.EMAIL_MAXTIME.isInteger()
							println env.FAILED.isInteger()
							// println env.EMAIL_WAITTIME.multiply(env.FAILED)
							int int_current_value = env.EMAIL_WAITTIME.
							int failed = env.FAILED
							int val = int_current_value * failed
							println val
							// int current_value = new Integer(env.EMAIL_WAITTIME).intValue()
							// current_value = current_value * (env.FAILED as int)
							// echo current_value
							// int current_value = env.EMAIL_WAITTIME.toInteger() * env.FAILED.toInteger()
							// echo current_value
							// if (current_value >= env.EMAIL_MAXTIME.toInteger()){
							// 	env.EMAIL_WAITTIME=2
							// 	env.FAILED=1
							// 	echo "Send email"
							// }else{
							// 	echo "Still waiting to send email"
							// 	env.FAILED=env.FAILED.toInteger()+1
							// 	env.EMAIL_WAITTIME=env.EMAIL_WAITTIME.toInteger() * env.EMAIL_WAITTIME.toInteger()
							// 	sh "cat env.groovy"
							// }
						} else {
							echo 'I execute elsewhere'
						}

						
					}
				}
				success{
					script{
						load "env.groovy"
						if("${env.EMAIL_WAITTIME}"==1000){

							echo "------------------------ Build pass -----------------------------------------"
							emailext attachmentsPattern: 'log.txt', 
							body: "Pipeline: ${currentBuild.fullDisplayName} was successful",
							subject: "Build: ${currentBuild.fullDisplayName} passed", 
							to: "maybeam@gmail.com"

						}
						

					}
					
				}
				failure {
					script{
						load "env.groovy"
						if("${env.EMAIL_WAITTIME}"==1000){
							echo "------------------------- Build failed --------------------------------------"
							emailext attachmentsPattern: 'log.txt', 
							body: "Something is wrong with pipeline: ${currentBuild.fullDisplayName}",
							subject: "Failed Pipeline: ${currentBuild.fullDisplayName}", 
							to: "maybeam@gmail.com"
							}
					}
					}
			}
		}
	}
}