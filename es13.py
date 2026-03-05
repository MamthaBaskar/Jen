//Experiment 1: Basic Pipeline with Parameter and BAT Command
1. 
pipeline {
    agent any

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello Jenkins', description: 'Enter message')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Print Parameter') {
            steps {
                echo "Message is: ${params.MESSAGE}"
            }
        }

        stage('Run BAT Command') {
            steps {
                bat 'echo Hello from Jenkins'
            }
        }
    }
}
2.
pipeline {
    agent any

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Test Message', description: 'Enter message')
    }

    stages {

        stage('Checkout Updated Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Show Date') {
            steps {
                bat 'date /t'
            }
        }

        stage('Print Parameter') {
            steps {
                echo "Message is: ${params.MESSAGE}"
            }
        }
    }
}
3.
pipeline {
    agent any

    stages {

        stage('Checkout Latest Commit') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create File') {
            steps {
                bat 'echo Jenkins Output > output.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type output.txt'
            }
        }
    }
}
4.
pipeline {
    agent any

    parameters {
        string(name: 'USERNAME', defaultValue: 'User', description: 'Enter username')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create File') {
            steps {
                bat 'echo %USERNAME% > user.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type user.txt'
            }
        }
    }
}


//Experiment 2: Boolean and Choice Parameters

1.
pipeline {
    agent any

    parameters {
        booleanParam(name: 'RUN_TEST', defaultValue: false, description: 'Run Test?')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Check Boolean') {
            steps {
                script {
                    if (params.RUN_TEST) {
                        bat 'echo Running Test'
                    } else {
                        echo 'RUN_TEST is false'
                    }
                }
            }
        }

    }
}

2.
pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['DEV', 'TEST', 'PROD'], description: 'Select Environment')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Print Environment') {
            steps {
                echo "Selected Environment: ${params.ENVIRONMENT}"
            }
        }

    }
}

3.

pipeline {
    agent any

    parameters {
        string(name: 'BUILD_NAME', defaultValue: 'Build1', description: 'Enter build name')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create File') {
            steps {
                bat 'echo %BUILD_NAME% > build.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type build.txt'
            }
        }

    }
}

4.
pipeline {
    agent any

    parameters {
        string(name: 'NAME', defaultValue: 'Jenkins', description: 'Enter Name')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Show Workspace Path') {
            steps {
                echo "Workspace Path: ${env.WORKSPACE}"
            }
        }

        stage('Print Parameter') {
            steps {
                echo "Parameter Value: ${params.NAME}"
            }
        }

    }
}


//Experiment 3: Simple Build Simulation

1.
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Compile') {
            steps {
                bat 'echo Compiling...'
            }
        }

        stage('Build Success') {
            steps {
                bat 'echo Build Successful'
            }
        }

    }
}

2.
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create Build Folder') {
            steps {
                bat 'mkdir build'
            }
        }

        stage('Copy Files') {
            steps {
                bat 'copy * build'
            }
        }

    }
}

3.
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('List Files') {
            steps {
                bat 'dir'
            }
        }

        stage('Show Timestamp') {
            steps {
                echo "Build Time: ${new Date()}"
            }
        }

    }
}

4.
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create Artifact') {
            steps {
                bat 'echo Build Artifact > artifact.txt'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'artifact.txt'
            }
        }

    }
}



