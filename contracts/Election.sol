pragma solidity 0.4.24;

contract Election {
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    bool goingon = true;
    mapping(address => bool) public voters;
    mapping(uint => Candidate) public candidates;
    uint public candidatesCount;

    event votedEvent (
        uint indexed _candidateId
    );

    constructor () public {
        addCandidate("Candidate 1");
        addCandidate("Candidate 2");
        addCandidate("Candidate 3");
        addCandidate("Candidate 4");
        addCandidate("Candidate 5");
        addCandidate("Candidate 6");
        addCandidate("Candidate 7");
        addCandidate("Candidate 8");
        addCandidate("Candidate 9");
        addCandidate("Candidate 10");
    }

    function addCandidate (string memory _name) private {
        candidatesCount ++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    function end () private {
        goingon = false;
    }

    function vote (uint _candidateId) public {
        require(!voters[msg.sender],"Already voted");

        require(_candidateId > 0 && _candidateId <= candidatesCount,"Invalid candidate");

        require(goingon,"Election ended");

        voters[msg.sender] = true;

        candidates[_candidateId].voteCount ++;

        emit votedEvent(_candidateId);
    }
}