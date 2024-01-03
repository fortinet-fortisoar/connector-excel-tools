## About the connector
Security Scorecard Platform combines several threat intelligence sources to provide in-depth insights on threat hosts and attack infrastructure.This connector facilitates automated operations to pull off real-time host configuration analysis to come up with actionable threat intelligence that is vital in detection, mitigation, and remediation.
<p>This document provides information about the Security Scorecard Connector, which facilitates automated interactions, with a Security Scorecard server using FortiSOAR&trade; playbooks. Add the Security Scorecard Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Security Scorecard.</p>

### Version information

Connector Version: 1.0.0


Authored By: spryIQ.co

Contributors: Swapnil Koulgikar

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-security-scorecard`

## Prerequisites to configuring the connector
- You must have the URL of Security Scorecard server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Security Scorecard server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Security Scorecard</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the security scorecard server to connect and perform automated operations.<br>
<tr><td>API key<br></td><td>Specify the API key to access the endpoint to which you will connect and perform the automated operations.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get All Companies Portfolio<br></td><td>Retrieves a list companies of from security scorecard.<br></td><td>get_all_companies_portfolio <br/>Investigation<br></td></tr>
<tr><td>Get List of Portfolio<br></td><td>Retrieves a list portfolio of from security scorecard.<br></td><td>get_list_of_portfolio <br/>Investigation<br></td></tr>
<tr><td>Get Company Score<br></td><td>Retrieve company overall score from security scorecard.<br></td><td>get_company_score <br/>Investigation<br></td></tr>
<tr><td>Get Company Factor Score<br></td><td>Retrieve company factor score from security scorecard.<br></td><td>get_company_factor_score <br/>Investigation<br></td></tr>
<tr><td>Get Company History Score<br></td><td>Retrieve company history score from security scorecard.<br></td><td>get_company_history_score <br/>Investigation<br></td></tr>
<tr><td>Get Company History Factor Score<br></td><td>Retrieve company history factor score from security scorecard.<br></td><td>get_company_history_factor_score <br/>Investigation<br></td></tr>
<tr><td>Get Alert List<br></td><td>Retrieve list alerts triggered from security scorecard.<br></td><td>get_alert_list <br/>Investigation<br></td></tr>
<tr><td>Get Ransomware Details  <br></td><td>Retrieve ransomware details triggered from security scorecard.<br></td><td>get_ransomware_details <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Get All Companies Portfolio
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Portfolio ID<br></td><td>Specify the portfolio unique id retrieve.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SecurityScorecard": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Portfolio": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Company": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "grade": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "grade_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "industry": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "is_custom_vendor": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "last30days_score_change": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "score": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "size": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get List of Portfolio
#### Input parameters
None.

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "id": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "privacy": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "read_only": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "is_public": ""
</code><code><br>}</code>

### operation: Get Company Score
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain<br></td><td>Specify the domain of a company in SecurityScorecard.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SecurityScorecard": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Score": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "created_at": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "grade": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "grade_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "industry": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "last30day_score_change": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "score": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                "tags": []
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Company Factor Score
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain<br></td><td>Specify the domain of a company in Security Scorecard.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SecurityScorecard": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "Factor": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "grade": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "grade_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "issue_summary": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                        {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                            "count": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                            "detail_url": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                            "severity": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                            "total_score_impact": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                            "type": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    ],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "name": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "score": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ]
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Company History Score
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain<br></td><td>Specify the domain of a company in SecurityScorecard.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SecurityScorecard": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ScoreHistory": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "date": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "score": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ]
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Company History Factor Score
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Domain<br></td><td>Specify the domain of a company in SecurityScorecard.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "SecurityScorecard": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Company": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "ScoreHistory": [
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "date": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                    "score": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            ]
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Alert List
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Email ID<br></td><td>Specify the user email id in SecurityScorecard.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "entries": [],
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "page": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "size": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "sizes_by_category": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "standard": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "unread": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "prioritized": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "unread": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "customer_contacts": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "unread": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        },
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "queued": {
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "total": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;            "unread": ""
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        }
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    }
</code><code><br>}</code>

### operation: Get Ransomware Details  
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Ransomware ID<br></td><td>Specify the user ransomware id in SecurityScorecard.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "date": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "domain": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "score": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - security-scorecard - 1.0.0` playbook collection comes bundled with the Security Scorecard connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Security Scorecard connector.

- Get Alert List
- Get All Companies Portfolio
- Get Company Factor Score
- Get Company History Factor Score
- Get Company History Score
- Get Company Score
- Get List of Portfolio
- Get Ransomware Details  

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
