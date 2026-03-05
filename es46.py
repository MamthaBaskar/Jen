git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

git init
git clone <repository_url>

git status
git add <file_name>
git add .
git commit -m "commit message"

git log
git log --oneline

git branch
git branch <branch_name>
git checkout <branch_name>
git checkout -b <branch_name>

git merge <branch_name>

git remote add origin <repository_url>
git remote -v

git push origin <branch_name>
git push -u origin main

git pull origin main
git fetch

git diff
git reset <file_name>
git reset --hard

git rm <file_name>
git mv <old_name> <new_name>

git stash
git stash pop

git tag <tag_name>

git show
git help
git clone <repo_url>
git status
git add .
git commit -m "message"
git push origin main
git config --list
git config --global --edit

git branch -a
git branch -d <branch_name>
git branch -D <branch_name>

git checkout main
git checkout -- <file_name>

git pull origin <branch_name>
git push origin --delete <branch_name>
git pull --rebase origin main



//Experiment 4: Manual Input and Approval

pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Approval') {
            steps {
                input message: 'Proceed with Build?'
            }
        }

        stage('Confirmation') {
            steps {
                echo "Build Approved and Continuing..."
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

        stage('User Approval') {
            steps {
                script {
                    input message: 'Do you approve this build?'
                }
            }
        }

        stage('Show Confirmation') {
            steps {
                bat 'echo Build Approved Successfully'
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

        stage('Print Build Number') {
            steps {
                echo "Build Number: ${env.BUILD_NUMBER}"
            }
        }

        stage('Status Message') {
            steps {
                echo "Build is running successfully"
            }
        }

    }
}
4.
pipeline {
    agent any

    parameters {
        string(name: 'TEXT_VALUE', defaultValue: 'Hello Jenkins', description: 'Enter text')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Save Parameter') {
            steps {
                bat 'echo %TEXT_VALUE% > message.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type message.txt'
            }
        }

    }
}


//Experiment 5: File Handling Operations

pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create File') {
            steps {
                bat 'echo This is sample file > sample.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type sample.txt'
            }
        }

    }
}

pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Append Data') {
            steps {
                bat 'echo Adding new line >> sample.txt'
            }
        }

        stage('Count Lines') {
            steps {
                bat 'find /c /v "" sample.txt'
            }
        }

    }
}

pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Rename File') {
            steps {
                bat 'rename sample.txt newfile.txt'
            }
        }

        stage('List Files') {
            steps {
                bat 'dir'
            }
        }

    }

}

pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Delete File') {
            steps {
                bat 'del newfile.txt'
            }
        }

        stage('Confirm Deletion') {
            steps {
                bat 'dir'
            }
        }

    }
}


//Experiment 6: Environment Variables
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Print Environment Variables') {
            steps {
                bat 'set'
            }
        }

        stage('Custom Message') {
            steps {
                echo "Jenkins Environment Variables Displayed"
            }
        }

    }
}

pipeline {
    agent any

    environment {
        MY_VAR = "Hello Jenkins"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Print Environment Variable') {
            steps {
                bat 'echo %MY_VAR%'
            }
        }

    }
}

pipeline {
    agent any

    parameters {
        string(name: 'VERSION', defaultValue: '1.0', description: 'Enter version')
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Create Version File') {
            steps {
                bat 'echo %VERSION% > version.txt'
            }
        }

        stage('Display File') {
            steps {
                bat 'type version.txt'
            }
        }

    }
}

pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/yourusername/jenkins-pipeline-lab.git'
            }
        }

        stage('Show Commit ID') {
            steps {
                bat 'git rev-parse HEAD'
            }
        }

        stage('Build Result') {
            steps {
                echo "Build Completed Successfully"
            }
        }

    }
}