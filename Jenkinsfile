pipeline {
    agent any
    environment {
        JIRA_ISSUE_KEY = 'ESS-1183'
        JIRA_API_URL = "https://infosys.atlassian.net/rest/api/latest/issue/${JIRA_ISSUE_KEY}/comment"
    }
    stages {
        stage('Installing requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Testing') {
            steps {
                 bat 'pytest --jira tests\\test_home_page.py'
               // bat 'pytest tests\\test_network_wifi_on.py'
            }
        }
    }
        post{
            always {
                script {
                    bat "C:/Users/urimilla.s/Desktop/Batfiles/cicd.bat"
                }
            }
            success{
                    script {
                    def response = httpRequest(
                    acceptType: 'APPLICATION_JSON',
                    contentType: 'APPLICATION_JSON',
                    httpMode: 'POST',
                    requestBody: '''{
                        "body": "This build was successful!::Test execution report: [Link to Report](file:///C:/ProgramData/Jenkins/.jenkins/workspace/jira/report.html)"
                    }''',
                    url: 'https://infosys.atlassian.net/rest/api/latest/issue/ESS-1183/comment',
                    authentication: 'jira_creds'
                    )
                    // Log the response for debugging purposes
                    echo "Response status: ${response.status}"
                    echo "Response content: ${response.content}"
                }
         }
         failure {
              script {
                    def response = httpRequest(
                    acceptType: 'APPLICATION_JSON',
                    contentType: 'APPLICATION_JSON',
                    httpMode: 'POST',
                    requestBody: '''{
                        "body": "This build was Failed!"
                    }''',
                    url: 'https://infosys.atlassian.net/rest/api/latest/issue/ESS-1183/comment',
                    authentication: 'jira_creds'
                    )
                    // Log the response for debugging purposes
                    echo "Response status: ${response.status}"
                    echo "Response content: ${response.content}"
                 }
             }
        } 
    }