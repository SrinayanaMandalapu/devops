pipeline {
    agent any


    environment {
        PYTHON = "C:\\Users\\manda\\AppData\\Local\\Programs\\Python\\Python312" 
        PATH = "${PYTHON};${PYTHON}\\Scripts;${env.PATH}"
    }


    stages {

        stage('Install Dependencies') {
            steps {
                echo '🔹 Installing dependencies using pip...'
                bat 'pip install -r requirements.txt'
            }
        }


        stage('Run Tests') {
            steps {
                echo '🔹 Running pytest...'
                bat 'pip install pytest'
                bat 'pytest --maxfail=1 --disable-warnings -q'
            }
        }


        stage('Archive Artifacts') {
            steps {
                echo '🔹 Archiving build artifacts...'
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }


    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check console output for details.'
        }
    }
}

