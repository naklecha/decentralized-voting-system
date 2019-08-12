# decentralized-voting-system

A decentralized voting system where a user can walk into a government authorized center (Ex- banks, telecom companies etc.) and cast their vote using the proposed portal.

**NOTE:** All diagrams are made by me and appropriate credits must be given before copying it.
## Key Advantages

 - **No VoterID required** as 1 vote (coin) is granted to each valid user (age: 18+) from the Aadhaar database 
 - **Secure vote** by Azure blockchain and biometric authentication (using pre-existing Aadhaar database)
 - **Reduced cost** during election process
 - **Shorter wait times** as it is decentralized
 - A vote can be cast from **anywhere in the country**
 - **Highly scalable** design
 - **Efficient election system** in which the portal can be up for days together, in turn **increasing voter turnout**
 - Portal **front end** can provide useful information on the candidate and **can aid in their decision making** (display promises, proposals etc.)

## A Vote's Story

A user will walk into a government authorized center and complete his/her biometric verification. Once the verification is complete the user will be taken to a web-based portal **(developed by me)** where he/she will be presented with the voting options. The portal then sends the information of the user's vote (encrypted) to azure blockchain service where the data will be decrypted and the vote's transaction from the user to the candidate will take place. The candidate with the most votes is elected. During each election time the users are granted one vote which will make sure only one transaction can be made by the user during the whole election process.

## Workflow Diagram

 <img src="/images/workflow_idea.PNG" alt="BLOCKCHAIN WORKFLOW" height="35%"/>
 
## Voting System Workflow

During the election time the admin will initiate the election. When the election is initiated, each valid user from the Aadhaar database is granted a vote (coin). This way when the election period starts each valid user will have 1 vote automatically and no VoterID is required. The user cannot vote again for that election period as he will have 0 votes remaining. Along with granting one vote to each valid user the candidate list is sent to the front end to the portal (which is setup at govt. authorized locations). The front end can display useful information on the candidate and can aid in their decision making (display promises, proposals etc.). The encrypted vote along with the user information is sent to the backend where the vote cast method adds the vote to the ledger and the transaction is complete.

**NOTE:** At the end of the election, if a vote is not used by a user, it is taken back and the candidate with the most votes is elected.

<img src="/images/votingsystem.PNG" alt="VOTING SYSTEM WORKFLOW" height="35%"/>

## Technologies

 - Azure Blockchain
 - Aadhaar API service
 - Docker (deployment of portal on the cloud)
 - Flask (web framework)
 - Python 
 
### Author

 - Email: nishant.aklecha@gmail.com
 - LinkedIn: https://www.linkedin.com/in/naklecha
 - CodeChef: https://www.codechef.com/users/naklecha
 - PYPI: https://pypi.org/user/naklecha
 - GitHub: https://github.com/Naklecha
