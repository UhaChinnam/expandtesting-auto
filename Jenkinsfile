pipeline {
    agent any

    environment {
        // Inject Python into PATH so Jenkins Windows Service can find it
        PATH = "C:\\Users\\uhasu\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\uhasu\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;${env.WORKSPACE}\\venv\\Scripts;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python venv') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            python3 -m pip install --upgrade pip
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            .\\venv\\Scripts\\activate
                            python -m pip install --upgrade pip
                        '''
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pip install -r requirements.txt
                            playwright install --with-deps
                        '''
                    } else {
                        bat '''
                            .\\venv\\Scripts\\activate
                            pip install -r requirements.txt
                            python -m playwright install --with-deps
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            pytest --junitxml=reports/results.xml
                        '''
                    } else {
                        bat '''
                            .\\venv\\Scripts\\activate
                            pytest --junitxml=reports/results.xml
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive the test reports
            junit 'reports/results.xml'
            
            // Optionally archive playwright reports if you configure playwright to generate them
            // archiveArtifacts artifacts: 'playwright-report/**/*', allowEmptyArchive: true
        }
    }
}
