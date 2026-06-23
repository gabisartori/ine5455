pragma solidity 0.8.0;

contract ClientContractorContract {
    
    address owner = msg.sender; //dono do contrato é o criador

    enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }
    enum ObligationStatus { Created, InEffect, Completed}

    Status status;
    
    string client;
    string contractor;
    int creationDate;
    string memory[] public obligations;
    ObligationStatus[] public obligation_status;

    // INCOMPLETO

    constructor( string memory _client, string memory _contractor, int _creationDate ) public {
        client = _client;
        contractor = _contractor;
    	creationDate = _creationDate;
        status = Status.Created;
    }

    function add_obligation(string memory obligation) public {
        obligations.push(obligation);
        obligation_status.push(ObligationStatus.Created);
    }

    function terminate() public {
        bool has_incomplete = false;
        for (uint256 i = 0; i < obligations.length; ) {
            if (obligation_status[i] != ObligationStatus.Completed) {
                has_incomplete = true;
            }
        }
        if (has_incomplete) {
            status = Status.UnsuccessfulTermination;
        } else {
            status = Status.SuccessfulTermination;
        }
    }
    //SETTERS
    
   	function activate () public {  	
    	status = Status.InEffect;
        for (uint256 i = 0; i < obligations.length; ) {
            obligation_status[i] = ObligationStatus.InEffect;
        }
    }


    //GETTERS
    
    //view significa que nao tem transacao, nao precisa minerar (nao usa gas para executar)
    
    function getStatus() public view returns (Status) {
        return status;
    }

    function getClient() public view returns (string memory) {
        return client;
    }
    
    function getCreationDate() public view returns (int) {
        return creationDate;
    }

    function close() public returns (bool) {
        return true;
    }

    function is_created() public returns (bool) {
        return status == Status.Created;
    }

    function is_in_effect() public returns (bool) {
        return status == Status.InEffect;
    }

    function is_successful() public returns (bool) {
        return status == Status.SuccessfulTermination;
    }
    
    function is_unsuccessful() public returns (bool) {
        return status == Status.UnsuccessfulTermination;
    }

    function set_obligation_as_complete(string memory obligation) public {
        uint256 index = 0;
        for (uint256 i = 0; i < obligations.length;) {
            if (obligations[i] == obligation) {
                index = i+1;
            }
        }
        if (index > 0) {
            obligation_status[index-1] = ObligationStatus.Completed;
        }
    }

}