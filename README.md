# decentralized-voting-system

A decentralized voting system where a user can walk into a government authorized center (Ex- banks, telecom companies etc.) and cast their vote using the proposed portal.

## Key Advantages

 - **No VoterID required** as 1 vote (coin) is granted to each valid user (age:18) from the Aadhar database 
 - **Secure vote** by Azure blockchain and biometric authentication (using pre-existing Aadhar database)
 - **Reduced cost** during election process
 - **Shorter wait times** as it is decentralized
 - A vote can be cast from **anywhere in the country**
 - **Highly scalable** design
 - **Longer election periods** as the portal can be up for days together, in turn **increasing voter turnout**
 - Portal **front end** can provide useful information on the candidate and **can aid in their decision making** (display promises, proposals etc.)

## A Vote's Story

A user will walk into a government authorized center and complete his/her biometric verification. Once the verification is complete the user will be taken to a web-based portal **(developed by me)** where he/she will be presented with the voting options. The portal then sends the information of the user's vote (encrypted) to azure blockchain service where the data will be decrypted and the vote's transaction from the user to the party will take place. The party with the most votes is elected. During each election time the users are granted one vote which will make sure only one transaction can be made by the user during the whole election process.

**NOTE:** All diagrams are made by me and appropriate credits must be given before copying it.
## Workflow Diagram

 <img src="blockchain.PNG" alt="BLOCKCHAIN WORKFLOW" height="350px"/>

## Voting System Workflow

During the election time the admin will initiate the election. When the election is initiated, each valid user from the Aadhar database is granted a vote (coin). This way when the election period starts each valid user will have 1 vote automatically and no VoterID is required. The user cannot vote again for that election period as he will have 0 votes remaining. Along with granting one vote to each valid user the candidate list is sent to the front end to the portal (which is setup at govt. authorized locations). The front end can display useful information on the candidate and can aid in their decision making (display promises, proposals etc.). The encrypted vote along with the user information is sent to the backend where the vote cast method adds the vote to the ledger and the transaction is complete. 

**NOTE:** At the end of the election, if a vote is not used by a user, it is taken back and the candidate with the most votes is elected.

<img src="voting_system.PNG" alt="VOTING SYSTEM WORKFLOW" height="400px"/>

## Technologies

 - Azure Blockchain
 - Docker (deployment of portal)
 - Flask (web framework)
 - Python 
 
**NOTE:** This is my idea for CodeFunDo2019.
